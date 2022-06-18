# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('vtest.avi')
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG() #foreground_background (we are creating a background object of the function)
# #fgbg = cv.createBackgroundSubtractorMOG2() #foreground_background (we are creating a background object of the function)
# #fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False) #foreground_background (we are creating a background object of the function)
# # fgbg = cv.createBackgroundSubtractorKNN() #foreground_background (we are creating a background object of the function)
#
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     fgmask = fgbg.apply(frame) #foreground mask
#     fin = cv.bitwise_and(frame, frame, mask=fgmask)
#     # fgmask = np.multiply(fgmask, [1,1,1])
#     # colorforeground = np.multiply(fgmask, frame)
#     print(fgmask.shape)
#     print('a')
#     print(frame.shape)
#     cv.imshow('Frame', frame)
#     # cv.imshow('FG mask', fgmask)
#     cv.imshow('c', fin)
#     keyboard = cv.waitKey(30)
#     if keyboard == 'q' or keyboard ==27:
#         break
# cap.release()
# cv.destroyAllWindows()
#

import numpy as np
import cv2 as cv
img = cv.imread('bg.png')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG() #foreground_background (we are creating a background object of the function)
# fgbg = cv.createBackgroundSubtractorMOG2() #foreground_background (we are creating a background object of the function)
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False) #foreground_background (we are creating a background object of the function)
# fgbg = cv.createBackgroundSubtractorKNN() #foreground_background (we are creating a background object of the function)

fgmask = fgbg.apply(img) #foreground mask
fin = cv.bitwise_and(img, img, mask=fgmask)
# fgmask = np.multiply(fgmask, [1,1,1])
# colorforeground = np.multiply(fgmask, frame)
print(fgmask.shape)
print('a')
print(img.shape)
cv.imshow('Frame', img)
cv.imshow('FG mask', fgmask)
cv.imshow('c', fin)
cv.waitKey(0)


