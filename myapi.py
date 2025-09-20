import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Use Flet/pyinstaller safe path
try:
    base_path = os.path.dirname(__file__)
except NameError:
    # __file__ not defined (e.g., in interactive session)
    base_path = os.getcwd()

dotenv_path = os.path.join(base_path, ".env")
load_dotenv(dotenv_path)

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("WARNING: HF_TOKEN not found. Hugging Face API calls will fail!")


class API:
    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=HF_TOKEN,
        )

    def sentiment_analysis(self, text):
        return self.client.sentiment_analysis(
            text, model="tabularisai/multilingual-sentiment-analysis"
        )

    def ner(self, text):
        return self.client.token_classification(text, model="dslim/bert-base-NER")

    def emotion(self, text):
        return self.client.text_classification(
            text, model="j-hartmann/emotion-english-distilroberta-base"
        )
