import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
conn1 = mysql.connector.connect(host="localhost", user="root", password="<PASSWORD>",database='streamlit')
CSR1=conn1.cursor()

def callback1(user,course):
    C_REC=[user,course]
    SQL_insert=("insert into users values(%s,%s)")
    CSR1.execute(SQL_insert,C_REC)
    conn1.commit()


def master_callback(user,course):
    callback1(user,course)
    switch_page("EXAMS")

st.set_page_config(
    page_title="category",
    initial_sidebar_state="collapsed",
)
st.header("Choose a category")
User1 = st.session_state["username"]
st.error(User1)
# if "category" not in st.session_state :
    # st.session_state["category"] = ""

m = st.markdown("""
<style>
div.stButton > button:first-child {
    height : 15rem;
    width : 15rem;
}
</style>""", unsafe_allow_html=True)

b1 = st.button("Student")

# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
    # height : 15 rem;
    # width : 15 rem;
# }
# </style>""", unsafe_allow_html=True)

b2 = st.button("Undergraduate")

student_card = card(
    title="Student",
    text="Click to register as a Student Page",
    image="https://via.placeholder.com/150",
    #st.error(User1)
    #on_click = master_callback(User1,"student")
)

undergraduate_card = card(
    title="Undergraduate",
    text="Click to register as an Undergraduate",
    image="https://via.placeholder.com/150",
    #st.error(User1)
    #on_click = master_callback(User1,"Undergraduate")
)


