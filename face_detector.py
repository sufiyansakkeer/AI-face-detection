#importing the cv2 library that is opencv. that is a open source library for detecting tons of images
import cv2

#trained_face_data is the variable where the face detection data is stored.it is pre-trained data from the opencv library.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#random image to detection
img = cv2.imread('random_guy.jpg')



'''we need to convert the image to black and white, then only it can detect easily 
    so we use cvtColor function to convert the "img " to "COLOR_BGRf2GRAY" (that is black and white) '''
converted_grey_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#imshow is used to display the detection in our image file in the name of the face detection
cv2.imshow('face detection',converted_grey_img)

#this waitKey will help us to wait until we press any key to continue,without this function the image will show only milliseconds
cv2.waitKey()

print("code completed")