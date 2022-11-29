# importing OpenCV
import cv2 as c

# loading haar data for face detection
haar_data=c.CascadeClassifier("HAAR/haarcascade_frontalface_default.xml")

# Video Source(0=Default Cam,1=Set up cam software, direct video path works too)
vid = c.VideoCapture(0)
while True:
    flag,frame=vid.read()
    if flag:
        # Detecting the face 
        faces=haar_data.detectMultiScale(frame)

        # Drawing rectangle around Faces in frame
        for x,y,h,w in faces:
            c.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
        c.imshow('res',frame)

        #IMP-- Click Esc to Close the Window
        if c.waitKey(1)==27:
            break
# Releasing the Cam Access
vid.release()
c.destroyAllWindows()