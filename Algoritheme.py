import streamlit as st
from fuzzywuzzy import fuzz
import json
from random import randint
from numpy import array
from math import sqrt

st.set_page_config(
    page_title="Algorithm to Python | DevTunisian",
    page_icon=":computer:",
    layout="centered"
)

if 'visits' not in st.session_state:
    st.session_state['visits'] = 0

st.session_state['visits'] += 1
user = st.session_state['visits']

            # Add other widgets or content here
st.title("Welcome To Algorithm.ai")
p = """The website "Algorithm.ai" is a platform that introduces users to the world of algorithms and artificial intelligence. The website aims to provide comprehensive and beginner-friendly information on algorithms, data structures, and AI concepts."""
st.write(p)
st.write("---")
# Load the JSON data
with open("algo.json", "r") as f:
    algorithm_data = json.load(f)
with open("algo_def.json", "r") as file:
    definition = json.load(file)
initial = "ecrire()"


# Function to find the closest matching words
def find_closest_word(user_input, algorithm_data):
    if user_input :
        max_similarity = 0
        closest_word = None

        for word in algorithm_data["Algorithms"]:
            similarity = fuzz.ratio(user_input.lower(), word.lower())
            if similarity > max_similarity:
                closest_word = word
                max_similarity = similarity
    

        return closest_word, max_similarity
    else:
        closest_word = initial
        max_similarity = 100
        return closest_word, max_similarity


# Function to get examples
def get_example(user_input, definition):
    if user_input:
        max_similarity_exe = 0
        closest_word_exe = None

        for word2 in definition["Algorithms_exe"]:
            similarity = fuzz.ratio(user_input.lower(), word2.lower())
            if similarity > max_similarity_exe:
                closest_word_exe = word2
                max_similarity_exe = similarity
    

        return closest_word_exe, max_similarity_exe
    else:
        closest_word_exe = initial
        max_similarity_exe = 100
        return closest_word_exe, max_similarity_exe

def algortitheme():
        user_input = st.chat_input("algorithm :")
    
    # Check if user input matches any algorithm key exactly
        if user_input in algorithm_data["Algorithms"] and user_input in definition["Algorithms_exe"]:
            st.code(algorithm_data["Algorithms"][user_input])
            st.write("Example:")
            st.code(definition["Algorithms_exe"][user_input])
            

        else:
            # Find the closest matching word
            closest_word, similarity_score = find_closest_word(user_input, algorithm_data)
            closest_word_exe, max_similarity_exe = get_example(user_input, definition)
            if closest_word and similarity_score or closest_word_exe and max_similarity_exe > 60 :  
                st.info(f"Did you mean '{closest_word}'?")
                st.code(algorithm_data["Algorithms"][closest_word])
                st.code(definition["Algorithms_exe"][closest_word_exe])
                
            
            else:
                st.warning("Algorithm not found. Please try a different input.")
    
def main():
    # Algorithm
    
    algortitheme()
    st.sidebar.write("New version")
    st.sidebar.write("added : tableau avec sous programme")
    st.sidebar.write("added : boucle pour")
    st.sidebar.write("added : sous programme")
    
        
    
    st.sidebar.markdown("[Learn Qt Designer](#soon)")
    st.write("Free Research Preview. [Algorithm.ai August 6 Version](#).")
    st.write("---")
    col1, col2 = st.columns([2, 5])
    with col2:

        st.write(":copyright:2023 by Algorithm.ai | DevTunisian")

    col4, col3 = st.sidebar.columns([3, 7])
    c1, c2 = st.sidebar.columns([5, 8])
    with col3:
        st.sidebar.write("Follow us on our social media:")
        with c2:
            st.sidebar.markdown("[Facebook](https://www.facebook.com/groups/6772196932792430)")
        with c2:
            st.sidebar.markdown("[Instagram](https://www.instagram.com/jasserabedrazzek/)")
        with c2:
            st.sidebar.markdown("[Discord](https://discord.gg/HFtfNdFv)")
        with c2:
            st.sidebar.markdown("[DevTunisian Web](https://devtunisian.netlify.app/)")


if __name__ == "__main__":
    main()
