import os
from extract_audio import extract_audio
from transcribe import transcribe_audio
from sentiment import analyze_sentiment

# Define directories

RAW_FOLDER = "/content/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments/data/raw/"
PROCESSED_FOLDER = "/content/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments/data/processed/"

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

        # Delete intermediate files after processing
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print(f"🗑️ Deleted intermediate file: {audio_path}")

        if os.path.exists(csv_transcription):
            os.remove(csv_transcription)
            print(f"🗑️ Deleted intermediate file: {csv_transcription}")

        print(f"✅ Finished processing: {video}")

if __name__ == "__main__":
    process_all_videos()
