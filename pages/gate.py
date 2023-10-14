
from streamlit_card import card
import streamlit as st
import webbrowser

def main():
    st.title("GATE")

    st.header("About: ")
    st.video("https://www.youtube.com/watch?v=U1N6PDrChHE&pp=ygUMd2hhdCBpcyBnYXRl", format="video/mp4", start_time=0)

    st.header("Top Institutions")
    col1, col2 = st.columns(2)

    with col1:
        si1_card = card(
        title="T.I.M.E",
        text="Click to view more",
        image="https://via.placeholder.com/150",
        on_click=lambda: webbrowser.open_new_tab("https://www.time4education.com/GATE")

    )
        
    with col2:
        si1_card = card(
        title="ACEEA",
        text="Click to view more",
        image="https://via.placeholder.com/150",
        on_click=lambda: webbrowser.open_new_tab("https://www.time4education.com/GATE")
    )


    st.header("Sample Papers: ")
    st.markdown(
        "- [Question Paper 1](https://www.aceenggacademy.com/wp-content/uploads/2023/04/GATE-CS-2022-Question-Paper.pdf)\n"
        "- [Question Paper 2](https://www.aceenggacademy.com/wp-content/uploads/2023/04/GATE-CS-2021Question-Paper.pdf)\n"

    )

    


    










if __name__ == '__main__':
    main()
















