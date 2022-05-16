# import cv2 as cv
# import numpy as np
#
# img = np.zeros((300,512,3), np.uint8)
#
# def nothing(x):
#     print(x)
#
# cv.namedWindow('image')
# cv.createTrackbar('B', 'image', 0, 255, nothing)
# cv.createTrackbar('G', 'image', 0,255, nothing)
# cv.createTrackbar('R', 'image', 0,255, nothing)
# while(1):
#     cv.imshow('image', img)
#     k = cv.waitKey(1) & 0xFF
#     b = cv.getTrackbarPos('B', 'image')
#     g = cv.getTrackbarPos('G', 'image')
#     r = cv.getTrackbarPos('R', 'image')
#
#     img[:] = [b,g,r]
#     if k==27:
#         break
#
# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np
#
# img = np.zeros((300,512,3), np.uint8)
#
# def nothing(x):
#     print(x)
#
# cv.namedWindow('image')
#
# switch = 'on or off'
#
# cv.createTrackbar('B', 'image', 0, 255, nothing)
# cv.createTrackbar('G', 'image', 0,255, nothing)
# cv.createTrackbar('R', 'image', 0,255, nothing)
# cv.createTrackbar(switch, 'image', 0,1,nothing)
# while(1):
#     cv.imshow('image', img)
#     k = cv.waitKey(1) & 0xFF
#     b = cv.getTrackbarPos('B', 'image')
#     g = cv.getTrackbarPos('G', 'image')
#     r = cv.getTrackbarPos('R', 'image')
#     s = cv.getTrackbarPos(switch, 'image')
#     if s==0:
#         img[:] = 0 # make it black
#         #pass  #this is for locking the color
#     else:
#         img[:] = [b,g,r]
#     if k==27:
#         break
#
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np


def nothing(x):
    pass

cv.namedWindow('image')

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0,1,nothing)
cv.createTrackbar('pos', 'image',  19, 321, nothing)
while(1):
    img = cv.imread('lena.jpg')
    s = cv.getTrackbarPos(switch, 'image')
    pos = cv.getTrackbarPos('pos', 'image')
    cv.putText(img, str(pos), (50,50), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 1)
    if s==0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break
    img = cv.imshow('image', img)

cv.destroyAllWindows()