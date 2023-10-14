
from streamlit_card import card
import streamlit as st
import webbrowser

def main():
    st.title("KCET")

    st.header("About: ")
    st.video("https://youtu.be/lmiMyMQrlSI?si=zJtNacsOYQV3U5JW", format="video/mp4", start_time=0)

    st.header("Top Institutions")
    col1, col2 = st.columns(2)

    with col1:
        si1_card = card(
        title="ALLEN",
        text="Click to view more",
        image="https://via.placeholder.com/150",
        on_click=lambda: webbrowser.open_new_tab("https://www.allen.ac.in/kota/iit-jee-main-Advanced-coaching.asp?year=2023-24")

    )
        
    with col2:
        si1_card = card(
        title="AAKASH",
        text="Click to view more",
        image="https://via.placeholder.com/150",
        on_click=lambda: webbrowser.open_new_tab("https://www.aakash.ac.in/")
    )


    st.header("Sample Papers: ")
    st.markdown(
        "- [Question Paper 1](JEE-Advanced-2020-Sample-Paper-1-Mock-Test-Nurture.pdf (allen.ac.in))\n"
        "- [Question Paper 2](https://example.com/question_paper_2)\n"
        "- [Question Paper 3](https://example.com/question_paper_3)\n"
    )

    


    










if __name__ == '__main__':
    main()
















