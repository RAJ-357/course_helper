import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys
import st_pages as stp
sys.tracebacklimit = 0
from streamlit_card import card

def load_data(data):
    df = pd.read_csv(data)
    return df

def vectorize_text_to_cosine_mat(data):
    count_vect = CountVectorizer()
    cv_mat = count_vect.fit_transform(data)
    # Get cosine
    cosine_sim_mat = cosine_similarity(cv_mat)
    return cosine_sim_mat

def get_recommendation(title, cosine_sim_mat, df):
    # indices of the course
    course_indices = pd.Series(df.index, index=df['Book_title']).drop_duplicates()
    idx = course_indices[title]
    # look in cosine
    sim_scores = list(enumerate(cosine_sim_mat[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    selected_courses_indices = [i[0] for i in sim_scores[1:]]
    selected_course_scores = [i[1] for i in sim_scores[1:]]

    result_df = df.iloc[selected_courses_indices]
    result_df['similarity_score'] = selected_course_scores
    return result_df[['Book_title', 'similarity_score', 'Description', 'Price']]

def search_term_if_not_contains(term, df):
    result_df = df[df['Book_title'].str.contains(term, case=False, regex=False)]
    return result_df

st.set_page_config(
    page_title="books",
    initial_sidebar_state="collapsed",
)
stp.hide_pages(["jee","kcet","neet","Category-Selection","Engg-courses","WEB_DEV","Engg-exams","gate","gre","books","neetpg","DSA","AIML","APP_DEV"]);
if "username" not in st.session_state :
    st.session_state["username"] = ""
User1 = st.session_state["username"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")
st.header("Hello :- "+ User1.capitalize())

st.title("Book Recommendation System")

df = load_data("prog_book.csv")
cosine_sim_mat = vectorize_text_to_cosine_mat(df['Book_title'])

search_term = st.text_input("Enter the book title:")

if st.button("Get Recommendations"):
    if search_term:
        try:
            result = get_recommendation(search_term, cosine_sim_mat, df)
            st.table(result)
        except:
            result_df = search_term_if_not_contains(search_term, df)
            st.table(result_df[['Book_title', 'Description', 'Price']])
    else:
        st.warning("Please enter a book title.")
