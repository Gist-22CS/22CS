import os
import requests

import pages
from utils.page import PageModel
from utils.init import init_once

import streamlit as st
import sqlalchemy

# DB 연결 설정 
# engine = sqlalchemy.create_engine('sqlite:///trainers.db')

# 페이지 설정
st.set_page_config(page_title="Trainer Management", layout="wide")

# 입력 폼
with st.form("trainer_form"):
    st.write("trainer registraion and recommendation")
    name = st.text_input("name")
    region = st.number_input("region",step=1)
    age = st.number_input("age",step=1)
    interest = st.number_input("interest",step=1)
    submitted = st.form_submit_button("save")
    if submitted:
        # 여기에 데이터베이스 저장 로직을 추가하세요.
        url = 'http://backend:8000/func/PT_recommender'
        payload = {
            "name": name,
            "region": region,
            "age": age,
            "interest": interest
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"{name} complete!")
            st.write("Recommendation result:")
            st.write("1st recommend: {}".format(result["output1"]))
            st.write("2nd recommend: {}".format(result["output2"]))
            st.write("3rd recommend: {}".format(result["output3"]))

        else:
            st.error("Failed to submit data. Check notice for register.")


# DB에서 트레이너 정보 읽기 (미구현: DB 구축 후 구현 예정)
# with engine.connect() as connection:
#     trainers = connection.execute(sqlalchemy.text("SELECT * FROM trainers")).fetchall()
#     for trainer in trainers:
#         st.write(f"{trainer.name} - {trainer.region}")

# 입력된 정보 확인용 임시 출력
if submitted:
    st.write("trainer information")
    st.write("name:", name)
    st.write("age:", age)
    st.write("region:", region)
    st.write("interest:", interest)
