import os
from extract_audio import extract_audio
from transcribe import transcribe_audio
from sentiment import analyze_sentiment
import pandas as pd

RAW_DIR = "data/raw/"
PROCESSED_DIR = "data/processed/"

def process_all_videos():
    for filename in os.listdir(RAW_DIR):
        if filename.endswith(".mp4") or filename.endswith(".mkv"):
            video_path = os.path.join(RAW_DIR, filename)
            audio_path = os.path.join(PROCESSED_DIR, f"{filename}.wav")
            csv_path = os.path.join(PROCESSED_DIR, f"transcription_{filename}.csv")

            # Extract audio
            extract_audio(video_path, audio_path)
            
            # Transcribe
            segments = transcribe_audio(audio_path)
            df = pd.DataFrame({"Timestamp": [s["start"] for s in segments], "Transcription": [s["text"] for s in segments]})
            df.to_csv(csv_path, index=False)

            # Sentiment Analysis
            analyze_sentiment(csv_path)

if __name__ == "__main__":
    process_all_videos()
