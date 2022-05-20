#corners are the region in the image with large variation in intensity in all the directions
import numpy as np
import cv2 as cv

img = cv.imread('chessboard.png')
img = cv.resize(img, (0, 0), fx=0.1, fy=0.1) #resizing image to half its size (because the image size of chessboard.png is actually very big)
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray) #converting coz cornerHarris method take input in float32 format
dst = cv.cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()