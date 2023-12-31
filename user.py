import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
conn1 = mysql.connector.connect(host="localhost", user="root", password="#MySQL123456789#",database='streamlit')
CSR1=conn1.cursor()

if "username" not in st.session_state :
    st.session_state["username"] = ""

st.set_page_config(
    page_title="Login-Page",
    initial_sidebar_state="collapsed",
)

table1 = pd.read_sql("select * from users",conn1)
User1 = st.text_input("Enter username : ")
st.session_state["username"] = User1

users_col = table1["UserId"].tolist()
cat_col = table1["Type_1"].tolist()
# index1 = users_col.index('User1')

if st.button("Submit") :
    if User1 in users_col :
        st.error("User in Database")
        index1 = users_col.index(User1)
        cat1 = cat_col[index1]
        if cat1 == "student" :
            switch_page("EXAMS")
        else :
            switch_page("under_grad")
        
    else :
        st.error(st.session_state["username"])
        switch_page("category")

st.dataframe(table1, use_container_width=True)