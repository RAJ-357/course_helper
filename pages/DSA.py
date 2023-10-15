import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys
import st_pages as stp
sys.tracebacklimit = 0
from streamlit_card import card

# Load the dataset
data = pd.read_csv("youtube_data1.csv")

# Use TF-IDF vectorization for channel names
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['Channel Name'])

# Calculate cosine similarity between channel names
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(channel_name):
    # Find the index of the input channel name
    channel_index = data[data['Channel Name'] == channel_name].index[0]
    
    # Calculate the similarity scores for all channels
    similarity_scores = list(enumerate(cosine_sim[channel_index]))
    
    # Sort channels by cosine similarity
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 5 most similar channels (excluding the input channel)
    top_similar_channels = similarity_scores[1:6]
    
    # Find the details of the top similar channels, including URL and Video Duration
    similar_channels_details = []
    for i in top_similar_channels:
        index = i[0]
        similar_channel_name = data['Channel Name'][index]
        similar_channel_url = data['Playlist URL'][index]
        similar_channel_duration = data['Video Count'][index]
        similar_channels_details.append((similar_channel_name, similar_channel_url, similar_channel_duration))
    
    return similar_channels_details

st.set_page_config(
    page_title="dsa",
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

# Streamlit UI
st.title("YouTube Playlist Recommender")
st.write("Find similar YouTube channels based on your preferred channel.")

input_channel = st.text_input("Enter your preferred channel:", "CodeWithHarry")
if st.button('Recommend'):
    recommendations = recommend(input_channel)
    st.write(f"Recommended Channels for {input_channel}:")
    for i, (channel_name, channel_url, channel_duration) in enumerate(recommendations):
        st.write(f"{i+1}. Channel Name: {channel_name}")
        st.write(f"   Playlist URL: {channel_url}")
        st.write(f"   Video Duration: {channel_duration} minutes")
