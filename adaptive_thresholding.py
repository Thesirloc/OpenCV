import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',0)

_, th = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("img", img)
cv.imshow("th", th)
cv.imshow("th1", th1)
cv.imshow("th2", th2)


cv.waitKey(0)
cv.destroyAllWindows()