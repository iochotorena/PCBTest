### YODAUT - Yolo Data Automation

> 🌐 Other languages: [Euskera](README.md) | [Castellano](README_ES.md)

### WHAT IS IT?
- YODAUT is a Python script for generating simple synthetic datasets for YOLO. Store `bg.png` and other images (in PNG format, transparency is required) in the input folder; when the script runs, it creates combinations of these images, with several tunable parameters to generate different combinations. From these combinations, image-label file pairs are created.

## MINIMUM REQUIREMENTS
- Python
  - numpy
  - opencv-python
  - matplotlib
  - pyyaml
- GIMP

Python: follow the installation instructions for your system:
https://www.python.org/downloads/

Once Python is installed:

pip install numpy opencv-python matplotlib pyyaml

## WHAT KIND OF IMAGES ARE NEEDED?
- YODAUT is a system to easily generate synthetic PCBs. It uses PNG images, all with the same size. **bg.png** is the PCB itself, and the other images are the PCB electronic components. For example:

bg.png
<img width="1355" height="934" alt="bg" src="https://github.com/user-attachments/assets/a79af8e0-7dc6-430a-930d-344ead9d0721" />

U1_OK.png
<img width="1355" height="934" alt="00004_U1_OK" src="https://github.com/user-attachments/assets/ab14ca93-b9ef-4b14-bfa8-39bc5ceaf7cc" />

Comparing these images, you can clearly see how the integrated-circuit image `U1_OK.png` has transparency and, at the same time, the same size as `bg.png`. Note how it matches the position where integrated circuit U1 should be on the board. All component images in the circuit must follow this same pattern. Tools and techniques for preparing these images are in the file **"INPUT itudiak sortzeko gida.md"**.

### HOW TO USE
- To try the example, download **yodaut.py** and the **input** folder from the 2dDataset folder. Put everything in the same folder. In a Linux console, run the following command:

python yodaut.py --minelement 4 --maxelement 15  --min_factor 0.8 --max_factor 1.2 --min_angle -20 --max_angle 20 --min_zoom 0.9 --max zoom 1.1 --dataset_dir directoriosalida

# Arguments
- minelement: minimum number of components to place on the PCB
- maxelement: maximum number of components to place on the PCB
- min_factor: minimum component scale factor
- max_factor: maximum component scale factor
- min_angle: minimum rotation angle of the generated image
- max_angle: maximum rotation angle of the generated image
- min_zoom: minimum zoom of the generated image
- max_zoom: maximum zoom of the generated image
- dataset_dir: folder where generated images and labels will be saved. Default: `datasets`

### RESULTS
In the `dataset_dir` folder:
- A `dataset_preview` image is created with 16 random images.
- `images` and `labels` folders are created, with image-label pairs.
- `data.yaml` file.
- `classes.txt` file.
- `index.txt` file.
