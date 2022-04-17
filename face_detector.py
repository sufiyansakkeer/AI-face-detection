#importing the cv2 library that is opencv. that is a open source library for detecting tons of images

import cv2

#trained_face_data is the variable where the face detection data is stored.it is pre-trained data from the opencv library.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#random image to detection
img = cv2.imread('random_guy.jpg')

#imshow is used to display the detection in our image file in the name of the face detection
cv2.imshow('face detection', img)

#this waitKey will help us to wait until we press any key to continue,without this function the image will show only miliseconds
cv2.waitKey()

print("code completed")