from streamlit_card import card
import streamlit as st

def main():
    st.set_page_config(
    page_title="STREAMS",
    initial_sidebar_state="collapsed",
)
    st.header("exams to be cleared")

    student_card1 = card(
        title="ENGINEERING",
        text="Click to view Student Page",
        image="https://via.placeholder.com/150",
        on_click=lambda: print("Clicked!")
    )

    student_card2 = card(
        title="MBBS",
        text="Click to view Undergraduate Page",
        image="https://via.placeholder.com/150",
        on_click=lambda: print("Clicked!")
    )

if __name__ == '__main__':
    main()
