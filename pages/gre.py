from streamlit_extras.switch_page_button import switch_page
import sys
sys.tracebacklimit = 0
from streamlit_card import card
import streamlit as st
import webbrowser
st.set_page_config(
    page_title="gre",
    initial_sidebar_state="collapsed",
)

if "username" not in st.session_state :
    st.session_state["username"] = ""
User1 = st.session_state["username"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")
st.header("Hello :- "+ User1.capitalize())

st.title("GRE")

st.header("About: ")
st.video("https://www.youtube.com/watch?v=k6JPVzekzbI", format="video/mp4", start_time=0)

st.header("Top Institutions")
col1, col2 = st.columns(2)

with col1:
    si1_card = card(
    title="Mahattan",
    text="Click to view more",
    image="https://via.placeholder.com/150",
    on_click=lambda: webbrowser.open_new_tab("https://www.manhattanreview.com/gre/")

)
    
with col2:
    si1_card = card(
    title="TIME",
    text="Click to view more",
    image="https://via.placeholder.com/150",
    on_click=lambda: webbrowser.open_new_tab("https://www.time4education.com/GRE/")
)


st.header("Sample Papers: ")
st.markdown(
    "- [Question Paper 1](https://www.aceenggacademy.com/wp-content/uploads/2023/04/GATE-CS-2022-Question-Paper.pdf)\n"
    "- [Question Paper 2](https://www.aceenggacademy.com/wp-content/uploads/2023/04/GATE-CS-2021Question-Paper.pdf)\n"

)
