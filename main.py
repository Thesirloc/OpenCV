import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('._yo.jpg')

plt.imshow(img)
plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()