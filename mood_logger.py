import csv
from datetime import datetime

LOG_FILE = "mood_history.csv"

def log_emotion(emotion):
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), emotion])