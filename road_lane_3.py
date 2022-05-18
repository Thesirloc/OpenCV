import cv2 as cv
import numpy as np


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    print(match_mask_color)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_img, (x1, y1), (x2, y2), (0,255,0), thickness=3)

    img = cv.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img

# image = cv.imread('road.png')
# image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
def process(image):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)
    ]
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    canny_image = cv.Canny(gray_image, 50, 120)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    lines = cv.HoughLinesP(cropped_image, rho=6, theta=np.pi / 60, threshold=50, lines=np.array([]), minLineLength=1,
                           maxLineGap=100)

    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines

cap = cv.VideoCapture('test.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    if ret == True:
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()