import threading
import cv2
from deepface import DeepFace

# Initialize webcam
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Frame counter and flag for face match
frame_count = 0
is_match = False

# Load reference image
ref_image = cv2.imread("reference.jpg")

# Face comparison function
def match_face(live_frame):
    global is_match
    try:
        result = DeepFace.verify(live_frame, ref_image.copy())
        is_match = result.get("verified", False)
    except ValueError:
        is_match = False

# Main loop
while True:
    success, frame = camera.read()

    if success:
        # Run verification every 30 frames
        if frame_count % 30 == 0:
            try:
                threading.Thread(target=match_face, args=(frame.copy(),)).start()
            except Exception:
                pass

        frame_count += 1

        # Display result on screen
        status_text = "Face Matched" if is_match else "Face Not Matched"
        color = (0, 255, 0) if is_match else (0, 0, 255)

        cv2.putText(frame, status_text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)
        cv2.imshow("Face Recognition", frame)

    # Exit condition
    if cv2.waitKey(1) == ord('d'):
        break

cv2.destroyAllWindows()
