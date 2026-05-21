# tools/2dDatasetCreator

*GPL-3.0-or-later / CC-BY-SA-4.0*

---

## Descripción

Script Python (`yodaut.py`) que genera **datasets sintéticos de imágenes 2D** para entrenar modelos YOLO.

Toma imágenes de componentes de la carpeta `input/`, las combina con parámetros configurables (número de elementos, escala, ángulo de rotación) y genera un dataset con imágenes y etiquetas YOLO listo para entrenar.

---

## Instalación de dependencias

```bash
pip install numpy opencv-python matplotlib pyyaml
```

---

## Estructura de carpetas

```
2dDatasetCreator/
├── yodaut.py           # Script principal
├── input/              # Imágenes de componentes fuente
└── Plaka_argazkiak/    # Imágenes de ejemplo de placas
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

**Parámetros:**

| Parámetro | Descripción |
|-----------|-------------|
| `--minelement` | Número mínimo de elementos por imagen. |
| `--maxelement` | Número máximo de elementos por imagen. |
| `--min_factor` | Factor de escala mínimo para los componentes. |
| `--max_factor` | Factor de escala máximo para los componentes. |
| `--min_angle` | Ángulo de rotación mínimo (grados). |
| `--max_angle` | Ángulo de rotación máximo (grados). |
| `--dataset_dir` | Directorio de salida del dataset generado. |

---

## Salida generada

El script crea la carpeta `directorio_salida` con la siguiente estructura:

```
directorio_salida/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

- **Imágenes** sintéticas con componentes colocados aleatoriamente.
- **Etiquetas** en formato YOLO (un `.txt` por imagen con coordenadas normalizadas).
- **data_preview**: imagen de vista previa con 16 imágenes y sus bounding boxes dibujados.

---

## Flujo de trabajo típico

1. Colocar imágenes de componentes en la carpeta `input/`.
2. Ejecutar `yodaut.py` con los parámetros deseados.
3. Verificar la imagen de preview `data_preview`.
4. Usar el dataset generado para entrenar un modelo YOLO.
5. Si es necesario, gestionar el dataset con [SubsetMaker](SubsetMaker).
