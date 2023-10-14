
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


if __name__ == '__main__':
    main()
















