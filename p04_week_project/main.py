from keywords import Keywords
import streamlit as st
from datetime import datetime
import pandas as pd

keywords = Keywords()

st.set_page_config(page_title="보험사 AI 상담 분석 앱", page_icon="💬", layout="wide")

def analyze_sentiment(text: str) -> str:
    return keywords.get_emotion(text)
    
def classify_intent(text: str) -> str:
    return keywords.get_intent(text)

def detect_urgent(text: str) -> str:
    return keywords.get_urgent(text)

def make_guide(sentiment: str, intent: str, urgent: str) -> str:
    if intent == "claim":
        guide = "청구 진행 상태와 필요 서류를 먼저 확인하고 예상 처리 일정을 안내하세요"
    elif intent == "payment":
        guide = "납입 내역과 자동이체 기록을 확인하고 중복 출금 여부를 검토하세요"
    elif intent == "cancel":
        guide = "해지 및 환급 규정을 명확히 설명하고 손해가 없도록 주의 사항을 안내하세요"
    else:
        guide = "문의 내용을 다시 확인하고 필요한 추가 정보를 요청하세요"
    
    if sentiment == "negative":
        guide = "불편을 드려 죄송합니다 " + guide
    elif sentiment == "positive":
        guide = "문의 주셔서 감사합니다 " + guide
    
    if urgent == "high":
        guide = "긴급도가 높으므로 진상일 수 있습니다. " + guide
    elif urgent == "medium":    
        guide = "어조에 신경써주세요. 그에 따라 달라집니다." + guide
    else: guide = "문의주셔서 감사합니다. " + guide
    
    return guide
    
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

if run_btn:
    if not user_text.strip():
        st.error("상담 내용을 입력하세요.")
    else:
        with st.spinner("AI가 상담 내용을 분석하고 있습니다..."):
            sentiment = analyze_sentiment(user_text)
            intent = classify_intent(user_text)
            urgent = detect_urgent(user_text)
            guide = make_guide(sentiment, intent, urgent)
            
            if sentiment == "negative":
                st.warning(f"감정 : {sentiment}")
            elif sentiment == "positive":
                st.success(f"감정 : {sentiment}")
            else: st.info(f"감정 : {sentiment}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("문의 유형", intent)
            c2.metric("긴급 여부", urgent)
            c3.metric("입력 길이", len(user_text))
            
            st.subheader("응대 가이드")
            st.write(guide)

            st.session_state.history.append({
                "time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "text" : user_text,
                "sentiment" : sentiment,
                "intent" : intent,
                "urgent" : urgent
            })
else:
    st.info("상담 내용을 입력하고 버튼을 눌러보세요!")
    
st.divider()

st.subheader("최근 기록")
if st.session_state.history:
    for index, item in enumerate(reversed(st.session_state.history[-5:]), start= 1):
        st.write(
            f"{index}, [{item['time']}] : [{item['intent']}]"
            f"{item['sentiment']} / {item['urgent']} / {item['text']}"
        )
    st.divider()
    st.subheader("상담 이력 표")
    st.dataframe(pd.DataFrame(st.session_state.history), use_container_width= True)
else: st.caption("아직 기록이 없습니다.")

st.divider()
st.subheader("상담 시간대별 통계")
if st.session_state.history:    
    df = pd.DataFrame(st.session_state.history)
    df["time"] = pd.to_datetime(df["time"])
    df["hour"] = df["time"].dt.hour
    count = df["hour"].value_counts().sort_index()
    st.bar_chart(count)    
else: st.caption("아직 기록이 없습니다.")

