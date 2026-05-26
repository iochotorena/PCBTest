YODAUT - Yolo Data Automation

ZER DA?

- YOLOrentzako dataset sintetiko sinpleak sortzeko Python-script bat da YODAUT. Input karpetan bg.png eta beste irudi batzu (png formatuan, transparentzia nahitaezkoa bait du) gorde eta script-a exekutatzean irudi hauen arteko konbinaketak sortzen dira, konbinaketa desberdinak sortzeko hainbat parametro doitzeko aukerarekin. Konbinaketa hauetatik irudi-label fitxategi bikoteak sortuko dira.

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


NOLAKO IRUDIAK BEHAR DIRA? 

- YODAUT PCB sintetikoak modu errazean sortzeko sistema bat da. PNG irudiak erabiltzen ditu, denak tamainu berdinekoak. bg.png PCBa bera izango da, eta beste irudiak, PCBko osagai elektronikoak.

bg.png
<img width="1355" height="934" alt="bg" src="https://github.com/user-attachments/assets/a79af8e0-7dc6-430a-930d-344ead9d0721" />

U1_OK.png
<img width="1355" height="934" alt="00004_U1_OK" src="https://github.com/user-attachments/assets/ab14ca93-b9ef-4b14-bfa8-39bc5ceaf7cc" />


Irudiak konparatuz, argi ikusten da nola U1_OK.png integratuaren irudiak gardentasuna duen, eta aldi berean, bg.png-ren tamainu bera. Ikusi nola zirkuituan U1 integratuak izan beharko lukeen posizioarekin koinziditzen duen. Zirkuituko osagai guztien irudiak modu honetakoak izan beharko dira.


NOLA ERABILI

- Deskargatu guztia, yodaut.py eta input karpeta
Jarri dena karpeta berdinean

python yodaut.py --minelement 4 --maxelement 15  --min_factor 0.8 --max_factor 1.2 --min_angle -20 --max_angle 20 --min_zoom 0.9 --max zoom 1.1 --dataset_dir directoriosalida

Argumentuak
- minelement: pcb-an montatuko den osagai kopuru minimoa
- maxelement: pcb-an montatuko den osagai kopuru maximoa
- min_factor: osagaien eskala_faktore minimoa
- max_factor: osagaien eskala_faktore maximoa
- min_angle: sortutako irudiaren errotazio minimoa
- max_angle: sortutako irudiaren errotazio maximoa
- min_zoom: sortutako irudiaren zoom minimoa
- max_zoom: sortutako irudiaren zoom maximoa
- dataset_dir: sortutako irudi eta etiketak gordeko diren karpeta. Defektuz "datasets"




EMAITZAK

"dataset_dir" karpetan:
 - dataset_preview irudi bat sortuko da ausazko 16 irudirekin.
 - images eta labels karpetak sortuko dira, irudi-label bikoteekin.
 - data.yaml fitxategia
 - classes.txt fitxategia
 - index.txt fitxategia





