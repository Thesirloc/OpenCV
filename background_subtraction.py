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
    cv.imshow('Frame', frame)
    cv.imshow('FG mask', fgmask)
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard ==27:
        break
cap.release()
cv.destroyAllWindows()

