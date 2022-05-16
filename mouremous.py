# import cv2
# import numpy as np
#
# def click_event(event, x, y, flags, param):  #callback function to join two points u clicked on image with a line
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, (x, y), 3, (255,255,0), -1)
#         points.append((x, y))
#         if len(points) >=2:
#             cv2.line(img, points[-1], points[-2], (0,5,222), 3, cv2.LINE_AA)
#         cv2.imshow('image', img)
#
# img = np.zeros((512,512,3), np.uint8)
# #img = cv2.imread('lena.jpg')
#
# points = []
# cv2.imshow('image', img)
#
# cv2.setMouseCallback('image', click_event)  # using callback function in setmousecallback method
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

def click_event(event, x, y, flags, param):  #callback function to create another window filled with color of the
                                             # point you just clicked on
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x,y,1]
        red = img[x,y,2]
        mycolorimage = np.zeros([512,512,3], np.uint8)
        mycolorimage[:] = [blue,green,red]
        cv2.imshow('imag', mycolorimage)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('lena.jpg')

points = []
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)  # using callback function in setmousecallback method

cv2.waitKey(0)
cv2.destroyAllWindows()