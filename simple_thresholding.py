import cv2 as cv
import numpy as np

img = cv.imread('gradient.png') # goes from pixel value 0 to 255 from left to right (check)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # assigns 0 to value less then threshold and 1 to greater value
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # opp of above
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # lower value remains same as before, after threshold value remains constant
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # lower value 0 greater value same as before
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # opp of above

cv.imshow("image", img)
cv.imshow("th1", th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)

cv.waitKey(0)
cv.destroyAllWindows()