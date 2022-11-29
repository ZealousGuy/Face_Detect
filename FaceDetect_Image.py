# importing OpenCV
import cv2 as c
# loading haar data for face detection
haar_data=c.CascadeClassifier("HAAR/haarcascade_frontalface_default.xml")

# -->Reading Image for Input
img = c.imread("photos/photo-1501386761578-eac5c94b800a.jpeg")

# Detecting the face 
faces=haar_data.detectMultiScale(img)

# Drawing recctangle around Faces in image
for x,y,w,h in faces:
    c.rectangle(img,(x,y),(x+w,y+h),(255,5,5),2)

# Displaying the image in another window
c.imshow('res',img)
c.waitKey() 
