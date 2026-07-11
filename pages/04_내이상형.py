import streamlit as st

st.set_page_config(page_title="나의 이상형 소개", page_icon="💖", layout="wide")

st.title("💖 나의 이상형 소개")
st.write("제가 소중하게 생각하는 가치관과 매력을 느끼는 이상형에 대한 소개입니다.")

st.divider()

st.subheader("📌 제가 중요하게 생각하는 3가지 키워드")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="키워드 1", value="대화와 소통")
    st.write("사소한 이야기부터 깊은 고민까지 편안하게 대화가 통하는 사람이 좋습니다. 서로의 의견을 존중해주는 태도가 중요해요.")

with col2:
    st.metric(label="키워드 2", value="긍정적인 마인드")
    st.write("힘든 상황 속에서도 함께 웃을 수 있는 긍정적인 에너지를 가진 사람에게 매력을 느낍니다.")

with col3:
    st.metric(label="키워드 3", value="배울 점이 있는 사람")
    st.write("자신의 일에 열정을 가지고 노력하며, 서로에게 좋은 자극을 줄 수 있는 건강한 가치관을 가진 사람이 이상형입니다.")

st.divider()

st.subheader("💌 한 줄 요약")
st.info("“함께 있을 때 가장 나다운 모습이 될 수 있고, 서로를 더 좋은 사람이 되고 싶게 만드는 따뜻한 사람”")
