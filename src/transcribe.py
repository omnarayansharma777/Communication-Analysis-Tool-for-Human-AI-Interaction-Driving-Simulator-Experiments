import whisper
import os
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium").to(device)

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path, language="en", word_timestamps=True)
    return result["segments"]

if __name__ == "__main__":
    audio_path = "data/processed/sample.wav"
    segments = transcribe_audio(audio_path)
    print(segments)
