from keywords import Keywords
import streamlit as st

keywords = Keywords()

st.set_page_config(page_title="보험사 AI 상담 분석 앱", page_icon="💬", layout="wide")

def analyze_sentiment(text: str) -> str:
    return keywords.get_emotion(text)
    
def classify_intent(text: str) -> str:
    return keywords.get_intent(text)

def detect_urgent(text: str) -> str:
    return keywords.get_urgent(text)

def make_guide(sentiment: str, intent: str, urgent: str) -> str:
    st.title("보험사 AI 상담 분석 앱")
    st.write("고객 상담 내용을 입력하면 감정 / 문의 유형 / 긴급도를 분석 합니다.")
    
left, right = st.columns([2,1])
    
with left:
    st.subheader("상담 입력")
    user_text = st.text_area(
        "고객 상담 문장을 입력하세요",
        placeholder = "예: 보험금을 청구 했는데 아직 입금이 되지 않았고, 너무 답답합니다.",
        height= 180
    )
    run_btn = st.button("상담 분석하기", use_container_width= True)
    
with right:
    st.subheader("분석 기록")
    if "history" not in st.session_state:
        st.session_state.history = []
    if st.button("기록 초기화", use_container_width=True):
        st.session_state.history = []
        st.rerun()        
    
st.divider()


