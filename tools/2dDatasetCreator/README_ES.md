### YODAUT - Yolo Data Automation

> 🌐 Otros idiomas: [Euskera](README.md) | [English](README_EN.md)

### ¿QUÉ ES?
- YODAUT es un script de Python para generar datasets sintéticos simples para YOLO. Guarda `bg.png` y otras imágenes (en formato PNG, la transparencia es obligatoria) en la carpeta input y, al ejecutar el script, se generan combinaciones entre estas imágenes, con varias opciones de parámetros para crear combinaciones diferentes. A partir de estas combinaciones se crean pares de archivo imagen-etiqueta.

## REQUISITOS MÍNIMOS
- Python
  - numpy
  - opencv-python
  - matplotlib
  - pyyaml
- GIMP

Python: sigue las instrucciones de instalación para tu sistema:
https://www.python.org/downloads/

Una vez instalado Python:

pip install numpy opencv-python matplotlib pyyaml

## ¿QUÉ TIPO DE IMÁGENES HACEN FALTA?
- YODAUT es un sistema para generar PCBs sintéticos de forma sencilla. Utiliza imágenes PNG, todas del mismo tamaño. **bg.png** será la propia PCB y las demás imágenes serán los componentes electrónicos de la PCB. Por ejemplo:

bg.png
<img width="1355" height="934" alt="bg" src="https://github.com/user-attachments/assets/a79af8e0-7dc6-430a-930d-344ead9d0721" />

U1_OK.png
<img width="1355" height="934" alt="00004_U1_OK" src="https://github.com/user-attachments/assets/ab14ca93-b9ef-4b14-bfa8-39bc5ceaf7cc" />

Comparando estas imágenes, se ve claramente cómo la imagen del integrado `U1_OK.png` tiene transparencia y, al mismo tiempo, el mismo tamaño que `bg.png`. Observa cómo coincide con la posición donde debería estar el integrado U1 en el circuito. Todas las imágenes de componentes del circuito deben seguir este patrón. Las herramientas y técnicas para preparar estas imágenes se encuentran en el archivo **"INPUT itudiak sortzeko gida.md"**.

### CÓMO USARLO
- Para probar el ejemplo, descarga **yodaut.py** y la carpeta **input** desde la carpeta 2dDataset. Pon todo en la misma carpeta. En la consola de Linux, ejecuta el siguiente comando:

python yodaut.py --minelement 4 --maxelement 15  --min_factor 0.8 --max_factor 1.2 --min_angle -20 --max_angle 20 --min_zoom 0.9 --max zoom 1.1 --dataset_dir directoriosalida

# Argumentos
- minelement: número mínimo de componentes que se montarán en la PCB
- maxelement: número máximo de componentes que se montarán en la PCB
- min_factor: factor de escala mínimo de los componentes
- max_factor: factor de escala máximo de los componentes
- min_angle: rotación mínima de la imagen generada
- max_angle: rotación máxima de la imagen generada
- min_zoom: zoom mínimo de la imagen generada
- max_zoom: zoom máximo de la imagen generada
- dataset_dir: carpeta donde se guardarán las imágenes y etiquetas generadas. Por defecto `datasets`

### RESULTADOS
En la carpeta `dataset_dir`:
- Se creará una imagen `dataset_preview` con 16 imágenes aleatorias.
- Se crearán las carpetas `images` y `labels`, con pares imagen-etiqueta.
- Archivo `data.yaml`.
- Archivo `classes.txt`.
- Archivo `index.txt`.
