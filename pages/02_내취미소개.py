import streamlit as st
import pandas as pd

st.set_page_config(page_title="나의 취미 소개", page_icon="🎨", layout="wide")

st.title("🎨 나의 취미 소개")
st.write("일상 속에서 에너지를 얻고 스트레스를 해소하는 저의 소중한 취미들입니다.")

st.divider()

# 취미 데이터를 깔끔하게 표로 정리
hobbies = {
    "취미": ["📸 사진 촬영", "📚 독서 & 글쓰기", "🏃‍♂️ 러닝 / 운동", "☕ 예쁜 카페 탐방"],
    "선호도 (5점 만점)": [5, 4, 4, 5],
    "설명": ["풍경이나 일상의 순간을 기록하는 것을 좋아합니다.", "생각을 정리하고 새로운 지식을 얻는 시간입니다.", "체력을 기르고 잡생각을 비우기에 최고입니다.", "맛있는 커피와 멋진 인테리어를 즐깁니다."]
}
df = pd.DataFrame(hobbies)

st.subheader("📊 나의 취미 현황")
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### 🌲 요즘 가장 빠져있는 활동: 캠핑과 자연 탐방
    도시의 복잡함에서 벗어나 조용한 자연 속에서 불멍을 하거나 가만히 바람 소리를 듣는 것에서 큰 힐링을 얻습니다.
    """)
with col2:
    st.image("https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=500&auto=format&fit=crop&q=60", caption="Healing in Nature")
