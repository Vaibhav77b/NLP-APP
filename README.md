# NLP Desktop App

A Python desktop app for NLP tasks using Hugging Face models.

---

## Features
- Sentiment analysis
- Emotion detection
- Text Summarization
- Named Entity Recognition
- Translation (Anything --> English)
---

## Requirements
- Python 3.12+
- Pip

---

## Installation
Just copy and paste this in your terminal and look out for the virutal environment creation part that'll go according to your device
1. Clone the repository:

```bash
# At home or any other directory you want to add to,
git clone https://github.com/dev-vaibhav-0/NLP-APP.git
cd ~/NLP-APP

    # Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # Linux/Mac | --> For users using Fish(linux) its . venv/bin/activate.fish
venv\Scripts\activate      # Windows

    # Install dependencies:

pip install -r requirements.txt

    # Make a .env and make a variable named exactly-    HF_TOKEN   in HF_TOKEN add your Huggingface token

    # After making .env, Run the Application
python3 main.py
```
---

# Cli

To run the Cli, (No login) do python main-cli.py after making venvs and downloads requirements.txt
