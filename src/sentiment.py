import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment(transcription_file):
    df = pd.read_csv(transcription_file)
    df["Sentiment"] = df["Transcription"].apply(get_sentiment)
    output_file = transcription_file.replace("transcription", "sentiment")
    df.to_csv(output_file, index=False)
    print(f"✅ Sentiment analysis saved as {output_file}")

if __name__ == "__main__":
    analyze_sentiment("data/processed/transcription_sample.csv")
