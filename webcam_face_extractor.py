# OpenCV program to detect face in real time from webcam footage.
import cv2

def make_webcam_face_getter():
    imageCount = 0

    # Hooks up camera to the default video capture device.
    camera = cv2.VideoCapture(0)

    # The classifier we use. HAAR is slower than some other options, but
    # is more accurate. We can tune this later.
    faceCascade = cv2.CascadeClassifier(
        "/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
#    faceCascade = cv2.CascadeClassifier(
#        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


    # Get dimensions of camera.
    width  = camera.get(3) # float
    height = camera.get(4) # float
    
    def zoomer():
        success, img = camera.read()
        
        if not success:
            print("[error] Could't read from webcam.")
            return
        greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Perform the detection with some standard params.
        faces = faceCascade.detectMultiScale(
            greyscale,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )

        # Iterate over the found faces and write them away.
        for (x, y, w, h) in faces:
            colorFace = img[y:y + h, x:x + w]
            # To write extracted face to file uncomment the line below
            # this and create a directory called "example_faces" where the
            # program will write the faces to.
#            cv2.imwrite("images/" + str(imageCount) + '.jpg', colorFace)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('dog', img)
        return faces

    return zoomer, width, height
