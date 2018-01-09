import numpy as np
import cv2

cap = cv2.VideoCapture(0)
prevFrame = None

try:
    while(True):
        ret, img = cap.read()
        if (not ret):
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if prevFrame is None:
            prevFrame = gray
        frameDelta = cv2.absdiff(gray, prevFrame)
        thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=1)
        opening, contours, hierarchy = cv2.findContours(thresh, 1, 2)
        for cnt in contours:
            if cv2.contourArea(cnt) < 10000:
                continue
            cv2.drawContours(img, cnt, -1, (0,255,0), 2)
            #(x,y,w,h) = cv2.boundingRect(cnt)
            #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.imshow('video', img)
        if cv2.waitKey(33) == 27:
            break
        if cv2.waitKey(33) == 32:
            prevFrame = gray

    cap.release()
    cv2.destroyAllWindows()
except:
    pass
