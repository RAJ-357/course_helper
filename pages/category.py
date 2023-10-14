import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
conn1 = mysql.connector.connect(host="localhost", user="root", password="#MySQL123456789#",database='streamlit')
CSR1=conn1.cursor()

count = 0

def set_category(input1) :
    st.session_state["category"] = input1
    #return "hello"
    

st.set_page_config(
    page_title="category",
    initial_sidebar_state="collapsed",
)
st.header("Choose a category")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    height: 15rem;
    width: 15rem;
}
</style>""", unsafe_allow_html=True)

b = st.button("test")

if "category" not in st.session_state :
    st.session_state["category"] = ""

st.card("Click me to change the variable value", on_click=lambda : st.error("Clicked"))

student_card = card(
    title="Student",
    text="Click to register as a Student Page",
    image="https://via.placeholder.com/150",
    on_click = set_category("student")
)

undergraduate_card = card(
    title="Undergraduate",
    text="Click to register as an Undergraduate",
    image="https://via.placeholder.com/150",
    on_click = set_category("Undergraduate")
)

if st.button("Submit") :
    if st.session_state["category"] == "student" :
        st.error("student")
        
    else :
        st.error(st.session_state["username"])
        switch_page("Undergraduate")