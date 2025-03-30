import os
import ffmpeg
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path, codec="pcm_s16le")
    return output_audio_path

if __name__ == "__main__":
    video_path = "data/raw/sample.mp4"
    output_audio = "data/processed/sample.wav"
    extract_audio(video_path, output_audio)
