# Main entry point for controlls.
from pyserial import get_serial, send_command
from webcam_face_extractor import make_webcam_face_getter
from time import sleep

def make_direction_decider(width):
    DISTANCE_THRESHOLD = 0.25 * width

    def decider(faces):
        try:
            len(faces)
        except:
            return 's'
        if len(faces) == 0:
            return "s"

        print("found " + str(len(faces)) + " faces")
        # Find the face with the minimum distance from the center.
        # f[0] is its x cord, f[2] is its width.
        target = max(faces, key=lambda f: abs(f[0] + f[2]/2 -
                                              width/2))
        distance = target[0] + target[2] / 2 - width/2

        if abs(distance) > DISTANCE_THRESHOLD:
            if distance < 0:
                return "l"
            else:
                return "r"
        return "s"

    return decider

def main():
    face_getter, width, height = make_webcam_face_getter()
    controller = make_direction_decider(width)
    ser = get_serial()

    while 1:
        faces = face_getter()
        command = controller(faces)
        print("[sending] " + command)
#        ser = send_command(ser, command)
#        if ( command == 'l' or command == 'r' ):
#            ser = send_command(ser, 'd')
#            print("sleeping for 20 seconds")
#            sleep(10)

main()


