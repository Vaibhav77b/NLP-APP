import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

class API:
    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=HF_TOKEN,
        )

    def sentiment_analysis(self, text):
        result = self.client.sentiment_analysis(
            text,
            model="tabularisai/multilingual-sentiment-analysis",
        )
        print(result)
        return result
    
    def ner(self, text):
        # Hugging Face NER model
        result = self.client.token_classification(
            text,
            model="dslim/bert-base-NER"
        )
        print(result)
        return result

    def emotion(self, text):
        # Hugging Face Emotion model
        result = self.client.text_classification(
            text,
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )
        print(result)
        return result
    def translation(self, text):
        # Hugging Face Translation model
        result = self.client.translation(
            text,
            model="Helsinki-NLP/opus-mt-es-en"
        )
        print(result)
        return result
    def text_summarization(self, text):
        # Hugging Face Summarization model
        result = self.client.summarization(
            text,
            model="sshleifer/distilbart-cnn-12-6"
        )
        print(result)
        return result