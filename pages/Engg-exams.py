from streamlit_card import card
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys
sys.tracebacklimit = 0

st.set_page_config(
    page_title="eng_exams",
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

m = st.markdown("""
<style>
div.stButton > button:first-child {
    height : 15rem;
    width : 15rem;
    font-size : 30px;
}
</style>""", unsafe_allow_html=True)

col1, col2= st.columns(2,gap = "medium")
with col1 :
    b1 = st.button("GATE")
    if b1 :
        switch_page("gate")
    
with col2 :
    b2 = st.button("GRE")
    if b2 :
        switch_page("gre")
