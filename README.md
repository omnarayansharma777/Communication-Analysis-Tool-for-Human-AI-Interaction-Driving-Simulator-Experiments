

# **Communication Analysis Tool for Human-AI Interaction**

## **📌 Project Overview**
This project processes video files containing human-to-human communication data, transcribes the speech, performs sentiment analysis, and visualizes the results. The goal is to analyze **group dynamics in simulated environments** by extracting insights from spoken words.

✅ **Key Features**:  
- **Batch Processing**: Processes multiple video files automatically.  
- **Whisper AI for Speech-to-Text**: Uses OpenAI Whisper for high-accuracy transcription.  
- **Offline Sentiment Analysis**: Uses VADER NLP (no external API required).  
- **5-Second Segmentation**: Breaks transcripts into **5-second chunks** for structured analysis.  
- **Data Pipeline**: Stores raw videos and saves processed transcriptions/sentiment results.  
- **Visualization**: Generates sentiment trend graphs over time.  

---

## **📁 Project Structure**
```
communication-analysis/
│── data/
│   ├── raw/           # Store uploaded videos
│   ├── processed/     # Store generated CSVs (transcriptions & sentiment analysis)
│── src/
│   ├── extract_audio.py   # Extracts audio from videos
│   ├── transcribe.py      # Transcribes audio using Whisper
│   ├── sentiment.py       # Performs sentiment analysis (no external API)
│   ├── visualize.py       # Generates graphs
│   ├── process_all.py     # Processes all videos in `raw/`
│── requirements.txt       # Dependencies
│── README.md              # Setup and Usage Guide
│──cumulative_sentiment_trend.png  # these images will be created later 
│──sentiment_distribution.png
│──word_count_histogram.png  
```

---

## **🚀 Setup & Installation[ Only Colab with GPU ]** 

```
!git clone https://github.com/omnarayansharma777/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments.git

```
### **1️⃣ Install Required Dependencies**
Run the following command to install all necessary Python libraries:
```bash
!cd Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments
!pip install -r "/content/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments/requirements.txt"

```

### **2️⃣ Add Your Video Files**
Place all video files in the `data/raw/` directory.

### **3️⃣ Run the Processing Pipeline**
Run the following command to process **all videos** in the `raw/` folder:
```bash
!python "/content/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments/src/process_all.py"
```
This will:
- Extract audio from each video.
- Transcribe the audio into text.
- Perform sentiment analysis (Positive, Negative, Neutral).
- Save the results in `data/processed/`.

### **4️⃣ Visualize Sentiment Trends**
To analyze a specific processed file, run:
```bash
!python /content/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments/src/visualize.py '/content/Communication-Analysis-Tool-for-Human-AI-Interaction-Driving-Simulator-Experiments/data/processed/<your_video_filename>.csv'
```

This will generate a
**word_count_histogram** , in each window ~5 seconds how many words 

![word_count_histogram (2)](https://github.com/user-attachments/assets/d6baea0c-d236-4ebd-bea6-47d6e1191cf6)

**cumulative sentiment trend graph** ,showing sentiment distribution over time.

![cumulative_sentiment_trend (4)](https://github.com/user-attachments/assets/7ce5aac1-1065-4eee-8d60-34330c8d555f)

**sentiment_distribution** , total number of positive , negative, neutral sentiment

![sentiment_distribution (4)](https://github.com/user-attachments/assets/d5a80f08-77f6-4b98-86cd-17507c0d7c8a)


---

## **📊 Expected Output**
Each processed video will generate a CSV file in `data/processed/` with the following format:

| Timestamp | Transcription | Sentiment |
|-----------|--------------|-----------|
| 0-5 sec   | Hello team!  | Positive  |
| 5-10 sec  | I don't agree with this... | Negative |
| 10-15 sec | Let's find a solution. | Neutral |

A **cumulative sentiment trend graph** will be generated, showing sentiment distribution over time.

---

## **🛠️ How It Works**
### **1️⃣ Audio Extraction**
- Uses `ffmpeg` to extract high-quality WAV audio from video.

### **2️⃣ Speech-to-Text Transcription**
- Uses OpenAI's **Whisper (Medium model)** for accurate transcription. 
- **Supports multiple speakers** and noisy environments.

### **3️⃣ Sentiment Analysis**
- Uses **VADER Sentiment Analysis** (offline, no API required).
- Classifies text as **Positive, Negative, or Neutral**.

### **4️⃣ Visualization**
- **Histogram of word counts per 5-second interval**.
- **Cumulative sentiment trend over time**.

---
