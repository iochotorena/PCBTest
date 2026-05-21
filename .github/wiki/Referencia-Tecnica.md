# Referencia técnica

*GPL-3.0-or-later / CC-BY-SA-4.0*

---

## Pipeline de inspección

```
Cámara
  → capturar imagen
  → detectar placa (contorno)
  → aplicar homografía
  → verificar orientación (template matching con serigrafia.png)
  → inferencia YOLO (detectar componentes)
  → comparar con referenceBoard/
  → resultado: PLACA OK / PLACA MAL
```

---

## Scripts principales

### `pcb_gui_inspeccion.py` / `.sh`

Interfaz gráfica principal (Tkinter). Coordina todos los demás scripts.

### `pcb_realtime_pipeline.py` / `.sh`

Ejecuta el pipeline completo de inspección sin GUI. Útil para integración en líneas de producción o pruebas por terminal.

**Parámetros:**

| Parámetro | Descripción |
|-----------|-------------|
| `--camera-source` | Fuente de cámara (`0`, `1`, `/dev/video0`, ...) |
| `--output-dir` | Directorio de resultados |
| `--reference-dir` | Carpeta `referenceBoard/` |
| `--config` | Fichero `config_homografia.json` |
| `--orientation-template` | Imagen de serigrafía |
| `--component-model` | Modelo YOLO (`weights/best.pt` o `.engine`) |
| `--limit` | Número de capturas (0 = continuo) |
| `--interval` | Intervalo entre capturas en segundos (0 = manual) |
| `--homography-method` | Método de homografía (`hough`) |
| `--conf` | Confianza YOLO mínima |
| `--max-center-distance` | Distancia máxima entre centros |
| `--max-center-distance-relaxed` | Distancia máxima relajada |

### `pcb_camera_test.py` / `.sh`

Realiza una captura de prueba y la guarda. No ejecuta el pipeline de inspección.

### `procesar_pcb_homografia_yolo.py`

Contiene las funciones de:
- Detección del contorno de la placa.
- Aplicación de homografía.
- Verificación de orientación mediante template matching.
- Ejecución de inferencia YOLO.

### `comparar_yolo_reference.py`

Compara las detecciones YOLO con los componentes de la referencia y clasifica cada uno como OK, MISSING, MISPLACED o EXTRA.

---

## Ficheros de configuración

### `config_homografia.json`

```json
{
  "out_width": 1355,
  "out_height": 774
}
```

Define el tamaño en píxeles de la imagen generada tras la homografía. Las coordenadas de `referenceBoard/labels/referencia.txt` deben corresponder a estas dimensiones.

### `referenceBoard/notes.json`

Contiene los nombres de las clases YOLO:

```json
{
  "names": ["componente_A", "componente_B", "..."]
}
```

### `referenceBoard/labels/referencia.txt`

Etiquetas YOLO de la placa de referencia correcta. Formato estándar YOLO:

```
<class_id> <x_center> <y_center> <width> <height>
```

Coordenadas normalizadas al rango `[0, 1]` respecto a las dimensiones de `config_homografia.json`.

### `keypoints/serigrafia.png`

Imagen de la zona de serigrafía de la placa. Se usa como template para detectar la orientación mediante template matching.

---

## Parámetros de comparación

| Parámetro | Descripción | Rango típico |
|-----------|-------------|--------------|
| `conf` | Confianza YOLO mínima | `0.3 – 0.8` |
| `max-center-distance` | Distancia máxima (normalizada) entre centro de referencia y detección | `0.02 – 0.08` |
| `max-center-distance-relaxed` | Tolerancia ampliada para casos límite | `0.05 – 0.12` |

---

## Criterios de clasificación

| Estado | Condición |
|--------|-----------|
| **OK** | Se encontró un candidato de la clase correcta dentro de la distancia máxima. |
| **MISSING** | No se encontró ningún candidato válido de la clase esperada. |
| **MISPLACED** | Se encontró un candidato de la clase correcta, pero fuera de la distancia máxima. |
| **EXTRA** | Detección YOLO sin componente equivalente en la referencia. |

---

## Estructura de resultados

```
results/gui_pcb_inspection/
├── raw/                    # Imágenes crudas de la cámara
│   └── latest_raw.jpg
├── corrected/              # Imágenes tras homografía
│   └── latest_corrected.jpg
├── overlay/                # Overlay con todas las detecciones
│   └── latest_result.jpg
├── overlay_failures/       # Overlay solo con los fallos
│   └── latest_failures.jpg
├── components/             # CSV con todas las detecciones YOLO
│   └── latest_components.csv
├── comparison/             # CSV con la comparación referencia vs. detecciones
│   └── latest_comparison.csv
├── camera_test/            # Imágenes del test de cámara
│   └── latest_camera_test.jpg
├── debug/                  # Imágenes de depuración
│   ├── homography/
│   └── orientation/
└── summary_realtime.csv    # Resumen global de inspecciones
```

---

## Docker

Los scripts `.sh` ejecutan el pipeline dentro de un contenedor Docker:

```bash
DOCKER_IMAGE="ultralytics/ultralytics:latest-jetson-jetpack6"
```

El contenedor recibe:
- Todos los dispositivos `/dev/video*` del host.
- El directorio del proyecto montado como volumen.
- El usuario del host (`--user $(id -u):$(id -g)`) para evitar ficheros creados como root.

---

## Glosario

| Término | Significado |
|---------|-------------|
| Homografía | Transformación proyectiva que rectifica la perspectiva de la imagen de la placa. |
| Serigrafía | Zona de texto o símbolo impreso en la placa, usada como referencia de orientación. |
| referenceBoard | Conjunto de etiquetas YOLO y metadatos de una placa correcta de referencia. |
| YOLO | You Only Look Once. Modelo de detección de objetos en tiempo real. |
| Template matching | Búsqueda de una imagen patrón (serigrafía) dentro de otra imagen para determinar orientación. |
| JetPack | SDK de NVIDIA para Jetson que incluye el sistema operativo, drivers, CUDA y herramientas de IA. |
| TensorRT | Motor de inferencia de NVIDIA que optimiza modelos para ejecución acelerada en GPU. |
