# My NLP Desktop App

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

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

    # Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # Linux/Mac --> For users using Fish its . venv/bin/activate.fish
venv\Scripts\activate      # Windows

    # Install dependencies:

pip install -r requirements.txt

    # Create a .env file in the project root:

touch .env

# Add your Hugging Face token in .env:

HF_TOKEN=your_hf_token_here
