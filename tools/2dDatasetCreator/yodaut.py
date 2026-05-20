import cv2
import numpy as np
import os
import re
import csv
import random
import yaml
from math import ceil
import matplotlib.pyplot as plt
from itertools import product
import argparse

# ---- Parámetros de línea de comandos ----
parser = argparse.ArgumentParser(description='Generador de dataset YOLO con estados, MISSING, iluminación y rotación')
parser.add_argument('--minelement', type=int, default=1)
parser.add_argument('--maxelement', type=int, default=3)
parser.add_argument('--num_images', type=int, default=50)
parser.add_argument('--min_factor', type=float, default=0.8)
parser.add_argument('--max_factor', type=float, default=1.2)
parser.add_argument('--min_angle', type=int, default=-30)
parser.add_argument('--max_angle', type=int, default=30)
parser.add_argument('--dataset_dir', type=str, default='datasets')
args = parser.parse_args()

minelement = args.minelement
maxelement = args.maxelement
num_images = args.num_images
min_factor = args.min_factor
max_factor = args.max_factor
min_angle = args.min_angle
max_angle = args.max_angle
dataset_dir = args.dataset_dir

# ---- Configuración de rutas ----
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, 'input')
images_train_dir = os.path.join(dataset_dir, 'images', 'train')
images_val_dir = os.path.join(dataset_dir, 'images', 'val')
labels_train_dir = os.path.join(dataset_dir, 'labels', 'train')
labels_val_dir = os.path.join(dataset_dir, 'labels', 'val')
preview_dir = os.path.join(dataset_dir, 'boxes_preview')

for d in [dataset_dir, images_train_dir, images_val_dir, labels_train_dir, labels_val_dir, preview_dir]:
    os.makedirs(d, exist_ok=True)

# ---- Funciones ----
def overlay_image(background, foreground, x=0, y=0):
    """Superpone foreground sobre background respetando transparencia"""
    if background.shape[2] == 3:
        background = cv2.cvtColor(background, cv2.COLOR_BGR2BGRA)
    h, w = foreground.shape[:2]
    H, W = background.shape[:2]
    if y + h > H or x + w > W:
        h = min(h, H - y)
        w = min(w, W - x)
        foreground = foreground[0:h, 0:w]
    roi = background[y:y+h, x:x+w]
    alpha = foreground[:, :, 3:] / 255.0
    inv_alpha = 1.0 - alpha
    roi[:, :, :3] = (alpha * foreground[:, :, :3] + inv_alpha * roi[:, :, :3])
    roi[:, :, 3] = np.maximum(foreground[:, :, 3], roi[:, :, 3])
    background[y:y+h, x:x+w] = roi
    return background

def apply_brightness(img, factor):
    """Multiplica canales RGB por factor, manteniendo alpha"""
    img_out = img.copy().astype(np.float32)
    img_out[:, :, :3] = np.clip(img_out[:, :, :3] * factor, 0, 255)
    return img_out.astype(np.uint8)

def rotate_image_and_boxes(image, boxes, angle, bg_fill=(0,0,0,255)):
    """
    Rota image (BGRA) sobre un canvas ampliado y rellena las zonas vacías con bg_fill (RGBA).
    Devuelve la imagen rotada y las cajas recalculadas y NORMALIZADAS respecto al TAMAÑO ROTADO.
    - boxes: list of {'combined': name, 'bbox': (cx,cy,w,h)} con coords relativas a la imagen original.
    """
    H, W = image.shape[:2]
    center = (W / 2.0, H / 2.0)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # calcular nuevo tamaño para no cortar (fórmula habitual)
    cos = abs(M[0,0])
    sin = abs(M[0,1])
    nW = int((H * sin) + (W * cos))
    nH = int((H * cos) + (W * sin))

    # ajustar la traslación de la matriz para centrar en el nuevo canvas
    M[0,2] += (nW / 2.0) - center[0]
    M[1,2] += (nH / 2.0) - center[1]

    # realizar la rotación rellenando con bg_fill (RGBA)
    border = tuple(int(x) for x in bg_fill)
    rotated = cv2.warpAffine(image, M, (nW, nH), flags=cv2.INTER_LINEAR,
                             borderMode=cv2.BORDER_CONSTANT, borderValue=border)

    # transformar cajas: convertir cada bbox a 4 esquinas, aplicar M y recomponer bbox
    new_boxes = []
    for b in boxes:
        cx, cy, w_box, h_box = b['bbox']
        # coords absolutas en original
        x_c = cx * W
        y_c = cy * H
        w_pix = w_box * W
        h_pix = h_box * H
        pts = np.array([
            [x_c - w_pix/2.0, y_c - h_pix/2.0, 1.0],
            [x_c + w_pix/2.0, y_c - h_pix/2.0, 1.0],
            [x_c + w_pix/2.0, y_c + h_pix/2.0, 1.0],
            [x_c - w_pix/2.0, y_c + h_pix/2.0, 1.0],
        ])  # shape (4,3)

        transformed = (M @ pts.T).T  # (4,2)
        xs = transformed[:,0]
        ys = transformed[:,1]
        x_min = xs.min(); x_max = xs.max()
        y_min = ys.min(); y_max = ys.max()

        # NORMALIZAR respecto al tamaño ROTADO (nW, nH) — esto es lo correcto
        cx_new = (x_min + x_max) / 2.0 / nW
        cy_new = (y_min + y_max) / 2.0 / nH
        w_new = (x_max - x_min) / nW
        h_new = (y_max - y_min) / nH

        # Clamp para garantizar 0..1
        cx_new = float(min(max(cx_new, 0.0), 1.0))
        cy_new = float(min(max(cy_new, 0.0), 1.0))
        w_new = float(min(max(w_new, 0.0), 1.0))
        h_new = float(min(max(h_new, 0.0), 1.0))

        new_boxes.append({'combined': b['combined'], 'bbox': (cx_new, cy_new, w_new, h_new)})

    return rotated, new_boxes

