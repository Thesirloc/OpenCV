# import cv2 as cv
# import numpy as np
#
# img = cv.imread('lena.jpg')
# lr1 = cv.pyrDown(img) #low resolution image
# lr2 = cv.pyrDown(lr1)
# hr2 = cv.pyrUp(lr2)
# hr1 = cv.pyrUp(hr2)
#
# cv.imshow('OG', img)
# cv.imshow('pyrdown 1', lr1)
# cv.imshow('pyrdown 2', lr2)
# cv.imshow('pyrup 1', hr1)
# cv.imshow('pyrup 2', hr2)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import cv2 as cv
# import numpy as np
#
# img = cv.imread('lena.jpg')
# layer = img.copy()
#
# gp = [layer] # gaussian pyramid (list of images)
#
# for i in range(6):
#     layer = cv.pyrDown(layer)
#     gp.append(layer)
#     cv.imshow(str(i), layer)
#
# cv.imshow('OG', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
layer = img.copy()

gp = [layer] #gaussian pyramid

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i), layer)

layer = gp[5]
cv.imshow('upper level', layer)
lp = [layer] #laplacian pyramid

for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended) # the result is like edge detection
    cv.imshow(str(i), laplacian)

cv.imshow('OG', img)
cv.waitKey(0)
cv.destroyAllWindows()