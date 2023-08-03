import streamlit as st
from fuzzywuzzy import fuzz
import json

st.set_page_config(
    page_title="Algorithm to Python | DevTunisian",
    page_icon=":computer:",
    layout="centered"
)

if 'visits' not in st.session_state:
    st.session_state['visits'] = 0

st.session_state['visits'] += 1
user = st.session_state['visits']
st.title("Welcome To Algorithm.ai")
p="""The website "Welcome To Algorithm.ai" is a platform that introduces users to the world of algorithms and artificial intelligence. The website aims to provide comprehensive and beginner-friendly information on algorithms, data structures, and AI concepts."""
st.write(p)

# Load the JSON data
with open("algo.json", "r") as f:
    algorithm_data = json.load(f)
initial = "ecrire"
# Algorithm
user_input = st.text_input("Algorithm : ", initial)

# Function to find the closest matching words
def find_closest_word(user_input, algorithm_data):
    max_similarity = 0
    closest_word = None

    for word in algorithm_data["Algorithms"]:
        similarity = fuzz.ratio(user_input.lower(), word.lower())
        if similarity > max_similarity:
            closest_word = word
            max_similarity = similarity

    return closest_word, max_similarity

# Check if user input matches any algorithm key exactly
if user_input in algorithm_data["Algorithms"]:
    st.code(algorithm_data["Algorithms"][user_input])
else:
    # Find the closest matching word
    closest_word, similarity_score = find_closest_word(user_input, algorithm_data)
    if closest_word and similarity_score > 60:  # Set a threshold for similarity score
        st.info(f"Did you mean '{closest_word}'? (Similarity: {similarity_score}%)")
        st.code(algorithm_data["Algorithms"][closest_word])
    else:
        st.warning("Algorithm not found. Please try a different input.")
st.markdown("[learn Qt Designer](#soon)")
st.write("---")
col1,col2 = st.columns([2,5])
with col2 :
    st.write(f" users who used web : {user}")
    st.write(":copyright:2023 by Algorithm.ai | DevTunisian")

col4,col3 = st.columns([3,7])
c1,c2 = st.columns([5,8])
with col3 :
    st.write("Follow us on our social medias:")
    with c2:
        st.markdown("[Facebook](https://www.facebook.com/groups/6772196932792430)")
    with c2:
        st.markdown("[Instagram](https://www.instagram.com/jasserabedrazzek/)")
    with c2:
        st.markdown("[Discord](https://discord.gg/HFtfNdFv)")
    with c2:
        st.markdown("[DevTunisian Web](https://devtunisian.netlify.app/)")

