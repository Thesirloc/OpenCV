# import cv2 as cv
# from matplotlib import pyplot as plt
#
# img = cv.imread('lena.jpg', -1)
# cv.imshow('img', img)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(img)
# #plt.xticks([]), plt.yticks([])
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('gradient.png') # goes from pixel value 0 to 255 from left to right (check)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # assigns 0 to value less then threshold and 1 to greater value
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # opp of above
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # lower value remains same as before, after threshold value remains constant
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # lower value 0 greater value same as before
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # opp of above

titles = ['Original Image', 'binary', 'binary inv', 'trunc', 'tozero', 'tozero inv']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()