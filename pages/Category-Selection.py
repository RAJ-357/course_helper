import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
import sys
sys.tracebacklimit = 0
conn1 = mysql.connector.connect(host="localhost", user="root", password="#MySQL123456789#",database='streamlit')
CSR1=conn1.cursor()

def callback1(user,course):
    C_REC=[user,course]
    SQL_insert=("insert into users values(%s,%s)")
    CSR1.execute(SQL_insert,C_REC)
    conn1.commit()


def master_callback(user,course):
    callback1(user,course)
    if course == "student" :
        switch_page("Student")
    else :
        switch_page("Undergrad")

st.set_page_config(
    page_title="category",
    initial_sidebar_state="collapsed",
)

if "username" not in st.session_state :
    st.session_state["username"] = ""
    #st.error(st.session_state["username"])
if "category1" not in st.session_state :
    st.session_state["category1"] = ""
User1 = st.session_state["username"]
cat1 = st.session_state["category1"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")
if cat1 != "" :
    st.error("User already logged in !!!")
    raise Exception("Sorry !!!")
st.header("Hello :- "+ User1.capitalize())
st.header("Choose a category")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    height : 15rem;
    width : 15rem;
    font-size : 30px;
}
</style>""", unsafe_allow_html=True)

col1, col2 = st.columns(2,gap = "medium")
with col1 :
    b1 = st.button("Student")
    if b1 :
        master_callback(User1,"student")
    
with col2 :
    b2 = st.button("Undergraduate")
    if b2 :
        master_callback(User1,"Undergraduate")


