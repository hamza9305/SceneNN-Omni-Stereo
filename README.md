# Scene-Omni-Stereo

Scene-Omni-Stereo is an omni-directional dataset generated by the Department, "Digital Signal Processing and Circuit Design" at Technische Universitat Chemnitz.

<p align="center">
  <img src="Resources/Distorted_Left.png" alt="sometext" width="250" height="250" hspace="30" figcaption="Album name">
  <img src="Resources/Distorted_Right.png" width="250" height="250" hspace="30">
  <img src="Resources/Distorted_Disparity.png" width="250" height="250" hspace="30">
</p>


<figure>
    <img src='Resources/Distorted_Left.png' width="250" height="250" hspace="30" alt='missing' />
    <figcaption>Album name goes here
</figure>

# Undistortion
The original dataset was undistorted using rectifciation maps and remaped into a perspective dataset.
The python file "Undistortion.py" undistorts the dataset, which takes input as the location of where the original dataset exists and the output as the location of where the post-processing dataset should be stored 
