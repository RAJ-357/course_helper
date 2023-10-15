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
    cosine_sim_mat = cosine_similarity(cv_mat)
    return cosine_sim_mat

def get_recommendation(title, cosine_sim_mat, df):
    course_indices = pd.Series(df.index, index=df['course_title']).drop_duplicates()
    idx = course_indices[title]
    sim_scores = list(enumerate(cosine_sim_mat[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    selected_courses_indices = [i[0] for i in sim_scores[1:]]
    selected_course_scores = [i[0] for i in sim_scores[1:]]

    result_df = df.iloc[selected_courses_indices]
    result_df['similarity_score'] = selected_course_scores
    result_df = result_df.sort_values(by='similarity_score', ascending=False)
    return result_df[['course_title', 'url', 'price']]

def search_term_if_not_contains(term, df):
    result_df = df[df['course_title'].str.contains(term)]
    return result_df

st.set_page_config(
    page_title="web-dev",
    initial_sidebar_state="collapsed",
)
stp.hide_pages(["jee","kcet","neet","Category-Selection","Engg-courses","WEB_DEV","DSA","Engg-exams","gate","gre","books","neetpg","AIML","APP_DEV"]);
if "username" not in st.session_state :
    st.session_state["username"] = ""
User1 = st.session_state["username"]
if User1 == "" :
    st.error("No User Logon !!!")
    st.success("Please go to Login Page to Login :")
    raise Exception("Sorry !!!")
st.header("Hello :- "+ User1.capitalize())

st.title("Course Recommendation System")
st.header("Premium Courses")

df = load_data("udemy_courses.csv")
cosine_sim_mat = vectorize_text_to_cosine_mat(df['course_title'])
search_term = st.text_input("Enter the course: ")

if search_term:
    try:
        result = get_recommendation(search_term, cosine_sim_mat, df)
        result = result.sort_values(by='similarity_score', ascending=False)
        result_list=[]
        for row in result.iterrows():
            rec_title=row[1][0]
            # rec_score=row[1][1]
            rec_url=row[1][2]
            rec_price=row[1][3]
            result_list.append([rec_title, rec_url, rec_price])
        st.write(result_list)

    except:
        result = "Not Found"
        result_df = search_term_if_not_contains(search_term, df)
        combined_data = {
            'Course Title': result_df['course_title'][:5],
            'URL': result_df['url'][:5]
        }
        combined_df = pd.DataFrame(combined_data)
        for idx, row in combined_df.iterrows():
            st.write((row['Course Title']), )
            st.markdown(f"({row['URL']})")

