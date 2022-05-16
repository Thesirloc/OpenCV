import numpy as np
import cv2 as cv

img = cv.imread('opencv-logo.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("no of contours = " + str(len(contours)))
print(contours[0]) # gives array of coordinates joining which will give the boundary for one of the contours (contour[0])

cv.drawContours(img, contours, -1 , (0, 255, 0), 3)


cv.imshow('image', img)
cv.imshow('image gray', imgray)

cv.waitKey(0)
cv.destroyAllWindows()