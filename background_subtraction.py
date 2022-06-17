import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG() #foreground_background (we are creating a background object of the function)
#fgbg = cv.createBackgroundSubtractorMOG2() #foreground_background (we are creating a background object of the function)
#fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False) #foreground_background (we are creating a background object of the function)
# fgbg = cv.createBackgroundSubtractorKNN() #foreground_background (we are creating a background object of the function)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame) #foreground mask
    fgmask = fgmask.reshape(fgmask.shape + (3,))
    # colorforeground = np.multiply(fgmask, frame)
    print(fgmask.shape)
    print('a')
    print(frame.shape)
    cv.imshow('Frame', frame)
    cv.imshow('FG mask', fgmask)
    # cv.imshow('c', colorforeground)
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard ==27:
        break
cap.release()
cv.destroyAllWindows()

