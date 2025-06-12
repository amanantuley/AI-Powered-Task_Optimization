import cv2
from deepface import DeepFace

def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)[0]
        return result['dominant_emotion']
    except:
        return None
