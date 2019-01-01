import cv2 as cv

img = cv.imread('plate1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imwrite('newtextTest.jpg', img)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()