import os
from extract_audio import extract_audio
from transcribe import transcribe_audio
from sentiment import analyze_sentiment

RAW_FOLDER = "data/raw/"
PROCESSED_FOLDER = "data/processed/"

def process_all_videos():
    """Processes all videos in `raw/` one by one."""
    video_files = [f for f in os.listdir(RAW_FOLDER) if f.endswith(".mp4")]

    for video in video_files:
        video_path = os.path.join(RAW_FOLDER, video)
        base_name = os.path.splitext(video)[0]

        audio_path = os.path.join(PROCESSED_FOLDER, f"{base_name}.wav")
        csv_transcription = os.path.join(PROCESSED_FOLDER, f"{base_name}_transcription.csv")
        csv_final = os.path.join(PROCESSED_FOLDER, f"{base_name}_final.csv")

        print(f"📢 Processing {video}...")

        extract_audio(video_path, audio_path)
        transcribe_audio(audio_path, csv_transcription)
        analyze_sentiment(csv_transcription, csv_final)

        print(f"✅ Finished processing: {video}")

if __name__ == "__main__":
    process_all_videos()
