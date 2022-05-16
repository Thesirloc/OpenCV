# import cv2
# import numpy as np
#
# img = cv2.imread('messi5.jpg')
#
# print(img.shape) # returns a tuple of number of rows, columns and channels
# print(img.size) # Total number of pixels is accessed
# print(img.dtype) # Image datatype is obtained
#
# b,g,r = cv2.split(img) # splits image into b,g,r
#
# img = cv2.merge((b,g,r)) # merges a b,g,r into array to make immage
#
# cv2.imshow('img', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# img = cv2.imread('messi5.jpg')
#       #img[y1:y2,x1:x2] where (x1,y1) is upper left and (x2,y2) is lower right
# ball = img[280:340 , 330:390] # img[upper left corner of ball, lower right corner of ball] the coordinates were
#                               # found by methods learned in prev lessons.
# img[273:333, 100:160] = ball #where you want to place the ball
# cv2.imshow('img', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('lena.jpg')

img = cv2.resize(img, (512,512))  #resizing of images is done because cv2.add function takes images of same size only
img2 = cv2.resize(img2, (512,512))

final = cv2.add(img,img2)
cv2.imshow('img', final)

# final = cv2.addWeighted(img, 0.9,img2,0.1,0) #in order to add weighted images: img1 x alpha , img2 x beta
                                               # gamma is the scaler to be added
# cv2.imshow('img', final)

cv2.waitKey(0)
cv2.destroyAllWindows()