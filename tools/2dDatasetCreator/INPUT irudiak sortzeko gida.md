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
- **Imagen-> Tamaño del Lienzo**  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5ed513f5-0529-4473-a957-4b7bb3227141" />
  
  - Sartu tamainuak  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/043ef1fb-673c-4818-a81c-a7796f4a9cd9" />  
  
  - Irudia ez da ondo sartzen, beraz, lientzoa proportzionalki handitu beharko da. Horretarako proportzio-katea itxia behar da.  
    <img width="608" height="601" alt="image" src="https://github.com/user-attachments/assets/f61fdcf5-a5d1-4d58-a33b-6a1e8a2c3af8" />  
  
  - Tamainuetako bat bikoiztu eta bestea ere bikoiztuko da.
	<img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/da0c20aa-5fd7-4dd3-93ee-f8ba67e6954d" />
  
  - **Redimensionar** sakatu.  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/a271a25d-f138-4206-b36d-41ab9e23ab6c" />  
		
- Transparentzia gehitu irudiari. **Capa-> Transparencia-> Añadir Canal Alfa**  
    <img width="280" height="274" alt="image" src="https://github.com/user-attachments/assets/0922de16-02c0-462f-b27b-96e0b7c8eb32" />  
  
- Aukeratu **Seleccion Difusa**  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/11200745-cdb1-4a65-8877-d7a730c041bd" />  
  
- Aukeratu irudiaren ingurunea eta Supr sakatuta ezabatu. Ondoren **Editar-> Seleccionar nada**
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d2402c44-7e40-4092-b01d-4b63470dedd4" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/381ae4c5-fdcd-456e-889f-435c9ec7b9f5" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/237854c5-c623-4fc4-8cdc-3ed7ec080af4" />  
  
- **Transformacion unificada** aukeratu eta erpinetako tiradoreak manipulatu plakak lienzo osoa tapatu arte. Intro sakatu.
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/73457278-1d0a-41db-b9cb-59766959ea2c" />  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8724237a-34d7-416a-9198-00356275c3bb" />  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/db2ef7da-49a7-4c91-a6f5-753fc82f4a6a" />

- Modu honetan PCBak irudi osoa okupatuko du, baino irudi-geruza agian iruditik kanpora egon daiteke. **Capa-> Capa a tamaño de imagen** aukeratu irudi geruza irudiaren tamainu murrizteko.

### OSAGAIDUN PCBa KARGATU ETA BERDIMENTSIONATU

Osagaidun plaka kargatzeko: Archivo-> **Abrir como capas**-> Osagaidun irudia aukeratu. Ondoren aurreko prozedurako behar diren pausuak eman irudi hau ere guztiz berdimentsionatu arte.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c692fb20-1988-4e41-afbb-6881d4c648a2" />  

### OSAGAIEKIN IRUDI-GERUZA BERRIAK SORTU

- Hau egiteko lehenik eta behin **Capas** lehioa irekita behar da. Orokorrean Gimp-en irekita egon ohi da, baino ez badago, ondorengoa jarraitu behar da: Ventanas-> Dialogos acoplables-> Capas.  
  <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8022da7c-271d-4719-95b6-391708de32fe" />
  
- Hau eginda eskubi aldean ikusi beharko litzateke kargatu diren bi irudien minuaturekin. Bat osagai gabeko irudi-geruza izango da, eta bestea berriz, osagaiduna. Osagaidunak egon beharko luke lehenengo, ala ez bada, saguarekin sakatu eta eramanez gora mugitu daiteke. Gainean dauden geruza irudian ikusiko dira, eta azpian daudenak berriz, tapatuak izango dira. Aukeratu **Seleccion Rectangular** tresna(goran ezkerretan)
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/ad230274-3b0c-4b70-b320-6c1131b67329" />
  
- Sagua erabiliz osagai bat aukeratuko ondoren bere inguruan selekzio-kaxa bat sortu beharko da.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/0a19bcbb-9d74-4401-ad9c-86f18d2fbbf9" />
  
- **Editar-> Copiar** (Ctrl+C) egin.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5145f793-2ec5-4c13-8aa7-91e2203b6f66" />
  
- **Editar-> Pegar como-> Pegar como capa unica en su lugar** egin. Ezer ez dela aldatu ditudien arren, irudi geruza berri bat agertu da, Copia de XXXXX izenekoa. Irudi geruzaren izenaren ezkerraldean dagoen begietan sakatuz, irudi geruzak garden bilakatzen dira, oso erabilgarria prozesu honetan. Osagaidun PCB eta osagai gabea ikustezin bihurtu beraien begietan sakatuz.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f43f48b1-bbc6-4420-9aab-20fe003f2108" />
  
- **Capa-> Capa a tamaño de imagen** aukeratu. Honek sortu berri den irudi-geruza irudiaren tamainura zabalduko du. Eta ondo lan egiteko, **Seleccionar-> nada** aukeratu.
  
- Irudia garbitu egin behar da. Horretarako tresnarik erosoena **Herramienta de seleccion libre** (lazoa) da.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/baa5a1c7-1ce7-4c41-bf8f-3ce096ddd8b3" />
  
-  Behin eta berriz saguan klik eginda eremu bat definitu eta itxi. Kontutan eduki Copia de XXXXXX irudi geruza aukeratuta edukitzeaz. **Supr** sakatu aukeratutako ezabatzeko. Errepikatu irudia garbitu arte.
<img width="496" height="728" alt="image" src="https://github.com/user-attachments/assets/3cc0ebee-fbb8-4462-bd67-e6b88e0d7dd4" />
<img width="1133" height="497" alt="image" src="https://github.com/user-attachments/assets/56875b3d-4f1e-4823-b46a-d8c82def3603" />
  
- Irudi-geruzaren gainean jarri, bi klik egin saguarekin (edo F2 sakatu) eta osagaiaren izena jarri. Adibide hoentan U1 jarriko da.
<img width="1327" height="550" alt="image" src="https://github.com/user-attachments/assets/cfe4315f-f2e7-463e-9ceb-a2f2b3dc261d" />
  
- Egin berdina beste geruzekin **bg** eta **OSAGAIAK** deituz.
<img width="1221" height="615" alt="image" src="https://github.com/user-attachments/assets/956c7ec3-6c9a-4ca2-8798-51c889397126" />
  
- Errepikatu osagai guztiekin. Plakaren konplexutasunaren arabera denbora gehiago edo gutxiago kostatuko da.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/286b995f-6a1a-4d80-b8da-a3f6f3625d8c" />


### IRUDI-GERUZAK BANATU

- Prozesuaren zati hau OSAGAIAK geruza ezabatuz hasiko da: **egin klik saguaren eskubiko botoarekin OSAGAIAK irudi-geruzan**, eta ondoren, **Eliminar Capas** aukeratu OSAGAIAK geruza ezabatzeko.
<img width="659" height="408" alt="image" src="https://github.com/user-attachments/assets/67c5aa6a-155e-467e-b506-198a9d3fa5ed" />
  
- **Archivo-> Exportar Capas** aukeratu. **Nombre** textu-kaxan [00001]_[layername] idatzi eta hurrengo kaxan png. **Exportar** sakatu. bg.png eta osagai guztiak irudi besberdinetan banatuko dira.

- 


 






  










	  
    
    




 



	

  


