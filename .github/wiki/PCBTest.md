# PCBTest – Aplicación de inspección de placas PCB

*GPL-3.0-or-later / CC-BY-SA-4.0*

---

## Propósito

Inspección visual de placas PCB mediante cámara, utilizando homografía para corregir la imagen, detectando componentes con YOLO y comparándolos con una placa de referencia.

**Pipeline:**
```
Cámara → homografía → orientación → YOLO → comparación → OK / MAL
```

---

## Qué hace pcbTest

pcbTest es una herramienta para analizar el estado de una placa PCB. Una cámara captura la imagen de la placa, el programa corrige la perspectiva, detecta los componentes y los compara con una placa de referencia correcta. Al final, informa al usuario si la placa está **OK** o **MAL**.

El programa no se limita a ejecutar inferencia YOLO. Antes prepara la imagen, coloca la placa en un plano plano y trata de corregir su orientación. Por eso es importante entender el pipeline completo.

```
Cámara
  → capturar imagen
  → detectar placa
  → aplicar homografía
  → verificar orientación mediante serigrafía
  → detectar componentes con YOLO
  → comparar con referenceBoard/
  → resultado: PLACA OK o PLACA MAL
```

> **Importante:** pcbTest está pensado para uso educativo y de prototipado. Antes de emplearlo en un entorno industrial, deben validarse adecuadamente la iluminación, la cámara, el modelo, las tolerancias y los falsos positivos/negativos.

---

## Estructura del proyecto

```
pcbTest/
├── pcb_gui_inspeccion.py
├── pcb_gui_inspeccion.sh
├── pcb_realtime_pipeline.py
├── pcb_realtime_pipeline.sh
├── pcb_camera_test.py
├── pcb_camera_test.sh
├── procesar_pcb_homografia_yolo.py
├── comparar_yolo_reference.py
├── config_homografia.json
├── keypoints/
│   └── serigrafia.png
├── referenceBoard/
│   ├── notes.json
│   └── labels/
│       └── referencia.txt
├── weights/
│   └── best.pt
├── results/
│   └── .gitkeep
├── README.md
└── install_notes.md
```

**Ficheros importantes:**

| Fichero | Descripción |
|---------|-------------|
| `pcb_gui_inspeccion.py` | Interfaz gráfica principal. |
| `pcb_realtime_pipeline.py` | Pipeline completo de inspección. |
| `pcb_camera_test.py` | Script para probar la cámara rápidamente. |
| `procesar_pcb_homografia_yolo.py` | Homografía, orientación y procesado de imagen. |
| `comparar_yolo_reference.py` | Compara las detecciones YOLO con la referencia. |
| `config_homografia.json` | Define el tamaño de la imagen corregida. |
| `referenceBoard/` | Referencia geométrica y nombres de clases de la placa correcta. |
| `weights/best.pt` | Modelo YOLO. |

---

## Hardware y software requerido

- **NVIDIA Jetson Orin Nano** (hardware de destino)
- Cámara USB o compatible V4L2
- Docker con imagen `ultralytics/ultralytics:latest-jetson-jetpack6`
- Python 3, Tkinter, Pillow (para la GUI)

---

## Lanzar la GUI

```bash
cd pcbTest
./pcb_gui_inspeccion.sh
```

La GUI tiene cuatro pestañas: **Inspección**, **Rutas**, **Cámara** y **Configuración de inspección**.

---

## Pestaña Rutas

Permite verificar o seleccionar las rutas necesarias:

| Campo | Descripción |
|-------|-------------|
| **Modelo YOLO** | El modelo YOLO. Recomendado: `weights/best.pt`. |
| **Carpeta de salida** | Carpeta donde se guardarán los resultados. Habitual: `results/gui_pcb_inspection/`. |
| **referenceBoard** | Carpeta que contiene la referencia de la placa correcta. |
| **config_homografia.json** | Define el ancho y alto de la imagen corregida. |
| **Serigrafía orientación** | Imagen de serigrafía usada para determinar la orientación. |

### config_homografia.json

Este fichero define el tamaño de la imagen generada tras la homografía. Contenido mínimo:

```json
{
  "out_width": 1355,
  "out_height": 774
}
```

### Carpeta referenceBoard

```
referenceBoard/
├── notes.json          ← nombres de las clases
└── labels/
    └── referencia.txt  ← posiciones YOLO de la placa correcta
```

Debe haber **exactamente un** fichero `.txt` dentro de `labels/`.

---

## Pestaña Cámara

Permite seleccionar la fuente de cámara y hacer una prueba de captura.

