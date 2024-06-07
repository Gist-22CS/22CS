import streamlit as st
import pandas as pd

# 간단한 데이터 생성
data1 = {
    '지역번호': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
    '지역이름': ["건국동", "계림1동", "계림2동", "광천동", "금호1동", "금호2동", "농성1동", "농성2동", "대촌동", "도산동", "동곡동", "동림동", "동명동", "동천동", "두암1동", "두암2동", "두암3동", "매곡동", "문화동", "문흥1동", "문흥2동", "방림1동", "방림2동", "백운1동", "백운2동", "본량동", "봉선1동", "봉선2동", "비아동", "사직동", "산수1동", "산수2동", "삼각동", "삼도동", "상무1동", "상무2동", "서남동", "서창동", "석곡동", "송암동", "송정1동", "송정2동", "수완동", "신가동", "신안동", "신용동", "신창동", "신흥동", "양3동", "양동", "양림동", "어룡동", "오치1동", "오치2동", "용봉동", "우산동(광산구)", "우산동(북구)", "운남동", "운암1동", "운암2동", "운암3동", "월곡1동", "월곡2동", "월산4동", "월산5동", "월산동", "유덕동", "일곡동", "임곡동", "임동", "주월1동", "주월2동", "중앙동", "중흥1동", "중흥동", "지산1동", "지산2동", "지원1동", "지원2동", "진월동", "첨단1동", "첨단2동", "충장동", "치평동", "평동", "풍암동", "풍향동", "하남동", "학동", "학운동", "화정1동", "화정2동", "화정3동", "화정4동", "효덕동"]
}
data2 = {
    '관심운동 번호': [1,2,3,4],
    '관심운동': ["상체", "하체", "유산소", "다이어트 및 취미"]
}

# 데이터프레임 생성
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Streamlit 페이지 제목 설정
st.title('회원가입 주의사항')

#age info
st.write('-나이는 1부터 99의 범위 내에서 입력해야 합니다')

#interest info
st.write('-관심분야의 범위는 1부터 4이고 해당 번호는 아래 표와 같습니다.')
st.subheader('관심분야 번호에 대한 table')
st.table(df2.assign(hack='').set_index('hack'))

#region info
st.write('-지역의 범위는 1부터 95이고 해당 번호는 아래 표와 같습니다.')
st.subheader('지역 번호에 대한 table')
st.table(df1.assign(hack='').set_index('hack'))
