import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

def plot_word_count_histogram(df):
    word_counts = []
    time_buckets = []

    for index, row in df.iterrows():
        timestamp = row["Timestamp"]
        transcription = row["Transcription"]
        word_count = len(transcription.split())  # Count words in transcription

        time_buckets.append(timestamp)
        word_counts.append(word_count)

    # Plot histogram
    plt.figure(figsize=(10, 5))
    sns.barplot(x=time_buckets, y=word_counts, palette="viridis")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Timestamp (5-sec Buckets)")
    plt.ylabel("Word Count")
    plt.title("Word Count per 5-Second Interval")
    plt.tight_layout()
    plt.savefig("word_count_histogram.png")
    plt.show()

def plot_sentiment_distribution(df):
    sentiment_counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Classification Distribution")
    plt.tight_layout()
    plt.savefig("sentiment_distribution.png")
    plt.show()

def plot_cumulative_sentiment_trend(df):
    # Convert timestamps to sorted order
    df["Timestamp"] = df["Timestamp"].astype(str)
    df = df.sort_values("Timestamp")

    # Initialize cumulative counts
    cumulative_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    timestamps = []
    pos_counts, neg_counts, neu_counts = [], [], []

    for _, row in df.iterrows():
        sentiment = row["Sentiment"]
        if sentiment in cumulative_counts:  # Check if sentiment is in our dictionary
            cumulative_counts[sentiment] += 1  # Increase count for the respective sentiment

        # Store values for plotting
        timestamps.append(row["Timestamp"])
        pos_counts.append(cumulative_counts["Positive"])
        neg_counts.append(cumulative_counts["Negative"])
        neu_counts.append(cumulative_counts["Neutral"])

    # Plot cumulative trend
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, pos_counts, label="Positive", color="green", marker="o")
    plt.plot(timestamps, neg_counts, label="Negative", color="red", marker="o")
    plt.plot(timestamps, neu_counts, label="Neutral", color="blue", marker="o")

    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Timestamp (5-sec Buckets)")
    plt.ylabel("Cumulative Sentiment Count")
    plt.title("Cumulative Sentiment Trend Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("cumulative_sentiment_trend.png")
    plt.show()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python app.py <filename.csv>")
        print("Example: python app.py data.csv")
        sys.exit(1)
    
    # Get the filename from command-line argument
    filename = sys.argv[1]
    
    # Construct the full path based on whether a relative or absolute path was provided
    if os.path.isabs(filename):
        file_path = filename
    else:
        # If it's a relative path, look in the data/processed directory first
        default_dir = os.path.join("data", "processed")
        if os.path.exists(os.path.join(default_dir, filename)):
            file_path = os.path.join(default_dir, filename)
        else:
            # Otherwise, use the current directory
            file_path = filename
    
    print(f"Loading data from: {file_path}")
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    # Load the data
    try:
        df = pd.read_csv(file_path)
        
        # Ensure correct column names
        if set(["Timestamp", "Transcription", "Sentiment"]).issubset(set(df.columns)):
            print("Column names are already correct.")
        else:
            print("Renaming columns to standard format...")
            if len(df.columns) >= 3:
                df.columns = ["Timestamp", "Transcription", "Sentiment"] + list(df.columns[3:])
            else:
                print("Error: CSV file doesn't have enough columns. Expected at least 3 columns.")
                sys.exit(1)
        
        # Generate plots
        print("Generating word count histogram...")
        plot_word_count_histogram(df)
        
        print("Generating sentiment distribution plot...")
        plot_sentiment_distribution(df)
        
        print("Generating cumulative sentiment trend...")
        plot_cumulative_sentiment_trend(df)
        
        print("Analysis complete! Plots have been saved as PNG files.")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
