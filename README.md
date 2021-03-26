# Move Detector
## Description:
The aim of this project is to detect movement in video clips and streams, 
including youtube and webcams.
The app inform user about movement through the inscription in the upper left corner, 
and green square around the moving area.
### Shortly about the detector:
In first stage the image (one of the frame in video) is trimmed to the area of interest 
specified by the user, and turned into grayscale.
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/grey_roi.jpg?raw=true)
Then we use the BackgroundSubtractor (from Open Cv) to compare current frame with background 
calculated based on the previous frames (history size specified by the user).
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/mask.jpg?raw=true)
After that, Gaussian blurr and dilation is applied to smooth the noise and magnify the moving object.
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/blurred_mask.jpg?raw=true)
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/dilate_mask.jpg?raw=true)
In final stage we use threshold to cut out the noise and distinct wanted object.
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/threshold_mask.jpg?raw=true)
Final decision whether movement is detected
depends on how much of area in the picture is being considered as moving.
Thre final result.
![alt text](https://github.com/czyjtu/MoveDetection/blob/main/photos/main_window.jpg?raw=true)
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
