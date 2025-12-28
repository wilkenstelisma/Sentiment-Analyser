# Sentiment Analysis App

Streamlit app that scores the sentiment of a statement using TextBlob. Enter text, press Enter or click **Analyze Sentiment**, and it returns Very Positive, Positive, Neutral, Negative, or Very Negative based on polarity.

## Requirements
- Python 3.9+
- Install deps from `requirements.txt`:
  - streamlit
  - textblob

## Setup (Windows PowerShell)
```powershell
cd "c:\Users\wilke\Coding Projects\Sentiment Analyser"
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run
```powershell
cd "c:\Users\wilke\Coding Projects\Sentiment Analyser"
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Usage
1) Type a statement in the input box.  
2) Press Enter or click **Analyze Sentiment**.  
3) The app displays the sentiment label derived from TextBlob polarity.  

## Notes
- If you prefer activation scripts, use `.\.venv\Scripts\Activate.ps1`, then `streamlit run app.py`.  
- TextBlob uses simple lexicon-based sentiment; results are heuristic.***
