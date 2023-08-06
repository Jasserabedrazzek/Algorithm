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
    selected_algorithm = st.selectbox("Select an algorithm:", list(algorithm_data["Algorithms"].keys()))

    if selected_algorithm:
        st.code(algorithm_data["Algorithms"][selected_algorithm])
        st.write("Example:")
        st.code(definition["Algorithms_exe"][selected_algorithm])
        st.write("Output :")
        # Add specific examples for certain algorithms
        if selected_algorithm == 'ecrire()':
            st.code("Hello , World!")
        elif selected_algorithm == '<-':
            st.code("19")
        elif selected_algorithm == 'alors' or selected_algorithm == 'si':
            st.code(19)
        elif selected_algorithm == 'afficher':
            st.code("bacmath")
        elif selected_algorithm == "racine":
            st.code(sqrt(16))
        elif selected_algorithm == "alea":
            rn5 = randint(1, 10)
            st.code(rn5)
        elif selected_algorithm == "long":
                    
                        st.code(len("Bac Math"))
        elif selected_algorithm == "pos":
                    
                    st.code('bac'.find('a'))
        elif selected_algorithm == "effacer":
                    
                    st.code("bcmath") 
        elif selected_algorithm == "sous chaine":
                    
                    st.code("bac math"[0:3])
        elif selected_algorithm == "majus":
                    
                    st.code('bac'.upper())
        elif selected_algorithm == "ou":
                    
                    st.code(True)
        elif selected_algorithm == "arrondi()":
                    
                    st.code(round(12.5))
        elif selected_algorithm == "abs":
               st.code(abs(-15))
        elif selected_algorithm == "pour" or selected_algorithm == "boucle pour":
                    
                    for i in range(3):
                            st.code(f"i = {i}")
        elif selected_algorithm == "repeter" or selected_algorithm == "tant que":
                    
                        st.code(5)
        elif selected_algorithm == "fonction":
                        st.code(2)
        elif selected_algorithm == "procedeur":
                    
                    st.code("Python")
            
    
def main():
    # Algorithm
    
    algortitheme()
    st.sidebar.title("New version:")
    st.sidebar.write(" 1 added : tableau avec sous programme")
    st.sidebar.write(" 2 added : boucle pour")
    st.sidebar.write(" 3 added : sous programme")
    st.sidebar.write(" 4 added : show output")
    st.sidebar.write(" 5 deleted text input and add selectbox")
    
        
    
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
