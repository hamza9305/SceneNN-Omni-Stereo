# Scene-Omni-Stereo

Scene-Omni-Stereo is an omni-directional dataset which was generated from the models of the SceneNN dataset and rendered by the Department, "Digital Signal Processing and Circuit Design" at Technische Universitat Chemnitz. The image pairs were generated with a virtual stereo camera placed at the ceiling at 1000 different locations with different elevation angles. The flats were split into three parts: training (34000 images), validation (5000 images) and testing (10000 images). The reference camera C_0 was always at a constant height of 2.3 m which is and the second camera C_1 was placed right of it, with a baseline of 30 cm.


<p align="center">
  <img src="Resources/Distorted_Left.png" img align="left" width="200" height="200" alt= "Distorted"> 
  <img src="Resources/Distorted_Right.png" width="200" height="200"  >
  <img src="Resources/Distorted_Disparity.png" img align="right" width="200" height="200">
</p>




## Undistortion
The original dataset was undistorted using rectifciation maps and remaped into a perspective dataset.
The python file "Undistortion.py" undistorts the dataset, which takes input as the location of the original dataset and the outputs the undistorted images to the output location. The script declares a intrinsic matrix of the fisheye dataset by finding the relevant parameters and the intrinsic matrix for a normal perspective camera. The script then generates rectification maps from the original image using camera matrix and the distortion coefficients. A remapping function is then used to undistort the fisheye image.

<p align="center">
  <img src="Resources/Undistorted_Left.png" width="200" height="200" img align="left">
  <img src="Resources/Undistorted_Right.png" width="200" height="200" hspace="30">
  <img src="Resources/Undistorted_Disparity.png" width="200" height="200" hspace="30" img align="right">
</p>

