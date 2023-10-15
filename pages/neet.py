from streamlit_extras.switch_page_button import switch_page
import sys
sys.tracebacklimit = 0
from streamlit_card import card
import streamlit as st
import webbrowser
import st_pages as stp
st.set_page_config(
    page_title="neet",
    initial_sidebar_state="collapsed",
)
stp.hide_pages(["jee","kcet","neet","Category-Selection","Engineering","DSA","Engg-courses","WEB_DEV","Engg-exams","gate","gre","books","neetpg","AIML","APP_DEV"]);
if "username" not in st.session_state :
    st.session_state["username"] = ""
    
User1 = st.session_state["username"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")
st.header("Hello :- "+ User1.capitalize())

st.title("NEET PG")

st.header("About: ")
st.video("https://www.youtube.com/watch?v=AwWffV6U-44&pp=ygUPd2hhdCBpcyBuZWV0IHBn", format="video/mp4", start_time=0)

st.header("Top Institutions")
col1, col2 = st.columns(2,gap = "medium")
    
with col1:
    si1_card = card(
    title="AAKASH",
    text="Click to view more",
    image="https://via.placeholder.com/150",
    on_click=lambda: webbrowser.open_new_tab("https://www.aakash.ac.in/classroom-courses?search_api_fulltext=&field_product_stream=15&field_product_classes=23&field_notification_select_stream=116&field_centers=2072&center_list_dropdown=2072")
)
    
with col2:
    si1_card = card(
    title="ALLEN",
    text="Click to view more",
    image="https://via.placeholder.com/150",
    on_click=lambda: webbrowser.open_new_tab("https://www.allen.ac.in/kota/neet-ug-aiims-coaching.asp?year=2023-24")
)

st.header("Sample Papers: ")
st.markdown(
    "- [Question Paper 1](https://medicine.careers360.com/download/sample-papers)\n"
)

