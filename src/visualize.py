import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(csv_path):
    """Generates a bar chart showing sentiment distribution."""
    df = pd.read_csv(csv_path)
    
    sentiment_counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(10, 5))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Distribution")
    plt.show()

def plot_cumulative_sentiment(csv_path):
    """Generates a cumulative sentiment trend over time."""
    df = pd.read_csv(csv_path)
    df["Count"] = 1  # Assign count per sentiment occurrence

    # Pivot table for cumulative counts
    sentiment_cumulative = df.pivot_table(index="Timestamp", columns="Sentiment", values="Count", aggfunc="sum", fill_value=0)
    sentiment_cumulative = sentiment_cumulative.cumsum()  # Cumulative sum

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=sentiment_cumulative, marker="o", dashes=False)
    plt.xlabel("Timestamp")
    plt.ylabel("Cumulative Sentiment Count")
    plt.title("Cumulative Sentiment Trends Over Time")
    plt.legend(["Negative", "Neutral", "Positive"])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    csv_path = "data/processed/sample_final.csv"
    plot_sentiment_distribution(csv_path)
    plot_cumulative_sentiment(csv_path)
