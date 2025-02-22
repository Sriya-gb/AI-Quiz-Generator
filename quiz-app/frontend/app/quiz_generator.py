#C:\Users\sriya\quiz-app\ai-quiz-gen\app\quiz_generator.py
import requests
from requests.exceptions import RequestException
from tenacity import retry, stop_after_attempt, wait_fixed

API_URL = "https://sriyagangothri-mcq.hf.space/generate-mcq/"

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def generate_quiz(text, num_questions=5):
    try:
        response = requests.post(API_URL, json={"text": text, "num_questions": num_questions}, timeout=30)
        response.raise_for_status()
        return response.json()["mcqs"]
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")


