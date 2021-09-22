# average_face_yunako
making average faces which are image files or gif  

I programming by being referenced below two git hubs.
  - making average face : https://github.com/stekhn/average-faces-opencv
     * This code made by python2. So I change the code. 
  - making a gif : https://github.com/johnwmillr/Facer/blob/master/facer/facer.py
     * I referenced this code because I wanna make a gif file.

Before using my code, you have to install libraries like cmake, numpy, opencv-python, requests, scikit-image, unidecode, dlib, etc..
To find landmarks, you have to download ".dat" file. 
   - url: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2﻿


## Method(cmd)
1. Find a face landmarks and Make 68 landmarks files(.txt).
> python extract.py shape_predictor_68_face_landmarks.dat {images folder path}
2. Make an average face (an image and gif file)
> python average_gif.py {images and landmarks text files folder path}



## If you have any questions, please contact my mail.

**yunako's email**: [![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:koyuna2837@gmail.com)](mailto:koyuna2837@gmail.com)
