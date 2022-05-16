# import cv2 as cv
# import matplotlib.pyplot as plt
# import numpy as np
#
# img = cv.imread('smarties.png', 0)
# _, mask = cv.threshold(img, 240, 255, cv.THRESH_BINARY_INV) #morphological transformations are generally performed on grayscale images
#
# kernal = np.ones((2,2), np.uint8) #small block that will overlap neighboring pixels
#
# dilation = cv.dilate(mask, kernal, iterations=2)
# erosion = cv.erode(mask, kernal, iterations = 2)
# opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal) #erosion then dilation
# closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal) #dilation then erosion
# mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal) #morpholgical gradient: difference b/w dilation and erosion
# th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal) # difference b/w image and opening of image
#
# titles = ['Original Image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
# images = [img, mask, dilation, erosion, opening, closing, mg, th]
#
# for i in range(8):
#     plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
#     plt.title([titles[i]])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('LinuxLogo.jpg', 0)
#_, mask = cv.threshold(img, 240, 255, cv.THRESH_BINARY_INV) #morphological transformations are generally performed on grayscale images

kernal = np.ones((5, 5), np.uint8) #small block that will overlap neighboring pixels

dilation = cv.dilate(img, kernal, iterations=2)
erosion = cv.erode(img, kernal, iterations = 2)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernal) #erosion then dilation
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernal) #dilation then erosion
mg = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernal) #morpholgical gradient: difference b/w dilation and erosion
th = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernal) # difference b/w image and opening of image

titles = ['Original Image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, img, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()