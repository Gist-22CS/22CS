import os
import streamlit as st
import pages
from utils.page import PageModel
from utils.init import init_once

# 초기 설정
settings = init_once()

# 메타데이터 구성
name = os.path.basename(__file__)[:-3]
model = PageModel(settings=settings, input=name, function=name, output_type='pydantic')

# 임시 데이터
trainers = [
    {"name": "정우진", "region": "광주과학기술원", "sessions": 10, "price": "5,000원", "tags": ["#다이어트전문", "#다이짐용사"]},
    {"name": "양은규", "region": "광주과학기술원", "sessions": 10, "price": "4,000원", "tags": ["#헬스대회", "#4년트레이닝"]},
    {"name": "양승민", "region": "광주과학기술원", "sessions": 10, "price": "3,000원", "tags": ["#피트니스모델", "#셀럽트레이너"]},
    {"name": "최민", "region": "광주과학기술원", "sessions": 15, "price": "9,000원", "tags": ["#여성전문", "#바디프로필"]}
]

# 페이지 그리기
def render(model):
    st.title('트레이너 추천')
    
    if 'selected_trainer' not in st.session_state:
        st.session_state.selected_trainer = None

    for trainer in trainers:
        with st.container():
            col1, col2 = st.columns([1, 3], gap="small")
            with col1:
                st.image('https://via.placeholder.com/150', width=100)  # 임시 이미지
            with col2:
                if st.button(f"{trainer['name']} ({trainer['region']})", key=trainer['name']):
                    st.session_state.selected_trainer = trainer

    if st.session_state.selected_trainer:
        trainer = st.session_state.selected_trainer
        st.write("———")
        st.subheader(f"{trainer['name']}의 자세한 프로필:")
        st.write(f"경력: {trainer['region']}")
        st.write(f"세션 수: {trainer['sessions']}")
        st.write(f"가격: {trainer['price']}")
        st.write(' '.join(trainer['tags']))

# 페이지 렌더링
if __name__ == '__main__':
    render(model)

