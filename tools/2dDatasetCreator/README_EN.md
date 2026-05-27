YODAUT - Yolo Data Automation

WHAT IS IT?

- YODAUT is a Python script for generating simple synthetic datasets for YOLO. Store bg.png and some other images (in PNG format, transparency is required) in the input folder and, when the script is executed, combinations of these images are generated, with the option to adjust various parameters to produce different combinations. From these combinations, image-label file pairs will be created.

MINIMUM REQUIREMENTS
- Python
 - numpy
 - opencv-python
 - matplotlib
 - pyyaml
- GIMP
  
Python: Follow the installation instructions for your system
https://www.python.org/downloads/

Once Python is installed:
pip install numpy opencv-python matplotlib pyyaml


WHAT KIND OF IMAGES ARE NEEDED?

- YODAUT is a system for easily generating synthetic PCBs. It uses PNG images, all of the same size. bg.png will be the PCB itself, and the other images will be the electronic components on the PCB.

bg.png
<img width="1355" height="934" alt="bg" src="https://github.com/user-attachments/assets/a79af8e0-7dc6-430a-930d-344ead9d0721" />

U1_OK.png
<img width="1355" height="934" alt="00004_U1_OK" src="https://github.com/user-attachments/assets/ab14ca93-b9ef-4b14-bfa8-39bc5ceaf7cc" />


Comparing the images, it is clear how the U1_OK.png integrated circuit image has transparency and, at the same time, is the same size as bg.png. Notice how it coincides with the position the U1 integrated circuit should occupy on the board. The images of all components on the circuit must be like this. The tools and techniques for preparing images can be found in the "INPUT itudiak sortzeko gida.md" file.


HOW TO USE

- Download everything: yodaut.py and the input folder.
Put everything in the same folder.

python yodaut.py --minelement 4 --maxelement 15  --min_factor 0.8 --max_factor 1.2 --min_angle -20 --max_angle 20 --min_zoom 0.9 --max zoom 1.1 --dataset_dir outputdirectory

Arguments:
- minelement: minimum number of components to be mounted on the PCB
- maxelement: maximum number of components to be mounted on the PCB
- min_factor: minimum scale factor for the components
- max_factor: maximum scale factor for the components
- min_angle: minimum rotation of the generated image
- max_angle: maximum rotation of the generated image
- min_zoom: minimum zoom of the generated image
- max_zoom: maximum zoom of the generated image
- dataset_dir: folder where the generated images and labels will be saved. Default is "datasets"




RESULTS

In the "dataset_dir" folder:
 - A dataset_preview image will be created with 16 random images.
 - images and labels folders will be created, with image-label pairs.
 - data.yaml file
 - classes.txt file
 - index.txt file
