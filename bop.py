import streamlit as st
import random

# --- [데이터 관리 영역] ---
# 앱이 꺼져도 데이터가 날아가지 않게 세션에 꽁꽁 숨겨두기!
if 'breakfast' not in st.session_state:
    st.session_state.breakfast = ["맥모닝", "서브웨이", "본죽", "던킨", "빵", "스프", "샐러드", "샌드위치"]
if 'lunch' not in st.session_state:
    st.session_state.lunch = [
        "버거킹", "KFC", "어쩌다농부", "혜화동 돈가스", "구내식당", "구포국수", "서브웨이", 
        "강가뼈해장국", "쌀베베", "온수반", "뚜레쥬르", "양식", "일식", "한식", "중식", 
        "베트남식", "인도식", "샌드위치", "햄버거", "피자", "짜장면", "국밥", "쌀국수", 
        "김밥", "샐러드", "순대국", "그릭요거트",'미미면가'
    ]
if 'dinner_heavy' not in st.session_state:
    st.session_state.dinner_heavy = [
        "피자", "치킨", "곱창", "마라탕", "족발", "돈가스", "불닭발", "삼겹살", "목살", 
        "소고기", "짜장면&탕수육", "쪽갈비", "제육볶음", "국밥", "아구찜", "햄버거", "마라샹궈", "훠궈", "양꼬치", "닭갈비"
    ]
if 'dinner_light' not in st.session_state:
    st.session_state.dinner_light = [
        "샐러드", "샌드위치", "포케", "회", "스시", "라멘", "라면", "만두", "쌀국수", "비빔밥"
    ]

# --- [페이지 레이아웃 정의] ---
# 전체적인 앱의 모양새 잡아주기!
st.set_page_config(page_title="결정장애 구원자", page_icon="😋", layout="centered")

# --- [디자인 & 헤더] ---
# 결정장애 친구들을 환영하는 인사말!
st.markdown('<p style="font-size:30px; font-weight:bold; color:#FF4B4B;">✨ 결정장애들을 위한 메뉴 탐험대 ✨</p>', unsafe_allow_html=True)

# 탭 나누기: 시간대별로 탭을 써서 깔끔하게 보여주기
tab1, tab2, tab3 = st.tabs(["🌅 아침", "☀️ 점심", "🌙 저녁 & 야식"])

# --- [기능 구현] ---

# 1. 아침 탭: 간단하게 추천!
with tab1:
    st.subheader("🌅 아침 메뉴")
    if st.button("아침 메뉴 추천받기! ☕"): # 버튼 정의
        pick = random.choice(st.session_state.breakfast) # 랜덤 추출
        st.success(f"활기찬 아침! 오늘은 간단하게 **{pick}** 어때요?")
        st.balloons() # 꾸미기: 당첨 풍선 날리기

# 2. 점심 탭: 충무로 밥집 리스트
with tab2:
    st.subheader("☀️ 점심 메뉴")
    if st.button("점심 메뉴 추천받기! 🍱"):
        pick = random.choice(st.session_state.lunch)
        st.info("충무로역 근처 맛집 탐방 중...") # 충무로 지역 관련 멘트 메모
        st.success(f"충무로 근처에서 찾은 오늘의 점심은 **{pick}**입니다!")
        st.balloons()

# 3. 저녁 탭: 슬라이더로 배고픔 정도 체크
with tab3:
    st.subheader("🌙 저녁 & 야식 메뉴")
    # 배고픔 단계 슬라이더(1~10): 숫자에 따라 메뉴 카테고리를 다르게 뽑음
    intensity = st.slider("배고픔 단계 (1: 가볍게, 10: 아주 든든하게)", 1, 10, 5)
    if st.button("저녁 메뉴 추천받기! 🌙"):
        if intensity <= 5: # 가벼운 메뉴 리스트
            pick = random.choice(st.session_state.dinner_light)
            st.success(f"가볍게 드시는군요! 오늘은 집에 가서 **{pick}** 드세요~ 🏠")
        else: # 무거운 메뉴 리스트
            pick = random.choice(st.session_state.dinner_heavy)
            st.warning(f"배가 많이 고프시군요! 오늘은 든든하게 **{pick}** 드세요~ 🏠")
        st.balloons()

# --- [사이드바 설정] ---
# 앱 설정 메뉴: 앱의 이름과 초기화 기능을 사이드바로 쏙!
st.sidebar.title("🛠️ 앱 설정")
st.sidebar.info("결정장애들을 위해서 만들어진 앱입니다.")
if st.sidebar.button("전체 데이터 초기화"):
    # 리스트 삭제 후 새로고침
    for key in ['breakfast', 'lunch', 'dinner_heavy', 'dinner_light']:
        del st.session_state[key]
    st.rerun()