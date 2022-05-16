import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('water.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25 # 5x5 matrix of 1/25 (1/width*length)

filter2d = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5)) #does the same thing as filter2d with our kernel (1/width*length)
gblur = cv.GaussianBlur(img, (5,5), 0) # weighed towards the centre (different matrix)
median = cv.medianBlur(img, 5) # best for salt and pepper noise
                               # replaces each pixel's value with median of neighboring pixels
                               # make sure kernel size is odd
bilateralfilter = cv.bilateralFilter(img, 9, 75,75) # used when we need to prevent border while blurring
                                                    # more info on wikipedia page of bilateral filter
images = [img, filter2d, blur, gblur, median, bilateralfilter]
titles = ['img', '2d convolution', 'blur', 'gaussian blur', 'median', 'bilateralfilter']
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()