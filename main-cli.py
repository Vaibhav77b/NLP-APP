import myapi
from myapi import API
import requests
import time


def validate_hf_token(token: str) -> bool:
    """Check if a Hugging Face API token is valid via direct REST call."""
    if not token:
        print("⚠️  Token missing.")
        return False

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get("https://huggingface.co/api/whoami-v2", headers=headers)

    if resp.status_code == 200:
        print("✅ Token is valid.")
        return True
    elif resp.status_code == 401:
        print("❌ Invalid or expired Hugging Face token.")
        return False
    else:
        print(f"⚠️ Unexpected response: {resp.status_code} {resp.text}")
        return False


def main() -> None:
    print("""
███╗░░██╗██╗░░░░░██████╗░  ░█████╗░██████╗░██████╗░██╗░░░░░██╗░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
████╗░██║██║░░░░░██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██╔██╗██║██║░░░░░██████╔╝  ███████║██████╔╝██████╔╝██║░░░░░██║██║░░╚═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║╚████║██║░░░░░██╔═══╝░  ██╔══██║██╔═══╝░██╔═══╝░██║░░░░░██║██║░░██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║░╚███║███████╗██║░░░░░  ██║░░██║██║░░░░░██║░░░░░███████╗██║╚█████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚══╝╚══════╝╚═╝░░░░░  ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

𝙒 elcome to the Natural Level Processing Application. 𝗣lease select one of the options below(Example-1=1,Example-2=NER):
1. Text Summarization (TS)
2. Sentiment Analysis (SA)
3. Emotion Detection (ED)
4. Named Entity Recognition (NER)
5. Translation (T)
""")
    HF_TOKEN = input("𝗣lease enter your Hugging Face API token:\n◄ ◎ ").strip()
    api: API = API(HF_TOKEN)
    if not validate_hf_token(HF_TOKEN):
        print("𝗘xiting... please check your token and try again.")
        time.sleep(1)
        return

    value_of_user_option = input("◄  ").strip().upper()

    if value_of_user_option in ("1", "TS", "ts"):
        print("𝗟oading...")
        time.sleep(1)
        print("𝗟oaded!")
        time.sleep(0.3)

        print("\n𝗘nter your paragraph/sentence that is to be summarized:")
        value_of_user_for_ts = input("◄  ")

        print("\n𝗦ummarizing your text...\n")
        summary_result = api.summarize(value_of_user_for_ts)
        print("𝗦ummary:\n", summary_result[33:-1:])

    elif value_of_user_option in ("2", "SA", "sa"):
        print("𝗟oading...")
        time.sleep(1)
        print("𝗟oaded!")
        time.sleep(0.3)

        print("\n𝗘nter your paragraph/sentence that is to be analysed:")
        value_of_user_for_ts = input("◄  ")

        print("\n𝗣erforming Sentiment Analysis...\n")
        sentiment_result = api.sentiment(value_of_user_for_ts)
        print("𝗦entiment:\n", sentiment_result)

    elif value_of_user_option in ("3", "ED", "ed"):
        print("𝗟oading...")
        time.sleep(1)
        print("𝗟oaded!")
        time.sleep(0.3)

        print("\n𝗘nter your paragraph/sentence that is to be Emotion Detected:")
        value_of_user_for_ts = input("◄  ")

        print("\n𝗣erforming Emotion Detection...\n")
        emotion_result = api.emotion(value_of_user_for_ts)
        print("𝗘motion Detection:\n", emotion_result)

    elif value_of_user_option in ("4", "NER", "ner"):
        print("𝗟oading...")
        time.sleep(1)
        print("𝗟oaded!")
        time.sleep(0.3)

        print("\n𝗘nter your paragraph/sentence that is to be Entity Recognised:")
        value_of_user_for_ts = input("◄  ")

        print("\n𝗣erforming Entity Recognition...\n")
        entity_result = api.ner(value_of_user_for_ts)
        print("𝗘ntity Recognition:\n", entity_result)

    elif value_of_user_option in ("5", "T", "t"):
        print("𝗟oading...")
        time.sleep(1)
        print("𝗟oaded!")
        time.sleep(0.3)

        print("\n𝗘nter your paragraph/sentence that is to be translated:")
        value_of_user_for_ts = input("◄  ")
        print("""\n𝗘nter language.. Available:
        For French, type --> fr
        For German, type --> de 
        For Spanish, type --> es
        For Hindi,type --> hi 
        For Japanese, type --> ja""")

        given_lang_target = input("◄ ◎  ")

        print("\n𝗣erforming Translation...\n")
        translate_result = api.translate(
            value_of_user_for_ts, target_lang=given_lang_target
        )
        print("Translation:\n", translate_result)

    else:
        print("𝗣lease type a valid input")
        exit()


if __name__ == "__main__":
    main()
