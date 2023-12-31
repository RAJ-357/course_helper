import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
conn1 = mysql.connector.connect(host="localhost", user="root", password="<PASSWORD>",database='streamlit')
CSR1=conn1.cursor()


User1 = st.session_state["username"]

st.set_page_config(
    page_title="EXAMS",
    initial_sidebar_state="collapsed",
)

st.header("Hello : ",User1)
st.header("exams to be cleared")

student_card1 = card(
    title="JEE",
    text="Click to view JEE details",
    image="https://via.placeholder.com/150",
    on_click=lambda: print("Clicked!")
)

student_card2 = card(
    title="KCET",
    text="Click to view KECET details",
    image="https://via.placeholder.com/150",
    on_click=lambda: print("Clicked!")
    )

student_card3 = card(
        title="NEET",
        text="Click to view NEET details",
        image="https://via.placeholder.com/150",
        on_click=lambda: print("Clicked!")
)
