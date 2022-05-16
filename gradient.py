# EDGE DETECTION

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg', 0)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3) # cv.CV_64F is just a datatype (64-bit float) which supports negative numbers that we have to deal with
                                   # the gradient of going from white to black will be negative
lap = np.uint8(np.absolute(lap)) # converting back to uint8 dtype suitable for our images

#use sudoku image to demonstrate sobel methods
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelcombined = cv.bitwise_and(sobelX, sobelY, )
images = [img, lap, sobelX, sobelY, sobelcombined]
titles = ['img', 'Laplacian', 'sobelX', 'sobelY', 'combined']
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()