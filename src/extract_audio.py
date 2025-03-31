import os
import ffmpeg

def extract_audio(video_path, output_audio_path):
    """Extracts audio from video and saves as a WAV file."""
    input_video = ffmpeg.input(video_path)
    audio = input_video.audio.output(output_audio_path, format="wav", acodec="pcm_s16le")
    ffmpeg.run(audio, overwrite_output=True, quiet=True)
    return output_audio_path

if __name__ == "__main__":
    extract_audio(video_path, output_audio_path)
