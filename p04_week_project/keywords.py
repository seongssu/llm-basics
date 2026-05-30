from openai import OpenAI
from open_api import get_client

def get_emotion(text):
    client = get_client()
    response = client.responses.create(
        model= "gpt-5",
        input= f"""
        {text}의 감정을 분석하고,
        
        positive, negative, neutral 중 하나로 알려주세요
        3개의 값말고 다른 값은 필요없습니다!
        """
    )
    return response.output_text.strip()