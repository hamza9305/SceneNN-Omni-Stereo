# Scene-Omni-Stereo

Scene-Omni-Stereo is an omni-directional dataset which was generated from the models of the SceneNN dataset and rendered by the Department, "Digital Signal Processing and Circuit Design" at Technische Universitat Chemnitz. The image pairs were generated with a virtual stereo camera placed at the ceiling at 1000 different locations with different elevation angles. The flats were split into three parts: training (34000 images), validation (5000 images) and testing (10000 images). The Rendering was done in Blender 2.8 with Cycles rendering engine. The reference camera C_0 was always at a constant height of 2.3 m which is and the second camera C_1 was placed right of it, with a baseline of 30 cm.

<p align="center">
  <img src="Resources/Distorted_Left.png" img align="left" width="200" height="200" title= "Distoretd" #distorted image>
  <img src="Resources/Distorted_Right.png" width="200" height="200"  >
  <img src="Resources/Distorted_Disparity.png" img align="right" width="200" height="200">
</p>

<figcaption> &emsp;&emsp;&emsp;&emsp;&emsp; Distorted Left Image
</figcaption>
<figcaption> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Distorted Right Image
</figcaption>
<figcaption> &emsp;&emsp;&emsp;&emsp;&emsp;&ensp; Distorted Disparity Image
</figcaption>


## Undistortion
The original dataset was undistorted using rectifciation maps and remaped into a perspective dataset.
The python file "Undistortion.py" undistorts the dataset, which takes input as the location of where the original dataset exists and the output as the location of where the post-processing dataset should be stored. The function calculate the focal length and camera center of every image and declares a camera matrix. It then declares new camera matrix using focal length and camera center of a perspective image. Rectification maps for each image are calculated using distortion coeffcients as that of a perspective image and then remapped.


<p align="center">
  <img src="Resources/Undistorted_Left.png" width="200" height="200" hspace="30">
  <img src="Resources/Undistorted_Right.png" width="200" height="200" hspace="30">
  <img src="Resources/Undistorted_Disparity.png" width="200" height="200" hspace="30">
</p>

<figcaption> &emsp;&emsp;&emsp;&emsp; Undistorted Left Image
</figcaption>
<figcaption> &emsp;&emsp;&emsp;&emsp;&emsp;&ensp; Undistorted Right Image
</figcaption>
<figcaption> &emsp;&emsp;&emsp;&emsp;&ensp; Undistorted Disparity Image
</figcaption>
