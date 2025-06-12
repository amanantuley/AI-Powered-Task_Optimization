from collections import deque

emotion_buffer = deque(maxlen=10)

def check_stress(emotion):
    emotion_buffer.append(emotion)
    if all(e in ["sad", "angry"] for e in emotion_buffer):
        return True
    return False