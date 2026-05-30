from keywords import Keywords

keywords = Keywords()

def analyze_sentiment(text: str) -> str:
    return keywords.get_emotion(text)
    
def classify_intent(text: str) -> str:
    return keywords.get_intent(text)

