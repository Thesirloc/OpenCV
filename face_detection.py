# import cv2 as cv
#
# face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv.imread('lena.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#
# for (x, y, w, h) in faces:
#     cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
#
#
# cv.imshow('img', img)
# cv.waitKey()

import cv2 as cv

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    return image


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while cap.isOpened():
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
