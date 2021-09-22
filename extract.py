#!/usr/bin/python

# Find frontal human faces in an image and extract landmarks
# Based on the dlib example: http://dlib.net/face_landmark_detection.py.html

import sys
import os
import glob
import dlib
from skimage import io
import shutil

if len(sys.argv) != 3:
    print(
        "Missing argument. Please provide a predictor model and the path to your image folder.\n"
        "A predictor model can be downloaded from: "
        "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2\n"
        "Usage example: python extract.py shape_predictor_68_face_landmarks.dat ./images\n"
    )
    exit()

def main():
    predictor_path = sys.argv[1]
    faces_folder_path = sys.argv[2]

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    except_folder_path = faces_folder_path + '/except_folder/'

    if os.path.isdir(except_folder_path):
        pass
    else:
        os.mkdir(except_folder_path)

    for f in glob.glob(os.path.join(faces_folder_path, "*.JPG")):
        try:
            print("Processing file: {}".format(f))
            img = io.imread(f)

            # Find the bounding boxes of each face.
            dets = detector(img, 1)
            print("Number of faces detected: {}".format(len(dets)))
            if len(dets) == 0 : 
                print("얼굴인식이 안됨, len(dets): ", len(dets))
                tmp = f.split('/')

                shutil.move(faces_folder_path+'/'+tmp[-1], except_folder_path+tmp[-1])

            else:
                for k, d in enumerate(dets):
                    results = []

                    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                        k, d.left(),
                        d.top(),
                        d.right(),
                        d.bottom()
                    ))

                    # Get the landmarks/parts for the face in box d.
                    shape = predictor(img, d)
                    print("Part 0: {}, Part 1: {} ...".format(
                        shape.part(0),
                        shape.part(1)
                    ))

                    # Save each landmark as xy coordinate
                    for n in range(0, 68):
                        results.append(str(shape.part(n).x) + " " + str(shape.part(n).y))

                    with open(f + ".txt", "w") as output:
                       output.write("\n".join(results))
        except:
            print("예외발생")
            tmp = f.split('/')
            shutil.move(faces_folder_path+'/'+tmp[-1], '/Users/yunako/Documents/Bigdata_study/average-faces-opencv-master/except_folder/'+ tmp[-1])


if __name__ == '__main__' :
    main()
