import whisper
import pandas as pd
import torch
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium").to(device)

def transcribe_audio(audio_path, output_csv):
    """Transcribes audio and saves as a single CSV with formatted timestamps."""
    result = model.transcribe(audio_path, language="en", word_timestamps=True)

    # Process transcription into 5-second chunks
    segments = []
    temp_text = []
    segment_start = None

    for segment in result["segments"]:
        start_time = round(segment["start"], 2)
        end_time = round(segment["end"], 2)
        text = segment["text"]

        if segment_start is None:
            segment_start = start_time  # Set the start of the first segment

        temp_text.append(text)

        # Start a new segment after 5 seconds
        if end_time - segment_start >= 5:
            segments.append((f"{segment_start:.2f} - {end_time:.2f}", " ".join(temp_text)))
            temp_text = []
            segment_start = end_time  # Reset segment start time

    # Add any remaining text
    if temp_text:
        segments.append((f"{segment_start:.2f} - {end_time:.2f}", " ".join(temp_text)))

    # Save to CSV
    df = pd.DataFrame(segments, columns=["Timestamp", "Transcription"])
    df.to_csv(output_csv, index=False)
    print(f"✅ Transcription saved: {output_csv}")

if __name__ == "__main__":
    audio_path = "data/processed/sample_audio.wav"
    output_csv = "data/processed/sample_transcription.csv"
    transcribe_audio(audio_path, output_csv)
