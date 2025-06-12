task_map = {
    "happy": ["Lead a meeting", "Work on creative tasks"],
    "sad": ["Take a break", "Do light admin work"],
    "angry": ["Take a short walk", "Do solo tasks"]
}

def recommend_tasks(emotion):
    return task_map.get(emotion, ["Review tasks or talk to manager"])