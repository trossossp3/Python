import cv2

img = cv2.imread('testText.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
newImg = cv2.equalizeHist(gray)
cv2.imwrite('newtestText.jpg', newImg)
cv2.imshow('img',newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
