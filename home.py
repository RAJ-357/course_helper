import streamlit as st

# Define the navigation bar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Page 1", "Page 2"])

# Create content for each page
if page == "Home":
    st.title("Welcome to the CareerSync")
    st.header("About Us")
    st.write("CareerSync Portal is your go-to destination for career guidance, exam preparation, and course selection. For students and undergraduates, we're more than just a website – we're your trusted companion on the path to a bright future. Our platform provides a wealth of information on academic exams, a wide array of courses, and an innovative Book Recommender System, all aimed at helping you make informed decisions and succeed in your academic and professional pursuits. Whether you're seeking guidance on career choices, preparing for exams, or finding the perfect course to fuel your ambitions, CareerSync is here to empower you every step of the way. Your success story begins here.")

elif page == "Page 1":
    st.title("Page 1")
    st.write("This is Page 1 content.")

elif page == "Page 2":
    st.title("Page 2")
    st.write("This is Page 2 content.")


st.text("")
st.text("")
col1, col2, col3, _ = st.columns([0.25, 1, 0.25, 0.25])
with col1:
    st.text(" ")
with col2:
    st.markdown(
        """
        ### Ready to Get Started?
        """
    )

    button_style = """
    <style>
    .st-eb {
        font-size: 50px;
        padding: 50px 100px;
        background-color: #FF5733;
        color: white;
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)
    st.button("Get Started", key="get_started_button")

with col3:
    st.text(" ")

