# Instalación en Jetson Orin Nano

*GPL-3.0-or-later / CC-BY-SA-4.0*

Esta guía describe cómo preparar una **NVIDIA Jetson Orin Nano** para ejecutar pcbTest.

---

## Dependencias

| Componente | Uso |
|------------|-----|
| Python 3 | GUI |
| Tkinter | Interfaz gráfica |
| Pillow | Mostrar imágenes en la GUI |
| Docker | Ejecutar el pipeline de visión |
| OpenCV | Dentro del contenedor |
| Ultralytics YOLO | Dentro del contenedor |
| Cámara V4L2 | Fuente de imagen |

**Imagen Docker por defecto:**

```
ultralytics/ultralytics:latest-jetson-jetpack6
```

Si se usa otra versión de JetPack, cambie `DOCKER_IMAGE` en `pcb_realtime_pipeline.sh` y `pcb_camera_test.sh`.

---

## Paso 1 – Actualizar el sistema

```bash
sudo apt update
sudo apt upgrade -y
```

Reiniciar si el sistema lo pide.

---

## Paso 2 – Instalar dependencias del sistema

```bash
sudo apt install -y python3 python3-pip python3-tk v4l-utils
python3 --version
```

---

## Paso 3 – Instalar Pillow

```bash
python3 -m pip install pillow
python3 - <<'PY'
from PIL import Image
print("Pillow OK")
PY
```

---

## Paso 4 – Comprobar Docker

En Jetson con JetPack, Docker normalmente ya viene instalado.

```bash
docker --version
docker info
```

Si no existe:

```bash
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
```

---

## Paso 5 – Permisos de Docker

```bash
sudo usermod -aG docker $USER
sudo usermod -aG video $USER
# Cerrar sesión y volver a entrar
groups   # Debe aparecer: docker video
docker run --rm hello-world
```

---

## Paso 6 – Descargar imagen Docker de Ultralytics

```bash
docker pull ultralytics/ultralytics:latest-jetson-jetpack6

# Verificar OpenCV
docker run --rm -it ultralytics/ultralytics:latest-jetson-jetpack6 \
  python -c "import cv2; print('OpenCV OK')"

# Verificar Ultralytics
docker run --rm -it ultralytics/ultralytics:latest-jetson-jetpack6 \
  python -c "from ultralytics import YOLO; print('Ultralytics OK')"
```

---

## Paso 7 – Copiar el proyecto

```
/home/usuario/pcbTest/
├── pcb_gui_inspeccion.py
├── pcb_gui_inspeccion.sh
├── pcb_realtime_pipeline.py
├── pcb_realtime_pipeline.sh
├── pcb_camera_test.py
├── pcb_camera_test.sh
├── procesar_pcb_homografia_yolo.py
├── comparar_yolo_reference.py
├── config_homografia.json
├── keypoints/serigrafia.png
├── referenceBoard/notes.json
├── referenceBoard/labels/referencia.txt
├── weights/best.pt
└── results/.gitkeep
```

---

## Paso 8 – Dar permisos de ejecución

```bash
cd ~/pcbTest
chmod +x pcb_gui_inspeccion.py pcb_gui_inspeccion.sh
chmod +x pcb_realtime_pipeline.py pcb_realtime_pipeline.sh
chmod +x pcb_camera_test.py pcb_camera_test.sh
```

---

## Paso 9 – Verificar ficheros necesarios

```bash
ls -lh weights/best.pt
cat config_homografia.json
# Debe contener: { "out_width": 1355, "out_height": 774 }

ls -lh referenceBoard/
ls -lh referenceBoard/labels/
find referenceBoard/labels -name "*.txt"
# Debe haber exactamente un fichero .txt
```

---

## Paso 10 – Comprobar cámara

```bash
ls -l /dev/video*
v4l2-ctl --list-devices

python3 - <<'PY'
import cv2
cap = cv2.VideoCapture(0)
print("opened:", cap.isOpened())
ret, frame = cap.read()
print("ret:", ret)
if ret:
    print("shape:", frame.shape)
cap.release()
PY
```

---

## Paso 11 – Primera configuración en la GUI

```bash
cd ~/pcbTest
./pcb_gui_inspeccion.sh
```

**Pestaña Rutas:** verificar modelo, carpeta de salida, referenceBoard, config_homografia.json y serigrafía.

**Pestaña Cámara:** probar fuente `0`. Si falla, probar `1`, `2`, `/dev/video0`, etc.

**Pestaña Configuración de inspección – valores recomendados iniciales:**

| Parámetro | Valor |
|-----------|-------|
| Método | `hough` |
| Confianza YOLO | `0.49` |
| Distancia máxima centro | `0.035` |
| Distancia máxima centro relajada | `0.060` |
| Límite de capturas | `1` |
| EXTRA como fallo | desactivado |

---

## TensorRT (opcional)

Para acelerar la inferencia en Jetson:

```python
from ultralytics import YOLO
model = YOLO("weights/best.pt")
model.export(format="engine", imgsz=640)
```

El `.engine` debe generarse en la misma Jetson o en un entorno compatible.

---

## Checklist de verificación

```
[ ] Docker funciona sin sudo
[ ] Usuario en grupo docker
[ ] Usuario en grupo video
[ ] Existe /dev/video0 o similar
[ ] TEST cámara funciona
[ ] Existe weights/best.pt
[ ] Existe config_homografia.json
[ ] Existe keypoints/serigrafia.png
[ ] Existe referenceBoard/notes.json
[ ] Existe un único .txt en referenceBoard/labels/
[ ] La placa aparece completa en la captura
[ ] La homografía se ve correcta
[ ] La imagen de fallos se genera correctamente
```

---

## Solución de problemas comunes

| Problema | Solución |
|----------|----------|
| Docker pide permisos | `sudo usermod -aG docker $USER` + reiniciar sesión |
| No se puede abrir la cámara | `ls /dev/video*`; probar otras fuentes; `sudo usermod -aG video $USER` |
| Docker no ve la cámara | Comprobar que el host ve `/dev/video*` |
| Modelo no encontrado | `ls -lh weights/best.pt`; usar ruta absoluta en GUI |
| Ficheros creados como root | `sudo chown -R $USER:$USER results .ultralytics .config .cache` |
