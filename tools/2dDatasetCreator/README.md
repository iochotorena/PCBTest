YODAUT - Yolo Data Automation

ZER DA?
Dataset sintetiko sinpleak sortzeko Python-script bat da YODAUT. Input karpetan bg.png eta beste irudi batzu (png formatuan, transparentzia nahitaezkoa bait du) gorde eta  eta script-a exekutatzean irudi hauen arteko konbinaketak sortzen dira, konbinaketa desberdinak sortzeko hainbat parametro doitzeko aukerarekin. 

NOLAKO IRUDIAK BEHAR DIRA? 
YODAUT PCB sintetikoak modu errazean sortzeko sistema bat da. PNG irudiak erabiltzen ditu, denak tamainu berdinekoak. bg.png PCBa bera izango da, eta beste irudiak, PCBko osagai elektronikoak.

https://github.com/iochotorena/PCBTest/blob/main/tools/2dDatasetCreator/input/bg.png

GUTXIENEKO ESKAKIZUNAK
- Python
 - numpy
 - opencv-python
 - matplotlib
 - pyyaml
- GIMP
  

Python: Jarraitu zure sistemarentzako instalakuntza jarraibidieak
https://www.python.org/downloads/

Behin python instalatuta
pip install numpy opencv-python matplotlib pyyaml

NOLA ERABILI

Deskargatu guztia, yodaut.py eta input karpeta
Jarri dena karpeta berdinean

 python ydt.py --minelement 4 --maxelement 15  --min_factor 0.8 --max_factor 1.2 --min_angle -20 --max_angle 20 --dataset_dir directoriosalida


directoriosalida izeneko karpeta bat sortuko du
Bertan irudiak eta etiketak egongo dira, entrenatu eta balidatzeko (images eta labels azpikarpetetan)

'data_preview' irudia begiratu, sortutako 16 irudi daude, eta labeletako kaxak marraztu dizkio gainean 


