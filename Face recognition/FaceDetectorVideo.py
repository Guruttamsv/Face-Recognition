import cv2 as cv
path= r''
capture=cv.VideoCapture(path)
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    if 0xFF==ord(' '):
        break
capture.release()
cv.destroyAllWindows()