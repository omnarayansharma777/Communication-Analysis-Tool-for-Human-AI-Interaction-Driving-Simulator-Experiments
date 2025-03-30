import whisper
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

model = whisper.load_model("base")

def transcribe_audio(audio_path, output_csv):
    """Transcribes an audio file and processes it into 5-second segments."""
    result = model.transcribe(audio_path)
    segments = result["segments"]

    grouped_segments = group_into_5s_segments(segments)

    df = pd.DataFrame({
        "Timestamp": [t for t, _ in grouped_segments],
        "Transcription": [text for _, text in grouped_segments]
    })
    df.to_csv(output_csv, index=False)
    print(f"✅ Transcription completed: {output_csv}")

# Step 7: Process Transcription into 5-Second Segments
def group_into_5s_segments(segments):
    grouped_segments = []
    current_segment_text = []
    segment_start_time = None
    segment_end_time = None

    for segment in segments:
        start_time = round(segment["start"], 2)
        end_time = round(segment["end"], 2)
        text = segment["text"]

        # If this is the first segment or we exceeded 5 seconds
        if segment_start_time is None:
            segment_start_time = start_time
            segment_end_time = min(segment_start_time + 5, end_time)  # Ensure max 5s window
        
        elif end_time - segment_start_time > 5:
            # Save previous segment
            grouped_segments.append((
                f"{segment_start_time:.2f} - {segment_end_time:.2f}",
                " ".join(current_segment_text)
            ))
            
            # Start new segment
            segment_start_time = end_time  # Start from this segment
            segment_end_time = min(segment_start_time + 5, end_time)  # Max 5s
            current_segment_text = []

        current_segment_text.append(text)

    # Add last segment if it exists
    if current_segment_text:
        grouped_segments.append((
            f"{segment_start_time:.2f} - {segment_end_time:.2f}",
            " ".join(current_segment_text)
        ))

    return grouped_segments
