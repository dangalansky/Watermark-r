# Watermark'R
 version 2.0
 
This is an updated version adding the use of the OpenCV library. The aim of this upgrade is to allow the upload of watermarks with pre-existing backgrounds and have them converted into transparencies within the program. 
 
## Usage, Photo Upload:
Watermark should be a pre-existing photo, ideally 3 or less colors and in the .png format though .jpg should also work. Positioning of the watermark in this upgrade is more complicated to customize for the user than v1.0 thus, I have left that version available here. I have included two options in the GUI: upper left corner and bottom right corner. The positioning of the watermark is determined by slicing into the photo-as-array. The slice size is equal to the size of the watermark image. If the watermark photo is larger than the original, check the box to reduce size by 50%. That should correct the error you will receive. The final watermarked image will be saved into the working directory as a .png . 
 
 ## GUI
 TKinter, all design and background images created by myself. Feel free to steal or destroy at will. 
 
 
 <img width="627" alt="Screen Shot 2022-09-08 at 4 12 39 PM" src="https://user-images.githubusercontent.com/97214702/189235246-f5af4b53-cf29-41ac-841d-057759e1fa8a.png">
<br><br>
Watermark'R v1.0

A desktop application that adds a pre-existing watermark to a photo and saves as a new file under the name of your choosing. 
This was coded using the Tkinter library.
I thought it easiest to paste the watermark at position (0,0) but this can be changed. I put a comment in the code where this occurs. 
Both .jpeg and .png files are suppported but as it stands, the final file is saved as a .png file.
The file will be saved inside the Watermark'r directory. 
The GUI design was done by myself in Adobe Illustrator.
As always, feel free to steal or destroy at will. <br>
<img width="624" alt="Screen Shot 2022-06-23 at 6 29 11 PM" src="https://user-images.githubusercontent.com/97214702/178829951-be929791-eb47-45ce-9c8c-03f893b481d9.png">
