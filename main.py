import cv2
from emotion_recognition import detect_emotion
from task_recommender import recommend_tasks
from mood_logger import log_emotion
from alert_system import check_stress
from analytics import get_mood_statistics
from secure_store import anonymize_user

user_id = anonymize_user()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    emotion = detect_emotion(frame)
    if emotion:
        log_emotion(emotion)
        tasks = recommend_tasks(emotion)

        y = 30
        cv2.putText(frame, f"Emotion: {emotion}", (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        y += 40

        for task in tasks:
            cv2.putText(frame, f"Suggested: {task}", (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            y += 30

        if check_stress(emotion):
            cv2.putText(frame, "STRESS ALERT: Notify HR!", (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("AI Task Optimizer", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()