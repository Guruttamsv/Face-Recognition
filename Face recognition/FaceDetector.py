import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("tfl.png")

grayscaled_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()
print(face_coordinates)
    
print("hello world")