from streamlit_extras.switch_page_button import switch_page
import sys
sys.tracebacklimit = 0
from streamlit_card import card
import streamlit as st
import webbrowser
import st_pages as stp

st.set_page_config(
    page_title="gate",
    initial_sidebar_state="collapsed",
)
stp.hide_pages(["jee","kcet","neet","Category-Selection","DSA","Engg-courses","WEB_DEV","Engg-exams","gate","gre","books","neetpg","AIML","APP_DEV"]);
if "username" not in st.session_state :
    st.session_state["username"] = ""
User1 = st.session_state["username"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")
st.header("Hello :- "+ User1.capitalize())

st.title("GATE")

st.header("About: ")
st.video("https://www.youtube.com/watch?v=U1N6PDrChHE&pp=ygUMd2hhdCBpcyBnYXRl", format="video/mp4", start_time=0)

st.header("Top Institutions")
col1, col2 = st.columns(2,gap = "medium")

with col1:
    si1_card = card(
    title="T.I.M.E",
    text="Click to view more",
    image="https://via.placeholder.com/150",
    on_click=lambda: webbrowser.open_new_tab("https://www.time4education.com/GATE")
)
    
with col2:
    si1_card = card(
    title="ACEEA",
    text="Click to view more",
    image="https://via.placeholder.com/150",
    on_click=lambda: webbrowser.open_new_tab("https://www.time4education.com/GATE")
)

st.header("Sample Papers: ")
st.markdown(
    "- [Question Paper 1](https://www.aceenggacademy.com/wp-content/uploads/2023/04/GATE-CS-2022-Question-Paper.pdf)\n"
    "- [Question Paper 2](https://www.aceenggacademy.com/wp-content/uploads/2023/04/GATE-CS-2021Question-Paper.pdf)\n"

)
