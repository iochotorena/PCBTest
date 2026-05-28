# INPUT IRUDIAK SORTZEKO GIDA

## ESKAKIZUNAK
- GIMP

## AZALPENA
- GIMP-en geruza multipleko irudi bat sortzen da, ondoren bertatik 2dDatasetCreator scriptak kapa hauetako batzu konbinatuz zirkuitu konfigurazio desberdineko irudi-etiketa bikoteak sortzeko.

## NOLA SORTU GERUZA MULTIPLEKO IRUDI BAT (ARDUINO ADIBIDEA)
### IRUDIA SORTU ETA BERDIMENTSIONATU

Populatu gabeko plakaren irudia ireki GIMP-en:  
- Archivo-> Abrir-> Aukeratu irudia
  
Adibide honetan Arduino Uno R3 plaka bat erabiliko da adibide gisa. Bere dimentsioak 68.6 x 53.3mm dira. PCBaren tamainua GIMP-en lientzoaren tamainuaren erreferentzi gisa erabiliko da. Hasierako oinarri gisa 686x533px izango da. Ondorengo prozedimentuarekin irudia eta lienzoa tamainu berekoak egingo dira.  
- Imagen-> Tamaño del Lienzo  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5ed513f5-0529-4473-a957-4b7bb3227141" />
  
- Sartu tamainuak  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/043ef1fb-673c-4818-a81c-a7796f4a9cd9" />  
  
- Irudia ez da ondo sartzen, beraz, lientzoa proportzionalki handitu beharko da. Horretarako proportzio-katea itxia behar da.  
    <img width="608" height="601" alt="image" src="https://github.com/user-attachments/assets/f61fdcf5-a5d1-4d58-a33b-6a1e8a2c3af8" />  
  
- Tamainuetako bat bikoiztu eta bestea ere bikoiztuko da.
	<img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/da0c20aa-5fd7-4dd3-93ee-f8ba67e6954d" />
  
- Redimensionar sakatu.  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/a271a25d-f138-4206-b36d-41ab9e23ab6c" />  
		
- Transparentzia gehitu irudiari. Capa-> Transparencia-> Añadir Canal Alfa  
    <img width="280" height="274" alt="image" src="https://github.com/user-attachments/assets/0922de16-02c0-462f-b27b-96e0b7c8eb32" />  
  
- Aukeratu Seleccion Difusa  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/11200745-cdb1-4a65-8877-d7a730c041bd" />  
  
- Aukeratu irudiaren ingurunea eta Supr sakatuta ezabatu. Ondoren Seleccionar nada
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d2402c44-7e40-4092-b01d-4b63470dedd4" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/381ae4c5-fdcd-456e-889f-435c9ec7b9f5" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/237854c5-c623-4fc4-8cdc-3ed7ec080af4" />  
  
- Transformacion unificada aukeratu eta erpinetako tiradoreak manipulatu plakak lienzo osoa tapatu arte. Intro sakatu.
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/73457278-1d0a-41db-b9cb-59766959ea2c" />  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8724237a-34d7-416a-9198-00356275c3bb" />  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/db2ef7da-49a7-4c91-a6f5-753fc82f4a6a" />

Modu honetan PCBak irudi osoa okupatuko du.

### OSAGAIDUN PCBa KARGATU ETA BERDIMENTSIONATU

Osagaidun plaka kargatzeko: Archivo-> **ABrir como capas**-> Osagaidun irudia aukeratu  





	  
    
    




 



	

  


