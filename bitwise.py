import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1[0:250, 250:500] = [255,255,255] #VERY IMPORTANT - take care of the coordinates
cv2.imshow('img1', img1)

img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2, (200,0), (300,100), [255,255,255], -1)
cv2.imshow('img2', img2)

# bitAnd = cv2.bitwise_and(img1,img2)
#cv2.imshow('and', bitAnd)

# bitOr = cv2.bitwise_or(img1,img2)
# cv2.imshow('or', bitOr)

# bitXor = cv2.bitwise_xor(img1,img2)
# cv2.imshow('xor', bitXor)

# bitNot = cv2.bitwise_not(img1)
# cv2.imshow('not', bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()