def draw_yolo_box(img, labels, class_to_index, estado_dict):
    H, W = img.shape[:2]
    for lbl in labels:
        cls_name = lbl['combined']
        cx, cy, w, h = lbl['bbox']
        if cls_name == 'MISSING':
            color = (255, 0, 255)
        else:
            estado = estado_dict.get(cls_name.split('_')[0], 'OK')
            color = (0, 255, 0) if estado == 'OK' else (255, 0, 0)
        x1 = int((cx - w/2.0) * W)
        y1 = int((cy - h/2.0) * H)
        x2 = int((cx + w/2.0) * W)
        y2 = int((cy + h/2.0) * H)
        cv2.rectangle(img, (x1,y1), (x2,y2), color, 2)
        cv2.putText(img, cls_name, (x1, max(y1-5,15)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    return img

# ---- Leer imágenes ----
files_in_input = [f for f in os.listdir(input_dir) if f.lower().endswith('.png')]
if 'bg.png' not in [f.lower() for f in files_in_input]:
    raise FileNotFoundError("No se encontró bg.png")
foreground_files = [f for f in files_in_input if f.lower() != 'bg.png']
pattern = re.compile(r'^\d+_([^_]+)_(.+?)(?:\s*#\d+)?\.png$')
file_info = []
for f in foreground_files:
    m = pattern.match(f)
    if not m:
        raise ValueError(f"{f} no cumple formato")
    class_id, estado = m.groups()
    file_info.append({'filename': f, 'class_id': class_id, 'estado': estado})

# ---- Agrupar por clase ----
classes = {}
for info in file_info:
    cls = info['class_id']
    classes.setdefault(cls, []).append(info)

unique_classes = sorted(classes.keys())
class_to_index = {'MISSING': 0}
for idx, cls in enumerate(unique_classes, start=1):
    class_to_index[cls + '_OK'] = len(class_to_index)
    class_to_index[cls + '_NOTOK'] = len(class_to_index)

# ---- Cargar bg ----
bg_path = os.path.join(input_dir, 'bg.png')
background_orig = cv2.imread(bg_path, cv2.IMREAD_UNCHANGED)
H_bg, W_bg = background_orig.shape[:2]

# ---- Calcular bbox promedio por clase ----
avg_bbox = {}
for cls, items in classes.items():
    bboxes = []
    for info in items:
        path = os.path.join(input_dir, info['filename'])
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        info['image'] = img
        alpha = img[:, :, 3]
        ys, xs = np.where(alpha > 0)
        x_min, x_max = xs.min(), xs.max()
        y_min, y_max = ys.min(), ys.max()
        cx = (x_min + (x_max - x_min) / 2.0) / W_bg
        cy = (y_min + (y_max - y_min) / 2.0) / H_bg
        w = (x_max - x_min) / W_bg
        h = (y_max - y_min) / H_bg
        info['bbox'] = (cx, cy, w, h)
        bboxes.append((cx, cy, w, h))
    avg_bbox[cls] = tuple(np.mean(np.array(bboxes), axis=0))

# ---- Guardar classes.txt ----
classes_txt_path = os.path.join(dataset_dir, 'classes.txt')
with open(classes_txt_path, 'w') as f:
    f.write('MISSING\n')
    for cls in unique_classes:
        f.write(cls + '_OK\n')
        f.write(cls + '_NOTOK\n')

# ---- Generar combinaciones ----
def generate_random_combos(num_images):
    combos = []
    cls_ids = list(classes.keys())
    while len(combos) < num_images:
        n_sel = random.randint(minelement, min(maxelement, len(cls_ids)))
        sel_cls = random.sample(cls_ids, n_sel)
        combo = []
        for cls in cls_ids:
            if cls in sel_cls:
                chosen = random.choice(classes[cls])
                fg_item = chosen.copy()
                fg_item['combined'] = cls + '_' + chosen['estado']
                combo.append(fg_item)
            else:
                fg_item = {'class_id': cls, 'estado': 'MISSING', 'bbox': avg_bbox[cls], 'combined': 'MISSING'}
                combo.append(fg_item)
        combos.append(combo)
    return combos

all_combos = generate_random_combos(num_images)
split_idx = int(0.8 * len(all_combos))
train_combos = all_combos[:split_idx]
val_combos = all_combos[split_idx:]

# ---- Guardar imágenes y labels ----
def save_combos(combo_list, img_dir, lbl_dir):
    total = len(combo_list)
    for i, combo in enumerate(combo_list):
        # Color de fondo aleatorio (RGB) y alpha=255
        bg_rgb = [random.randint(0, 255) for _ in range(3)]
        bg_color = (int(bg_rgb[0]), int(bg_rgb[1]), int(bg_rgb[2]), 255)
        # canvas del tamaño de bg (BGRA)
        canvas = np.zeros((H_bg, W_bg, 4), dtype=np.uint8)
        canvas[:, :, 0:3] = bg_rgb
        canvas[:, :, 3] = 255
        # Pegar bg.png sobre el canvas (bg.png no se altera)
        composed = overlay_image(canvas.copy(), background_orig)
        # Pegar foregrounds (manteniendo sus transparencias)
        lbl_items = []
        estado_dict = {c['class_id']: c['estado'] for c in combo if 'estado' in c}
        for item in combo:
            if item['combined'] != 'MISSING':
                composed = overlay_image(composed, item['image'])
            lbl_items.append({'combined': item['combined'], 'bbox': item['bbox']})
        # Iluminación aplicada a la composición completa
        factor = random.uniform(min_factor, max_factor)
        composed = apply_brightness(composed, factor)
        # Rotación: rellenar las zonas vacías con el color de fondo (bg_color)
        angle = random.uniform(min_angle, max_angle)
        rotated, new_boxes = rotate_image_and_boxes(composed, lbl_items, angle, bg_fill=bg_color)
        # Guardar imagen y etiquetas
        img_name = f"{i+1:04d}.png"
        lbl_name = f"{i+1:04d}.txt"
        cv2.imwrite(os.path.join(img_dir, img_name), rotated)
        with open(os.path.join(lbl_dir, lbl_name), 'w') as f:
            for nb in new_boxes:
                cls_idx = class_to_index.get(nb['combined'], 0)
                cx, cy, w_box, h_box = nb['bbox']
                f.write(f"{cls_idx} {cx:.6f} {cy:.6f} {w_box:.6f} {h_box:.6f}\n")
        print(f"\rGenerando imágenes: {i+1}/{total}", end='', flush=True)
    print()

print("🚀 Generando imágenes de entrenamiento:")
save_combos(train_combos, images_train_dir, labels_train_dir)
print("🚀 Generando imágenes de validación:")
save_combos(val_combos, images_val_dir, labels_val_dir)

# ---- data.yaml ----
data_yaml_path = os.path.join(dataset_dir, 'data.yaml')
data = {'train': os.path.join(dataset_dir, 'images', 'train'),
        'val': os.path.join(dataset_dir, 'images', 'val'),
        'nc': len(class_to_index),
        'names': [k for k, v in sorted(class_to_index.items(), key=lambda x: x[1])]}
with open(data_yaml_path, 'w') as f:
    yaml.dump(data, f, sort_keys=False)

# ---- index.txt ----
index_path = os.path.join(dataset_dir, 'index.txt')
with open(index_path, 'w') as f:
    for img_name in sorted(os.listdir(images_train_dir)):
        f.write(os.path.join('images', 'train', img_name) + '\n')
    for img_name in sorted(os.listdir(images_val_dir)):
        f.write(os.path.join('images', 'val', img_name) + '\n')

# ---- Preview ----
train_images = sorted(os.listdir(images_train_dir))
if train_images:
    sample_images = random.sample(train_images, min(16, len(train_images)))
    cols = 4
    rows = ceil(len(sample_images) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    axes = axes.flatten()
    for i, img_name in enumerate(sample_images):
        img_path = os.path.join(images_train_dir, img_name)
        lbl_path = os.path.join(labels_train_dir, os.path.splitext(img_name)[0] + '.txt')
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        lbl_lines = []
        with open(lbl_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 5:
                    cls_idx, cx, cy, w_box, h_box = parts
                    cls_name = list(class_to_index.keys())[int(cls_idx)]
                    lbl_lines.append({'combined': cls_name, 'bbox': (float(cx), float(cy), float(w_box), float(h_box))})
        estado_dict = {c['class_id']: c['estado'] if 'estado' in c else 'MISSING' for c in train_combos[i]}
        img = draw_yolo_box(img, lbl_lines, class_to_index, estado_dict)
        axes[i].imshow(img)
        axes[i].set_title(img_name)
        axes[i].axis('off')
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')
    preview_path = os.path.join(dataset_dir, 'dataset_preview.png')
    plt.tight_layout()
    plt.savefig(preview_path, dpi=150)
    plt.close()
