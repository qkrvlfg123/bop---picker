import streamlit as st
import random

# 세션 상태 초기화
if 'restaurants' not in st.session_state:
    st.session_state.restaurants = [
        "버거킹", "KFC", "어쩌다농부", "혜화동 돈가스", "가톨릭회관 구내식당", 
        "153구포국수", "서브웨이", "강가뼈해장국", "쌀베베", "온수반", "뚜레쥬르",
        "양식", "일식", "한식", "중식", "베트남식", "인도식"
    ]
if 'history' not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="운명의 밥집 탐방", page_icon="🍚", layout="wide")

# 사이드바: 입력 및 설정 위젯
with st.sidebar:
    st.header("⚙️ 설정 및 추가")
    new_item = st.text_input("새 항목 추가:")
    if st.button("목록에 추가"):
        if new_item:
            st.session_state.restaurants.append(new_item)
            st.success(f"'{new_item}' 추가됨!")
    
    st.divider()
    # 추가 위젯: 슬라이더와 셀렉트박스
    num_pick = st.slider("한 번에 뽑을 개수", 1, 3, 1)
    category_filter = st.selectbox("종류 필터링(테스트용)", ["전체", "한식", "양식"])

# 메인 화면
st.title("🍚 운명의 밥집 선택기")
st.write("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🎲 선택의 시간")
    if st.button("운명의 뽑기 실행!", type="primary"):
        if st.session_state.restaurants:
            picks = random.sample(st.session_state.restaurants, min(num_pick, len(st.session_state.restaurants)))
            st.session_state.history.append(picks) # 결과 기억하기
            st.balloons() # 풍선 효과
            st.success("결과가 나왔습니다!")
        else:
            st.error("리스트가 비어있어요.")

with col2:
    st.subheader("✨ 당첨 결과")
    if st.session_state.history:
        latest = st.session_state.history[-1]
        for item in latest:
            st.metric("당첨 항목", item)
    else:
        st.info("아직 뽑기를 하지 않았습니다.")

# 리스트 숨기기 (Expander 활용)
with st.expander("📋 현재 전체 리스트 보기 (숨겨짐)"):
    st.write(st.session_state.restaurants)

# 히스토리 보여주기
st.subheader("📜 뽑기 기록")
st.write(st.session_state.history)

if st.button("초기화"):
    st.session_state.history = []
    st.rerun()