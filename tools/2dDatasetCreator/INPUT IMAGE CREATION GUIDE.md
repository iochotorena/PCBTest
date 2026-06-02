# INPUT IMAGE CREATION GUIDE

## REQUIREMENTS
- GIMP

## OVERVIEW
- A multi-layer image is created in GIMP. Then, the `2dDatasetCreator` script combines some of those layers to generate image-label pairs with different circuit configurations.

## HOW TO CREATE A MULTI-LAYER IMAGE (ARDUINO EXAMPLE)
### CREATE AND RESIZE THE IMAGE

Open the empty board image in GIMP:  
- File -> Open -> Choose image

In this example, an Arduino Uno R3 board is used. Its dimensions are 68.6 x 53.3 mm. The PCB size will be used as the reference for the GIMP canvas size. The initial base will be 686x533 px. With the following procedure, the image and the canvas will end up with the same size.  
- **Image -> Canvas Size**  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5ed513f5-0529-4473-a957-4b7bb3227141" />

  - Enter the dimensions  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/043ef1fb-673c-4818-a81c-a7796f4a9cd9" />  

  - The image does not fit properly, so the canvas must be increased proportionally. For this, the ratio lock must be enabled.  
    <img width="608" height="601" alt="image" src="https://github.com/user-attachments/assets/f61fdcf5-a5d1-4d58-a33b-6a1e8a2c3af8" />  

  - Double one of the dimensions and the other one will also double.
	<img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/da0c20aa-5fd7-4dd3-93ee-f8ba67e6954d" />

  - Click **Resize**.  
    <img width="608" height="595" alt="image" src="https://github.com/user-attachments/assets/a271a25d-f138-4206-b36d-41ab9e23ab6c" />  

- Add transparency to the image. **Layer -> Transparency -> Add Alpha Channel**  
    <img width="280" height="274" alt="image" src="https://github.com/user-attachments/assets/0922de16-02c0-462f-b27b-96e0b7c8eb32" />  

- Select **Fuzzy Select**  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/11200745-cdb1-4a65-8877-d7a730c041bd" />  

- Select the area around the board and press Delete. Then select **Edit -> Select None**
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d2402c44-7e40-4092-b01d-4b63470dedd4" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/381ae4c5-fdcd-456e-889f-435c9ec7b9f5" />
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/237854c5-c623-4fc4-8cdc-3ed7ec080af4" />  

- Select **Unified Transform** and adjust the corner handles until the board covers the full canvas. Press Enter.
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/73457278-1d0a-41db-b9cb-59766959ea2c" />  
    <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8724237a-34d7-416a-9198-00356275c3bb" />  
	<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/db2ef7da-49a7-4c91-a6f5-753fc82f4a6a" />

- This way the PCB will fill the whole image, but the image layer may still be outside the image boundaries. Select **Layer -> Layer to Image Size** to adjust the layer size.

### LOAD AND RESIZE THE PCB WITH COMPONENTS

To load the board with components: File -> **Open as Layers** -> Choose the image with components. Then repeat the required steps from the previous procedure until this image is also fully resized.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c692fb20-1988-4e41-afbb-6881d4c648a2" />  

### CREATE NEW IMAGE LAYERS WITH COMPONENTS

- First, make sure the **Layers** window is open. It is usually open in GIMP, but if it is not, go to: Windows -> Dockable Dialogs -> Layers.  
  <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8022da7c-271d-4719-95b6-391708de32fe" />

- After that, you should see the thumbnails of the two loaded images on the right. One layer will be the image without components and the other will contain the components. The component layer should be on top; if not, drag it upward with the mouse. Layers on top are visible, while lower ones are covered. Select the **Rectangle Select** tool (top-left area).
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/ad230274-3b0c-4b70-b320-6c1131b67329" />

- Use the mouse to select one component and create a selection box around it.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/0a19bcbb-9d74-4401-ad9c-86f18d2fbbf9" />

- Run **Edit -> Copy** (Ctrl+C).
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5145f793-2ec5-4c13-8aa7-91e2203b6f66" />

- Run **Edit -> Paste As -> Paste As Single Layer In Place**. Even if nothing seems to change, a new layer named `Copy of XXXXX` is created. By clicking the eye icon on the left side of a layer name, layers become invisible, which is very useful in this process. Make both the component PCB and non-component PCB invisible by clicking their eye icons.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f43f48b1-bbc6-4420-9aab-20fe003f2108" />

- Select **Layer -> Layer to Image Size**. This expands the newly created layer to the full image size. To continue working properly, also choose **Select -> None**.

- The image now needs cleanup. The most practical tool for this is the **Free Select Tool** (lasso).
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/baa5a1c7-1ce7-4c41-bf8f-3ce096ddd8b3" />

- Click repeatedly to define and close an area. Make sure the `Copy of XXXXXX` layer is selected. Press **Delete** to remove the selected part. Repeat until the image is clean.
<img width="496" height="728" alt="image" src="https://github.com/user-attachments/assets/3cc0ebee-fbb8-4462-bd67-e6b88e0d7dd4" />
<img width="1133" height="497" alt="image" src="https://github.com/user-attachments/assets/56875b3d-4f1e-4823-b46a-d8c82def3603" />

- Hover over the image layer, double-click it (or press F2), and set the component name. In this example, use `U1`.
<img width="1327" height="550" alt="image" src="https://github.com/user-attachments/assets/cfe4315f-f2e7-463e-9ceb-a2f2b3dc261d" />

- Do the same for other layers, naming them **bg** and **COMPONENTS**.
<img width="1221" height="615" alt="image" src="https://github.com/user-attachments/assets/956c7ec3-6c9a-4ca2-8798-51c889397126" />

- Repeat for all components. Depending on board complexity, this will take more or less time.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/286b995f-6a1a-4d80-b8da-a3f6f3625d8c" />

### SPLIT IMAGE LAYERS

- This part of the process starts by deleting the `COMPONENTS` layer: **right-click the COMPONENTS layer**, then choose **Delete Layers**.
<img width="659" height="408" alt="image" src="https://github.com/user-attachments/assets/67c5aa6a-155e-467e-b506-198a9d3fa5ed" />

- Select **File -> Export Layers**. In the **Name** text box, enter `[00001]_[layername]`, and in the next box enter `png`. Click **Export**. `bg.png` and all components will be exported as separate images.
