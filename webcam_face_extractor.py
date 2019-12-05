# OpenCV program to detect face in real time from webcam footage.
import cv2

def make_webcam_face_getter():
    imageCount = 0
    # Hooks up camera to the default video capture device.
    camera = cv2.VideoCapture(0)
    cameraIndex = 0
    if not camera.isOpened():
        camera = cv2.VideoCapture(1)
        cameraIndex = 1

    print("camera: " + str(cameraIndex))
    import time
    time.sleep(10)

    # The classifier we use. HAAR is slower than some other options, but
    # is more accurate. We can tune this later.
    faceCascade = cv2.CascadeClassifier(
        "/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml")

    # Get dimensions of camera.
    width  = camera.get(3) # float
    height = camera.get(4) # float

    def zoomer():
        nonlocal cameraIndex
        nonlocal imageCount
        # Make a new camera every time so that there
        # is no buffer that will mix us up.
        camera = cv2.VideoCapture(cameraIndex)

        if not camera.isOpened():
            print("[error] couldn't open camera. Aborting and trying new index.")
            cameraIndex += 1
            cameraIndex = cameraIndex % 2
            return []

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
            cv2.imwrite("images/" + str(imageCount) + '.jpg', colorFace)
            imageCount += 1
        camera.release()
        return faces

    return zoomer, width, height
