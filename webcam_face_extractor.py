# OpenCV program to detect face in real time 
import cv2  
  
camera = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while 1:
    success, img = camera.read()
    if not success:
        print("Error reading from webcam.")
        break
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Check for esc keypress.
    k = cv2.waitKey(30) & 0xff    
    if k == 27: 
        break
    faces = faceCascade.detectMultiScale(
        greyscale,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        colorFace = img[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('webcam', img)
