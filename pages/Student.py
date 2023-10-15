import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
import sys
import st_pages as stp
sys.tracebacklimit = 0
conn1 = mysql.connector.connect(host="localhost", user="root", password="<PASSWORD>",database='streamlit')
CSR1=conn1.cursor()


st.set_page_config(
    page_title="EXAMS",
    initial_sidebar_state="collapsed",
)

stp.hide_pages(["jee","kcet","neet","Category-Selection","Engineering","Engg-courses","WEB_DEV","DSA","Engg-exams","gate","gre","books","neetpg","AIML","APP_DEV"]);

if "username" not in st.session_state :
    st.session_state["username"] = ""

User1 = st.session_state["username"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")

st.header("Hello :- "+ User1.capitalize())
st.header("exams to be cleared")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    height : 15rem;
    width : 15rem;
    font-size : 30px;
}
</style>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3,gap = "medium")
with col1 :
    b1 = st.button("JEE")
    if b1 :
        switch_page("jee")
    
with col2 :
    b2 = st.button("KCET")
    if b2 :
        switch_page("kcet")

with col3 :
    b3 = st.button("NEET")
    if b3 :
        switch_page("neet")
