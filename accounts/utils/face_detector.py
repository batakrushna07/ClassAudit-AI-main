import cv2
import face_recognition
import numpy as np

def detect_faces(frame):
    # Ensure the frame is 8-bit (uint8)
    if frame.dtype != np.uint8:
        frame = frame.astype(np.uint8)

    # Convert to RGB robustly
    if len(frame.shape) == 2:  # Grayscale
        rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    elif frame.shape[2] == 4:  # BGRA
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
    else:  # BGR
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb)
    return locations
