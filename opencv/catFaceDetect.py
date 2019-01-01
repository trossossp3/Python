import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('Z:\Dev\Anaconda\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\haarcascades\haarcascade_frontalcatface.xml')
#eye_cascade = cv.CascadeClassifier('Z:\Dev\Anaconda\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\haarcascades\haarcascade_eye.xml')
img = cv.imread('cat.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#russian plates work best
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0, 100, 0),5)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    #for (ex,ey,ew,eh) in eyes:
     #   cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

