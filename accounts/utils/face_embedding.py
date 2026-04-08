import cv2
import face_recognition
import numpy as np

import logging

logger = logging.getLogger(__name__)

def get_embedding(frame, face_location=None):
    """
    Returns face embedding for the detected face in frame.
    
    Args:
        frame: The image frame (BGR format from OpenCV)
        face_location: Optional tuple (top, right, bottom, left) of face location.
                       If None, the function will detect faces automatically.
    
    Returns:
        Face embedding array or None if detection fails
    """
    try:
        # Ensure the frame is 8-bit (uint8)
        if frame.dtype != np.uint8:
            frame = frame.astype(np.uint8)

        # Handle different channel counts and convert to RGB
        if len(frame.shape) == 2:  # Grayscale
            rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        elif frame.shape[2] == 4:  # BGRA (with alpha channel)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        elif frame.shape[2] == 3:  # BGR (standard OpenCV)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            logger.error("Unsupported number of channels: %d", frame.shape[2])
            return None

        # Ensure the array is contiguous for face_recognition
        if not rgb.flags['C_CONTIGUOUS']:
            rgb = np.ascontiguousarray(rgb)
        if face_location is not None:
            # Use provided face location - wrap in list for face_encodings
            known_face_locations = [face_location]
            encodings = face_recognition.face_encodings(rgb, known_face_locations)
        else:
            # Auto-detect faces
            locations = face_recognition.face_locations(rgb)
            
            # For auto-detection, require exactly one face
            if len(locations) != 1:
                return None
            
            # Get encodings - let face_recognition handle face detection internally
            # This is more compatible across different library versions
            encodings = face_recognition.face_encodings(rgb)

        if not encodings:
            return None

        return encodings[0]
    
    except Exception as e:
        logger.error("Error getting face embedding: %s", e)
        return None


def average_embeddings(embeddings):
    return np.mean(embeddings, axis=0)
