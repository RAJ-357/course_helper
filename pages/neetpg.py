
from streamlit_card import card
import streamlit as st
import webbrowser

def main():
    st.title("NEET PG")

    st.header("About: ")
    st.video("https://www.youtube.com/watch?v=AwWffV6U-44&pp=ygUPd2hhdCBpcyBuZWV0IHBn", format="video/mp4", start_time=0)

    st.header("Top Institutions")
    col1, col2 = st.columns(2)
        
    with col1:
        si1_card = card(
        title="AAKASH",
        text="Click to view more",
        image="https://via.placeholder.com/150",
        on_click=lambda: webbrowser.open_new_tab("https://aakash.ac.in/pgplus/")
    )


    st.header("Sample Papers: ")
    st.markdown(
        "- [Question Paper 1](https://medicoholic.com/wp-content/uploads/2021/06/NEET-PG-2012-Question-Paper-With-Solutions.pdf)\n"
        "- [Question Paper 2](https://medicoholic.com/wp-content/uploads/2021/06/NEET-PG-2013-Question-Paper-With-Solutions.pdf)\n"
    )

    


    










if __name__ == '__main__':
    main()
















