# GUÍA PARA CREAR IMÁGENES DE INPUT

## REQUISITOS
- GIMP

## DESCRIPCIÓN
- En GIMP se crea una imagen con múltiples capas. Después, el script `2dDatasetCreator` combina algunas de esas capas para generar pares imagen-etiqueta con distintas configuraciones del circuito.

## CÓMO CREAR UNA IMAGEN MULTICAPA (EJEMPLO CON ARDUINO)
### CREAR Y REDIMENSIONAR LA IMAGEN

Abre en GIMP la imagen de la placa sin componentes:  
- Archivo -> Abrir -> Seleccionar imagen

En este ejemplo se usa una placa Arduino Uno R3. Sus dimensiones son 68.6 x 53.3 mm. El tamaño de la PCB se usará como referencia para el tamaño del lienzo en GIMP. Como base inicial se usará 686x533 px. Con el siguiente procedimiento, la imagen y el lienzo quedarán del mismo tamaño.  
- **Imagen -> Tamaño del lienzo**  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5ed513f5-0529-4473-a957-4b7bb3227141" />

  - Introduce los tamaños  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/043ef1fb-673c-4818-a81c-a7796f4a9cd9" />  

  - La imagen no encaja correctamente, así que hay que aumentar el lienzo proporcionalmente. Para ello, la cadena de proporción debe estar cerrada.  
    <img width="608" height="601" alt="image" src="https://github.com/user-attachments/assets/f61fdcf5-a5d1-4d58-a33b-6a1e8a2c3af8" />  

  - Duplica uno de los tamaños y el otro se duplicará también.
	<img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/da0c20aa-5fd7-4dd3-93ee-f8ba67e6954d" />

  - Pulsa **Redimensionar**.  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/a271a25d-f138-4206-b36d-41ab9e23ab6c" />  

- Añade transparencia a la imagen. **Capa -> Transparencia -> Añadir canal alfa**  
    <img width="280" height="274" alt="image" src="https://github.com/user-attachments/assets/0922de16-02c0-462f-b27b-96e0b7c8eb32" />  

- Selecciona **Selección difusa**  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/11200745-cdb1-4a65-8877-d7a730c041bd" />  

- Selecciona el contorno de la imagen y, pulsando Supr, elimínalo. Después: **Editar -> Seleccionar nada**
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d2402c44-7e40-4092-b01d-4b63470dedd4" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/381ae4c5-fdcd-456e-889f-435c9ec7b9f5" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/237854c5-c623-4fc4-8cdc-3ed7ec080af4" />  

- Selecciona **Transformación unificada** y manipula los tiradores de las esquinas hasta que la placa cubra todo el lienzo. Pulsa Intro.
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/73457278-1d0a-41db-b9cb-59766959ea2c" />  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8724237a-34d7-416a-9198-00356275c3bb" />  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/db2ef7da-49a7-4c91-a6f5-753fc82f4a6a" />

- De este modo la PCB ocupará toda la imagen, pero la capa puede quedar fuera de los límites. Selecciona **Capa -> Capa a tamaño de imagen** para ajustar la capa al tamaño de la imagen.

### CARGAR Y REDIMENSIONAR LA PCB CON COMPONENTES

Para cargar la placa con componentes: Archivo -> **Abrir como capas** -> Seleccionar imagen con componentes. Después, realiza los pasos necesarios del procedimiento anterior hasta redimensionar completamente esta imagen también.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c692fb20-1988-4e41-afbb-6881d4c648a2" />  

### CREAR NUEVAS CAPAS DE IMAGEN CON COMPONENTES

- Para ello, primero debes tener abierta la ventana **Capas**. Normalmente está abierta en GIMP, pero si no aparece, sigue: Ventanas -> Diálogos acoplables -> Capas.  
  <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8022da7c-271d-4719-95b6-391708de32fe" />

- Hecho esto, a la derecha deberías ver las miniaturas de las dos imágenes cargadas. Una capa será la imagen sin componentes y la otra la que tiene componentes. La capa con componentes debe estar arriba; si no, súbela arrastrándola con el ratón. Las capas superiores se ven y las inferiores quedan tapadas. Selecciona la herramienta **Selección rectangular** (arriba a la izquierda).
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/ad230274-3b0c-4b70-b320-6c1131b67329" />

- Usando el ratón, selecciona un componente y crea una caja de selección a su alrededor.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/0a19bcbb-9d74-4401-ad9c-86f18d2fbbf9" />

- Ejecuta **Editar -> Copiar** (Ctrl+C).
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5145f793-2ec5-4c13-8aa7-91e2203b6f66" />

- Ejecuta **Editar -> Pegar como -> Pegar como capa única en su lugar**. Aunque parezca que no cambió nada, habrá aparecido una nueva capa llamada `Copia de XXXXX`. Pulsando en el icono del ojo a la izquierda del nombre de la capa, las capas se vuelven invisibles, lo cual es muy útil en este proceso. Haz invisibles la PCB con componentes y la PCB sin componentes pulsando en sus ojos.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f43f48b1-bbc6-4420-9aab-20fe003f2108" />

- Selecciona **Capa -> Capa a tamaño de imagen**. Esto expandirá la capa recién creada al tamaño completo de la imagen. Para trabajar correctamente, selecciona también **Seleccionar -> Nada**.

- Hay que limpiar la imagen. Para ello, la herramienta más cómoda es la **Herramienta de selección libre** (lazo).
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/baa5a1c7-1ce7-4c41-bf8f-3ce096ddd8b3" />

- Haz clic varias veces para definir y cerrar un área. Asegúrate de tener seleccionada la capa `Copia de XXXXXX`. Pulsa **Supr** para borrar la selección. Repite hasta limpiar la imagen.
<img width="496" height="728" alt="image" src="https://github.com/user-attachments/assets/3cc0ebee-fbb8-4462-bd67-e6b88e0d7dd4" />
<img width="1133" height="497" alt="image" src="https://github.com/user-attachments/assets/56875b3d-4f1e-4823-b46a-d8c82def3603" />

- Colócate sobre la capa de imagen, haz doble clic con el ratón (o pulsa F2) y asigna el nombre del componente. En este ejemplo se usará `U1`.
<img width="1327" height="550" alt="image" src="https://github.com/user-attachments/assets/cfe4315f-f2e7-463e-9ceb-a2f2b3dc261d" />

- Haz lo mismo con otras capas, nombrándolas **bg** y **COMPONENTES**.
<img width="1221" height="615" alt="image" src="https://github.com/user-attachments/assets/956c7ec3-6c9a-4ca2-8798-51c889397126" />

- Repite con todos los componentes. Según la complejidad de la placa, tardará más o menos.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/286b995f-6a1a-4d80-b8da-a3f6f3625d8c" />

### SEPARAR LAS CAPAS DE IMAGEN

- Esta parte del proceso comienza eliminando la capa `COMPONENTES`: **haz clic derecho sobre la capa COMPONENTES** y después selecciona **Eliminar capas** para borrarla.
<img width="659" height="408" alt="image" src="https://github.com/user-attachments/assets/67c5aa6a-155e-467e-b506-198a9d3fa5ed" />

- Selecciona **Archivo -> Exportar capas**. En el cuadro de texto **Nombre** escribe `[00001]_[layername]` y en el siguiente cuadro `png`. Pulsa **Exportar**. `bg.png` y todos los componentes se separarán en imágenes diferentes.
- <img width="675" height="659" alt="image" src="https://github.com/user-attachments/assets/ea02b3c6-f12c-4236-a28a-ee84dd7230d2" />

