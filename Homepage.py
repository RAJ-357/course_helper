import streamlit as st
from streamlit_card import card
import streamlit_extras
# import streamlit_patches as st
# from streamlit_extras.badges import badge
# from streamlit_extras.function_explorer import function_explorer
# from streamlit_extras.mention import mention
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Courses",
    initial_sidebar_state="collapsed",
)

st.title("Select Type :")
#st.sidebar.success("Select a page above.")

if "type" not in st.session_state:
    st.session_state["type"] = ""

engg1 = card(
  title="Engineering",
  text="Click",
  on_click=lambda: switch_page("Select-Courses")
  #image="http://placekitten.com/200/300",
)

if engg1 :
    st.session_state["type"] = "Engg"
    switch_page("Select-Courses")

med1 = card(
  title="Medical",
  text="Click",
  #image="http://placekitten.com/200/300",
)

if med1 :
    st.session_state["type"] = "Med"
    switch_page("Select-Courses")
    