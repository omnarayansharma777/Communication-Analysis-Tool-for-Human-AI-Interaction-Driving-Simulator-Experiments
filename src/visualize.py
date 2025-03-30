import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df):
    sentiment_counts = df["Sentiment"].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Classification Distribution")
    plt.show()

def plot_cumulative_sentiment(df):
    df["Count"] = 1
    sentiment_cumulative = df.pivot_table(index="Timestamp", columns="Sentiment", values="Count", aggfunc="sum", fill_value=0).cumsum()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=sentiment_cumulative, marker="o")
    plt.xlabel("Timestamp")
    plt.ylabel("Cumulative Sentiment Count")
    plt.title("Cumulative Sentiment Trends Over Time")
    plt.legend(["Negative", "Neutral", "Positive"])
    plt.grid(True)
    plt.show()

def visualize(csv_file):
    df = pd.read_csv(csv_file)
    plot_sentiment_distribution(df)
    plot_cumulative_sentiment(df)

if __name__ == "__main__":
    visualize("data/processed/sentiment_sample.csv")
