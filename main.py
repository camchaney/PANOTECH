# Main entry point for controlls.
from pyserial import get_serial, send_command
from webcam_face_extractor import make_webcam_face_getter

def make_direction_decider(width):
    DISTANCE_THRESHOLD = 0.15 * width

    def decider(faces):
        if len(faces) == 0:
            return

        # Find the face with the minimum distance from the center.
        # f[0] is its x cord, f[2] is its width.
        target = min(faces, key=lambda f: abs(f[0] + f[2]/2 -
                                              width/2))
        distance = target[0] + target[2] / 2 - width/2

        if abs(distance) > DISTANCE_THRESHOLD:
            if distance < 0:
                return "right"
            else:
                return "left"
        return "none"

    return decider
    
    

def main():
    face_getter, width, height = make_webcam_face_getter()
    controller = make_direction_decider(width)


    while 1:
        faces = face_getter()
        print(controller(faces))

main()

        
