import cv2 as cv
img = cv.imread('lena.jpg', 0)
invert = cv.bitwise_not(img)
blur = cv.GaussianBlur(invert, (21, 21), sigmaX=0, sigmaY=0)
iblur = cv.bitwise_not(blur)
sketch = cv.divide(img, iblur, scale = 256.0)

cv.imshow('sketch', sketch)
cv.waitKey(0)
cv.destroyAllWindows()