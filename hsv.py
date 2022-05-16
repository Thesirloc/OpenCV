# import cv2 as cv
# import numpy as np
#
# def nothing(x):
#     pass
#
# while True:
#     frame = cv.imread('smarties.png')
#
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#
#     l_b = np.array([110,50,50]) #lower blue color
#     u_b = np.array([130,255,255]) #upper blue color
#
#     mask = cv.inRange(hsv, l_b, u_b)
#
#     res = cv.bitwise_and(frame, frame, mask=mask)
#
#     cv.imshow('frame', frame)
#     cv.imshow('mask', mask)
#     cv.imshow('res', res)
#
#     key = cv.waitKey(1) & 0xFF
#     if key == 27:
#         break
#
# cv.destroyAllWindows()
#
# import cv2 as cv
# import numpy as np
#
# def nothing(x):
#     pass
#
# cv.namedWindow("tracking")
# cv.createTrackbar("lh", "tracking", 0, 255, nothing)
# cv.createTrackbar("ls", "tracking", 0, 255, nothing)
# cv.createTrackbar("lv", "tracking", 0, 255, nothing)
# cv.createTrackbar("uh", "tracking", 255, 255, nothing)
# cv.createTrackbar("us", "tracking", 255, 255, nothing)
# cv.createTrackbar("uv", "tracking", 255, 255, nothing)
#
# while True:
#     frame = cv.imread('smarties.png')
#
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#
#     lh = cv.getTrackbarPos('lh', 'tracking')
#     ls = cv.getTrackbarPos('ls', 'tracking')
#     lv = cv.getTrackbarPos('lv', 'tracking')
#     uh = cv.getTrackbarPos('uh', 'tracking')
#     us = cv.getTrackbarPos('us', 'tracking')
#     uv = cv.getTrackbarPos('uv', 'tracking')
#
#     l_b = np.array([lh, ls, lv])
#     u_b = np.array([uh, us, uv])
#
#     mask = cv.inRange(hsv, l_b, u_b)
#
#     res = cv.bitwise_and(frame, frame, mask=mask)
#
#     cv.imshow('frame', frame)
#     cv.imshow('mask', mask)
#     cv.imshow('res', res)
#
#     key = cv.waitKey(1) & 0xFF
#     if key == 27:
#         break
#
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow("tracking")
cv.createTrackbar("lh", "tracking", 0, 255, nothing)
cv.createTrackbar("ls", "tracking", 0, 255, nothing)
cv.createTrackbar("lv", "tracking", 0, 255, nothing)
cv.createTrackbar("uh", "tracking", 255, 255, nothing)
cv.createTrackbar("us", "tracking", 255, 255, nothing)
cv.createTrackbar("uv", "tracking", 255, 255, nothing)

while True:
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lh = cv.getTrackbarPos('lh', 'tracking')
    ls = cv.getTrackbarPos('ls', 'tracking')
    lv = cv.getTrackbarPos('lv', 'tracking')
    uh = cv.getTrackbarPos('uh', 'tracking')
    us = cv.getTrackbarPos('us', 'tracking')
    uv = cv.getTrackbarPos('uv', 'tracking')

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()