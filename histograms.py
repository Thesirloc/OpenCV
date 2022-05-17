# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = np.zeros((200, 200), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)
# cv.imshow("img", img)
#
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv.imread('lena.jpg')
# #cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# #cv.rectangle(img, (0, 50), (100, 100), (127), -1)
# b, g, r = cv.split(img)
#
# cv.imshow("img", img)
# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
# print(b)
# plt.hist(b.ravel(), 256, [0, 256]) # ravel method converts multi-d array to 1d array for plotting
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()