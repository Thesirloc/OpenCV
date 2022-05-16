# import cv2 as cv
# import numpy as np
# apple = cv.imread('apple.jpg')
# orange = cv.imread('orange.jpg')
# print(apple.shape)
# print(orange.shape)
#
# apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
#
# cv.imshow('apple', apple)
# cv.imshow('orange', orange)
# cv.imshow('apple_orange', apple_orange)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv
import numpy as np
apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')
print(apple.shape)
print(orange.shape)

layer1 = apple.copy()
layer2 = orange.copy()
gp1 = [layer1]
gp2 = [layer2]
for i in range(6):
    layer1 = cv.pyrDown(layer1)
    gp1.append(layer1)
    layer2 = cv.pyrDown(layer2)
    gp2.append(layer2)

layer1 = gp1[5]
layer2 = gp2[5]
lp1 = [layer1]
lp2 = [layer2]
for i in range(5,0,-1):
    gaussian_extended1 = cv.pyrUp(gp1[i])
    gaussian_extended2 = cv.pyrUp(gp2[i])
    laplacian1 = cv.subtract(gp1[i-1], gaussian_extended1)
    laplacian2 = cv.subtract(gp2[i-1], gaussian_extended2)
    lp1.append(laplacian1)
    lp2.append(laplacian2)


apple_orange_pyramid = []
n=0
for apple_lap, orange_lap in zip(lp1, lp2):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)



cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('apple_orange', apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()