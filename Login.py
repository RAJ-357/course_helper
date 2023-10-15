import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import mysql.connector
import sys
import st_pages as stp
sys.tracebacklimit = 0
conn1 = mysql.connector.connect(host="localhost", user="root", password="<PASSWORD>",database='streamlit')
CSR1=conn1.cursor()

if "username" not in st.session_state :
    st.session_state["username"] = ""

st.set_page_config(
    page_title="Login-Page",
    initial_sidebar_state="collapsed",
)

stp.hide_pages(["Student","jee","kcet","neet","Undergrad","Category-Selection","Engineering","Engg-courses","WEB_DEV","DSA","Engg-exams","gate","gre","books","neetpg","dashboard","AIML","APP_DEV"]);
# show_pages(
    # [
        # Page("Login.py", "Login"),
        # Page("pages/Student.py", "Student"),
        # Page("pages/Undergrad.py", "Undergrad"),
        # Page("pages/Engineering.py", "Engineering"),
    # ]
# )

st.title("Welcome to the CareerSync")
st.header("About Us")
st.write("CareerSync Portal is your go-to destination for career guidance, exam preparation, and course selection. For students and undergraduates, we're more than just a website – we're your trusted companion on the path to a bright future. Our platform provides a wealth of information on academic exams, a wide array of courses, and an innovative Book Recommender System, all aimed at helping you make informed decisions and succeed in your academic and professional pursuits. Whether you're seeking guidance on career choices, preparing for exams, or finding the perfect course to fuel your ambitions, CareerSync is here to empower you every step of the way. Your success story begins here.")
st.markdown(
        """
        ### Ready to Get Started?
        """
    )

table1 = pd.read_sql("select * from users",conn1)
User1 = st.text_input("Enter username : ")
st.session_state["username"] = User1                 

users_col = table1["UserId"].tolist()
cat_col = table1["Type_1"].tolist()

if st.button("Submit") :
    if User1 == "" :
        raise Exception("No User Logon !!!")
    elif User1 in users_col :
        #st.error("User in Database")
        index1 = users_col.index(User1)
        cat1 = cat_col[index1]
        if cat1 == "student" :
            st.session_state["category1"] = "student"
            switch_page("Student")
        else :
            st.session_state["category1"] = "Undergraduate"
            switch_page("Undergrad")
    else :
        st.error(st.session_state["username"])
        switch_page("Category-Selection")

#st.dataframe(table1, use_container_width=True)