**Fuentes habituales:**

```
0 · 1 · /dev/video0 · /dev/video1 · /dev/video2
```

Para listar los dispositivos de vídeo del sistema:

```bash
ls -l /dev/video*
v4l2-ctl --list-devices
```

**Botón TEST cámara:** realiza una captura instantánea y la muestra. La imagen se guarda en:

```
results/gui_pcb_inspection/camera_test/latest_camera_test.jpg
```

Si *Ancho cámara* y *Alto cámara* se dejan en `0`, OpenCV utilizará la resolución predeterminada. Si hay problemas, pruebe `1280 × 720` o `1920 × 1080`.

---

## Configuración de la inspección

| Parámetro | Descripción | Valor recomendado |
|-----------|-------------|-------------------|
| **Método** | Método de homografía. | `hough` |
| **Confianza YOLO** | Confianza mínima para aceptar una detección. | `0.49` |
| **Distancia centro** | Distancia máxima entre centros (referencia vs. detección). | `0.035` |
| **Distancia relajada** | Tolerancia más amplia para no descartar candidatos. | `0.060` |
| **EXTRA como fallo** | Si está activo, cualquier componente extra marca la placa como MAL. | desactivado |
| **Límite captura** | Número de capturas por botón. | `1` |

> Cambie **un solo parámetro a la vez** para identificar el efecto de cada ajuste.

---

## Realizar una inspección

1. Abra la GUI: `./pcb_gui_inspeccion.sh`
2. Vaya a la pestaña **Rutas** y verifique todos los ficheros.
3. Vaya a la pestaña **Cámara** y pulse **TEST cámara**.
4. Si la captura es correcta, vaya a la pestaña **Inspección**.
5. Coloque la placa bajo la cámara, completamente visible y bien iluminada.
6. Pulse **Analizar placa**.
7. Espere el resultado: **PLACA OK** o **PLACA MAL**.

**Qué ocurre internamente:**

1. Captura de cámara.
2. Detección de la placa.
3. Aplicación de homografía.
4. Verificación de orientación mediante serigrafía.
5. Inferencia YOLO.
6. Comparación con la referencia.
7. Generación de imagen, CSVs y resumen.

---

## Interpretar los resultados

| Estado | Significado |
|--------|-------------|
| **OK** | El componente de referencia se encontró y su posición es aceptable. |
| **MISSING** | Un componente esperado en la referencia no fue detectado. |
| **MISPLACED** | Se detectó un componente de la clase correcta, pero su posición no es suficientemente buena. |
| **EXTRA** | YOLO realizó una detección que no tiene equivalente en la referencia. |

**Criterio de aceptación por defecto:** `MISSING = 0` y `MISPLACED = 0`.

**Carpeta de resultados:**

```
results/gui_pcb_inspection/
├── raw/latest_raw.jpg
├── corrected/latest_corrected.jpg
├── overlay/latest_result.jpg
├── overlay_failures/latest_failures.jpg
├── components/latest_components.csv
├── comparison/latest_comparison.csv
├── camera_test/latest_camera_test.jpg
├── debug/
└── summary_realtime.csv
```

---

## Ajustes recomendados

| Problema | Acción |
|----------|--------|
| Demasiados falsos positivos | Aumentar confianza YOLO: `0.49 → 0.55 → 0.60` |
| Componentes correctos aparecen como MISPLACED | Aumentar distancia centro: `0.035 → 0.045 → 0.060` |
| Componentes reales aparecen como MISSING | Disminuir confianza YOLO; revisar iluminación y enfoque |
| Homografía incorrecta | Asegurar que la placa completa es visible; evitar reflejos; revisar `debug/homography/` |
| Orientación incorrecta | Verificar `keypoints/serigrafia.png`; revisar `debug/orientation/` |

---

## Problemas frecuentes

**Error: no se puede abrir la cámara**

```bash
ls -l /dev/video*
v4l2-ctl --list-devices
sudo usermod -aG video $USER
```

**Docker da un error de permisos**

```bash
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar
```

**Los ficheros se crean como root**

```bash
sudo chown -R $USER:$USER results .ultralytics .config .cache
```

**Mensaje `no_valid_candidate_same_class`**

Significa que se encontraron detecciones de la misma clase pero ningún candidato válido para emparejar. Normalmente está relacionado con la distancia de centro, el solapamiento, el tamaño o la homografía.

---

*Resumen: primero pruebe la cámara, luego revise las imágenes de depuración de homografía y orientación, y por último ajuste gradualmente los parámetros de YOLO y comparación.*
