import i18n
import streamlit as st

from utils.init import init_once


import streamlit as st

def create_home_page():
    st.set_page_config(page_title="헬스 트레이너 매칭 서비스", layout="wide")
    st.title("헬스 트레이너 매칭 서비스에 오신 것을 환영합니다!")

    st.write("""
    전문화된 매칭 시스템을 통해 완벽한 트레이닝 파트너를 찾아보세요.
    프로필을 둘러보고, 리뷰를 읽고, 모든 것을 한 곳에서 세션을 예약하세요.
    """)





# 앱 시작 시 실행할 함수 결정
if 'navigate_to' in st.session_state and st.session_state['navigate_to'] == 'search_your_trainer':
    search_your_trainer()  # 트레이너 검색 페이지로 이동
else:
    create_home_page()  # 기본 홈 페이지를 먼저 보여줌
