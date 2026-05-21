# 2dDatasetCreator

Script para generar datasets sintéticos de imágenes 2D para entrenar modelos YOLO.

---

## Descripción

`yodaut.py` toma imágenes de componentes individuales desde la carpeta `input/`, las combina en imágenes sintéticas con parámetros configurables y genera un dataset completo (imágenes + etiquetas YOLO) listo para entrenar.

---

## Requisitos

```bash
pip install numpy opencv-python matplotlib pyyaml
```

---

## Uso

```bash
python yodaut.py \
  --minelement 4 \
  --maxelement 15 \
  --min_factor 0.8 \
  --max_factor 1.2 \
  --min_angle -20 \
  --max_angle 20 \
  --dataset_dir directorio_salida
```

### Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| `--minelement` | Número mínimo de elementos por imagen |
| `--maxelement` | Número máximo de elementos por imagen |
| `--min_factor` | Factor de escala mínimo |
| `--max_factor` | Factor de escala máximo |
| `--min_angle` | Ángulo de rotación mínimo (grados) |
| `--max_angle` | Ángulo de rotación máximo (grados) |
| `--dataset_dir` | Carpeta de salida del dataset generado |

---

## Salida

El script crea la carpeta `dataset_dir` con la siguiente estructura:

```
directorio_salida/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Además genera una imagen `data_preview` con 16 imágenes de muestra y las cajas de las etiquetas dibujadas encima, para verificar visualmente el resultado.

---

## Preparación de entrada

Coloca las imágenes de los componentes individuales en la carpeta `input/` antes de ejecutar el script.

---

## Licencia

El código fuente se distribuye bajo **GNU General Public License v3.0 or later** (`GPL-3.0-or-later`).  
La documentación y materiales explicativos se distribuyen bajo **Creative Commons Attribution-ShareAlike 4.0 International** (`CC-BY-SA-4.0`).
