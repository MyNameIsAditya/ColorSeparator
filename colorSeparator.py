#import cv2
#import numpy as np

pictureType = input("Choose an image: \n 1) Penguin \n 2) Giraffe \n 3) Peacock \n")
print(pictureType)

if ((pictureType.lower() == "penguin") or (pictureType == "1") or (pictureType == "1)")):
    print("Type 1 Success")
elif ((pictureType.lower() == "giraffe") or (pictureType == "2") or (pictureType == "2)")):
    print("Type 2 Success")
elif ((pictureType.lower() == "peacock") or (pictureType == "3") or (pictureType == "3)")):
    print("Type 3 Success")
else:
    pictureType = input("Input not recognized. Please try again. \n Choose an image: \n 1) Penguin \n 2) Giraffe \n 3) Peacock \n")
