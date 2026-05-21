# tools/SubsetMaker

*GPL-3.0-or-later / CC-BY-SA-4.0*

![SubsetMaker screenshot](https://github.com/user-attachments/assets/96bebab4-5fe4-416b-a2c5-462bf297fa62)

---

## Descripción

Aplicación de escritorio (`subsetmaker.py`) para **gestionar datasets YOLO** con seis funcionalidades integradas:

| Funcionalidad | Descripción |
|---------------|-------------|
| **✂ Crear subconjunto** | Filtra un dataset por clases y número máximo de imágenes por clase. |
| **🔍 Verificar dataset** | Detecta etiquetas huérfanas o imágenes sin etiqueta. |
| **🔀 Dividir dataset** | Divide un split en `train` / `val` con semilla reproducible. |
| **🔢 Renumerar etiquetas** | Remapea los IDs de clase en todos los ficheros de etiquetas. |
| **📋 JSON → YAML** | Convierte anotaciones COCO JSON a formato `data.yaml` de YOLO. |
| **📄 Info YAML** | Inspecciona cualquier fichero `data.yaml`. |

Soporta **temas oscuro y claro** y recuerda la preferencia entre sesiones.

---

## Requisitos

- Python 3.10+
- `Pillow` >= 9.0
- `tkinter` (incluido con la mayoría de distribuciones Python)

```bash
pip install -r requirements.txt
# Solo en Linux, si falta tkinter:
sudo apt-get install python3-tk
```

---

## Uso

```bash
python subsetmaker.py
```

---

## Estructura de dataset soportada

```
dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml        # opcional (usado para nombres de clases)
```

También soporta layouts planos (imágenes y etiquetas directamente bajo `images/` y `labels/`).

**Formatos de imagen soportados:** `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.tif`, `.webp`

---

## Formato de etiquetas YOLO

```
<class_id> <x_center> <y_center> <width> <height>
```

Todas las coordenadas están normalizadas al rango `[0, 1]`. SubsetMaker solo modifica el campo `<class_id>`, nunca las coordenadas del bounding box.

---

## ✂ Crear subconjunto

Copia un subconjunto filtrado y (opcionalmente) reequilibrado a una nueva carpeta de salida.

**Flujo de trabajo:**

1. **Carpeta del dataset** — seleccionar la raíz del dataset YOLO.
2. **Carpeta de salida** — elegir dónde se escribirá el subconjunto.
3. **Split** — elegir `train`, `val`, `test` o dejar en blanco para layouts planos.
4. **Cargar dataset** — la app escanea las etiquetas y lista cada clase con su número de imágenes.
5. **Panel de clases** — marcar/desmarcar las clases a conservar.
6. **Máximo de imágenes por clase** — límite superior de imágenes por clase.
7. **Semilla aleatoria** — semilla para muestreo reproducible.
8. **Reasignar IDs de clase** — si está marcado, renumera los IDs de clase desde 0.
9. **Crear subconjunto** — copia imágenes y etiquetas filtradas a la carpeta de salida.

**Algoritmo:**

1. Escanea imágenes y mapea `class_id` a las imágenes que lo contienen.
2. Para cada clase seleccionada, mezcla y toma las primeras `max_per_class` imágenes.
3. Une todas las imágenes seleccionadas (sin duplicados).
4. Filtra las etiquetas: solo escribe las líneas de clases conservadas.
5. Si el remapeo está activo, renumera los IDs consecutivamente desde 0.
6. Copia imágenes y genera nuevo `data.yaml`.

---

## 🔍 Verificar dataset

Escanea un split en busca de problemas de integridad.

**Flujo de trabajo:**

1. Seleccionar carpeta del dataset y split a verificar.
2. **Verificar dataset** — lista:
   - **Etiquetas faltantes** — imágenes sin fichero `.txt` correspondiente.
   - **Etiquetas huérfanas** — ficheros `.txt` sin imagen correspondiente.
3. Botones de corrección:
   - **Crear etiquetas vacías** — crea `.txt` vacíos para imágenes sin etiquetar (negatives/background).
   - **Eliminar etiquetas huérfanas** — borra ficheros `.txt` sin imagen.

---

## 🔀 Dividir dataset

Divide aleatoriamente un split en subconjuntos `train` y `val`.

**Flujo de trabajo:**

1. Seleccionar carpeta del dataset, carpeta de salida y split fuente.
2. **Train %** — porcentaje de imágenes para entrenamiento.
3. **Semilla aleatoria** — para reproducibilidad.
4. **Dividir dataset** — copia imágenes y etiquetas a `train/` y `val/`.

---

## 🔢 Renumerar etiquetas

Aplica una reasignación personalizada de IDs de clase a todos los ficheros de etiquetas.

**Flujo de trabajo:**

1. Seleccionar carpeta de etiquetas y carpeta de salida (misma carpeta = modo in-place).
2. **Mapeo** — una regla por línea: `id_antiguo -> id_nuevo` (ej. `2 -> 0`).
3. **Renumerar etiquetas** — reescribe solo los ficheros que cambian (modo in-place).

---

## 📋 JSON → YAML

Convierte un fichero JSON a `data.yaml` compatible con YOLO.

**Formatos JSON soportados:**

| Formato | Ejemplo |
|---------|---------|
| Anotaciones COCO | `{"categories": [{"id": 1, "name": "cat"}, ...]}` |
| Lista de nombres | `["cat", "dog", "bird"]` |
| Objeto de nombres | `{"names": ["cat", "dog"]}` |

**Flujo de trabajo:**

1. Seleccionar fichero JSON.
2. **Cargar JSON** — muestra el mapeo de clases.
3. Editar ruta de salida YAML si es necesario.
4. **Guardar YAML** — genera `data.yaml` con los nombres de clases.

---

## 📄 Info YAML

1. Seleccionar fichero `data.yaml`.
2. **Cargar YAML** — muestra `nc` (número de clases) y `names` (lista de clases).

---

## Ejecutar tests

```bash
pip install pytest
pytest test_subsetmaker.py -v
```
