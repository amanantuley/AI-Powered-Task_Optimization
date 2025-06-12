import pandas as pd

def get_mood_statistics():
    df = pd.read_csv("mood_history.csv", header=None, names=["timestamp", "emotion"])
    return df["emotion"].value_counts()