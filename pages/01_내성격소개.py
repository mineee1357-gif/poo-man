import streamlit as st

st.set_page_config(page_title="나의 성격 소개", page_icon="🧠", layout="wide")

st.title("🧠 나의 성격 소개")
st.write("저를 가장 잘 표현하는 성격과 성향에 대한 이야기입니다.")

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    # Unsplash 가상 이미지 (본인 사진 링크가 있다면 교체 가능)
    st.image("https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?w=400&auto=format&fit=crop&q=60", caption="My Personality")

with col2:
    st.subheader("✨ 저의 MBTI는? [ ENFP / INFP ]")
    st.markdown("""
    * **공감 능력이 뛰어납니다:** 타인의 감정에 깊이 공감하고 소통하는 것을 좋아합니다.
    * **창의적이고 호기심이 많습니다:** 새로운 아이디어를 내거나 새로운 분야를 배우는 것에 두려움이 없습니다.
    * **융통성 있는 태도:** 계획에 얽매이기보다는 상황에 유연하게 대처하는 편입니다.
    """)
    
    st.subheader("💪 장점과 약점")
    tab1, tab2 = st.tabs(["장점", "보완할 점"])
    with tab1:
        st.success("긍정적인 에너지를 주변에 전달하며, 문제 해결에 있어 열린 마음으로 다양한 시각을 수용합니다.")
    with tab2:
        st.warning("가끔 생각이 너무 많아져서 결정을 내릴 때 시간이 걸리기도 합니다. 이를 보완하기 위해 우선순위를 정하는 연습을 하고 있습니다.")
