# OpenCV program to detect face in real time from webcam footage.
import cv2

# Hooks up camera to the default video capture device.
camera = cv2.VideoCapture(0)

# The classifier we use. HAAR is slower than some other options, but
# is more accurate. We can tune this later.
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while 1:
    # Read the current image from the webcam.
    success, img = camera.read()
    if not success:
        print("Error reading from webcam.")
        break

    # The classifier expects images to be greyscale. This performs the
    # conversion.
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Check for esc keypress.
    k = cv2.waitKey(30) & 0xff    
    if k == 27: 
        break

    # Perform the detection with some standard params.
    faces = faceCascade.detectMultiScale(
        greyscale,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    # Iterate over the found faces.
    for (x, y, w, h) in faces:
        colorFace = img[y:y + h, x:x + w]
        # To write extracted face to file uncomment the line below
        # this and create a directory called "example_faces" where the
        # program will write the faces to.
        # cv2.imwrite("example_faces/" + str(w) + str(h) + '_faces.jpg', colorFace)

        # Draw a rectangle over the face.
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the image with the rectanges drawn on it.
    cv2.imshow('webcam', img)
