''' In this face detection there are 3 steps:
        1. get a crap load of data of faces(opencv is used)
        2. turn these images into black and white(so the computer will detect easily)
        3. train the algorithm to detect faces
'''


#importing the cv2 library that is opencv. that is a open source library for detecting tons of images
from ast import While
import cv2

#this will import random numbers
from random import randrange

'''trained_face_data is the variable where the face detection data is stored.it is pre-trained data from the opencv library.
    "haarcascade_frontalface_default.xml" is a bunch of data that is already trained
    "CascadeClassifier" is function for detectors
    classifiers are the fancy name for the detectors'''
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#random image to detection
#img = cv2.imread('WIN_20220418_11_47_29_Pro.jpg')

#to capture from webcam, 0 means its default camera and we can also upload the video file in between '_here _' 
webcam= cv2.VideoCapture(0)

while True:
    successfully_frame_read,frame=webcam.read()
   
    '''we need to convert the image to black and white, then only it can detect easily 
    so we use cvtColor function to convert the "img " to "COLOR_BGRf2GRAY" (that is black and white) '''
    converted_grey_img= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face_rectangle=trained_face_data.detectMultiScale(converted_grey_img)
    #by using for loop we can draw n number of rectangles in the image
    for(x,y,w,h) in face_rectangle:  
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
    
    #imshow is used to display the detection in our image file in the name of the face detection
    cv2.imshow('face detection',frame)
    #this waitKey will help us to wait until we press any key to continue,without this function the image will show only milliseconds
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# to release the video captured
webcam.release()





#here the faces will detect in a rectangular manner by detectmultiscale function,it will detect in different sizes that we input. 
#face_rectangle=trained_face_data.detectMultiScale(converted_grey_img)
'''#this will print the rectangle in (x,y,w,h) format
    print(face_rectangle)'''





'''to draw the rectangle cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2), 
here x2 and y2 is x+w and y+h
(255,0,0) is the color of the rectangle
2 is the width of line in the rectangle'''
#by using for loop we can draw n number of rectangles in the image
'''for(x,y,w,h) in face_rectangle:  
 cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)'''



#imshow is used to display the detection in our image file in the name of the face detection
cv2.imshow('face detection',img)
#this waitKey will help us to wait until we press any key to continue,without this function the image will show only milliseconds
cv2.waitKey()

print("code completed")