import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow("canny", edges)
lines = cv.HoughLines(edges, 1, np.pi/180, 200) # returns output vector of lines in polar coordinates
#rho = distance from (0,0) (topleft corner), theta is line rotation angle in radians
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho # (x0, y0) is origin of image (topleft corner) in cartesian coordinates
    y0 = b*rho

    x1 = int(x0 + 1000*(-b)) # rounded off value of (r*cos(theta) - 1000*sin(theta))
    y1 = int(y0 + 1000*(a)) # rounded off value of (r*sin(theta) + 1000*cos(theta))
    x2 = int(x0 - 1000*(-b)) # rounded off value of (r*cos(theta) + 1000*sin(theta))
    y2 = int(y0 - 1000*(a)) # rounded off value of (r*sin(theta) - 1000*cos(theta))
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()