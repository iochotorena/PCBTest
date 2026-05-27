YODAUT - Yolo Data Automation

¿QUÉ ES?

- YODAUT es un script de Python para generar datasets sintéticos simples para YOLO. Guarda bg.png y algunas otras imágenes (en formato PNG, la transparencia es obligatoria) en la carpeta input y, al ejecutar el script, se generan combinaciones entre estas imágenes, con la posibilidad de ajustar varios parámetros para crear combinaciones diferentes. A partir de estas combinaciones se generarán pares de archivos imagen-etiqueta.

REQUISITOS MÍNIMOS
- Python
 - numpy
 - opencv-python
 - matplotlib
 - pyyaml
- GIMP
  
Python: Sigue las instrucciones de instalación para tu sistema
https://www.python.org/downloads/

Una vez instalado Python:
pip install numpy opencv-python matplotlib pyyaml


¿QUÉ TIPO DE IMÁGENES SE NECESITAN?

- YODAUT es un sistema para generar PCBs sintéticas de forma sencilla. Utiliza imágenes PNG, todas del mismo tamaño. bg.png será la propia PCB, y las demás imágenes serán los componentes electrónicos de la PCB.

bg.png
<img width="1355" height="934" alt="bg" src="https://github.com/user-attachments/assets/a79af8e0-7dc6-430a-930d-344ead9d0721" />

U1_OK.png
<img width="1355" height="934" alt="00004_U1_OK" src="https://github.com/user-attachments/assets/ab14ca93-b9ef-4b14-bfa8-39bc5ceaf7cc" />


Comparando las imágenes, se puede ver claramente cómo la imagen del circuito integrado U1_OK.png tiene transparencia y, al mismo tiempo, tiene el mismo tamaño que bg.png. Obsérvese cómo coincide con la posición que debería ocupar el integrado U1 en el circuito. Las imágenes de todos los componentes del circuito deben ser de este tipo. Las herramientas y técnicas para preparar las imágenes se encuentran en el archivo "INPUT itudiak sortzeko gida.md".


CÓMO USAR

- Descarga todo: yodaut.py y la carpeta input.
Pon todo en la misma carpeta.

python yodaut.py --minelement 4 --maxelement 15  --min_factor 0.8 --max_factor 1.2 --min_angle -20 --max_angle 20 --min_zoom 0.9 --max zoom 1.1 --dataset_dir directoriodestino

Argumentos:
- minelement: número mínimo de componentes que se montarán en la PCB
- maxelement: número máximo de componentes que se montarán en la PCB
- min_factor: factor de escala mínimo de los componentes
- max_factor: factor de escala máximo de los componentes
- min_angle: rotación mínima de la imagen generada
- max_angle: rotación máxima de la imagen generada
- min_zoom: zoom mínimo de la imagen generada
- max_zoom: zoom máximo de la imagen generada
- dataset_dir: carpeta donde se guardarán las imágenes y etiquetas generadas. Por defecto "datasets"




RESULTADOS

En la carpeta "dataset_dir":
 - Se creará una imagen dataset_preview con 16 imágenes aleatorias.
 - Se crearán las carpetas images y labels, con los pares imagen-etiqueta.
 - Archivo data.yaml
 - Archivo classes.txt
 - Archivo index.txt
