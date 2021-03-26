# Move Detector
## Description:
Project is build in Python using OpenCv technology.
The aim of this project is to detect movement in video clips and streams, 
including youtube and webcams.
The app provides information about movement
in the form of red inscription in left up corner and green square in movement area.
### Quick about the detector:
In first stage the image (one of the frame in video) is turned into grey scale.

Then we use the BackgroundSubtractor (from Open Cv) to see the differences between previous frames.
It's just subtract pixels value from two frames.

In final stage we filter image from a buzz (using Open cv's bluer threshold).

Final decision whether movement is detected
depends on how much of area in the picture is being considered as moving.
## Features:
## Video from local file
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/file.png?raw=true)
## Webcam
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/camera.png?raw=true)
## Stream from IP camera
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/ip_camera.png?raw=true)
## Video or livestream from YouTube
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/yt.png?raw=true)

## Technologies:
Python + OpenCv + PyQt5
### Project realised for Multimedia course AGH 2021
### Authors: Joanna Tokarska, Alicja Niewiadomska, Maciej Czyjt, Krzysztof Niedziela
