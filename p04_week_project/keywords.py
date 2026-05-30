from openai import OpenAI
from open_api import get_client

class Keywords():
    def __init__(self, text):
        self.client = get_client()
        self.text = text
        self.model = "gpt-5"
    def get_emotion(self):
        
        response = self.client.responses.create(
            model= self.model,
            input= f"""
            {self.text}의 감정을 분석하고,        
            positive, negative, neutral 중 하나로 알려주세요
            3개의 값말고 다른 값은 필요없습니다. 추가 설명 하지 마세요!
            """
        )
        return response.output_text.strip()

    def get_intent(self):        
        response = self.client.responses.create(
            model= self.model,
            input= f"""
            {self.text}의 의도를 분석하고,
            문의 유형을
            claim, payment, cancle, general 중 하나로 알려주세요
            4개의 값 말고 다른 값은 필요없습니다. 추가 설명 하지 마세요!
            """
        )
        return response.output_text.strip()
    
    def get_urgent(self):
        response = self.client.responses.create(
            model= self.model,
            input = f"""
            {self.text}를 분석해서 긴급도를 판단하고 싶습니다.
            high, medium, low 중 하나로 알려주세요.
            3개의 값 말고 다른 값은 필요없습니다. 추가 설명 하지 마세요!
            """
        )
        return response.output_text.strip()