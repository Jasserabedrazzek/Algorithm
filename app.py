import streamlit as st
from fuzzywuzzy import fuzz
import json
from random import randint
from numpy import array

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

# Load the JSON data
with open("algo.json", "r") as f:
    algorithm_data = json.load(f)
with open("algo_def.json", "r") as file:
    definition = json.load(file)
initial = "ecrire()"


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


# Function to get examples
def get_example(user_input, definition):
    max_similarity_exe = 0
    closest_word_exe = None

    for word2 in definition["Algorithms_exe"]:
        similarity = fuzz.ratio(user_input.lower(), word2.lower())
        if similarity > max_similarity_exe:
            closest_word_exe = word2
            max_similarity_exe = similarity
    

    return closest_word_exe, max_similarity_exe


def main():
    # Algorithm
    user_input = st.chat_input("Say something")

    # Check if user input matches any algorithm key exactly
    if user_input in algorithm_data["Algorithms"] and user_input in definition["Algorithms_exe"]:
        st.code(algorithm_data["Algorithms"][user_input])
        st.write("Example:")
        st.code(definition["Algorithms_exe"][user_input])
        st.write("---")
        st.write("Test Code")
        if user_input == 'lire()' :
            test = st.text_input("Exemple: ","")
            if st.button("Run code"):
                st.code(f"Output: {test}")
        elif user_input == 'ecrire()':
            if st.button("Run code"):
                st.code("Hello , World!")
        elif user_input == '<-' :
            if st.button("Run code"):
                st.code("19")
        elif user_input == 'alors' or user_input == 'si' :
            if st.button("Run code"): st.code(19)
        elif user_input == 'valeur'  :
            N = (st.text_input("donner un entier :"))
            R = (st.text_input("donner un reel :"))
            if N != "             " and N != "" and R != "" and R != "          " and N.isnumeric():
                try:
                    n = int(N)
                    r = float(R)
                    if st.button("Run code"): st.code(f'{n}\n{r}')
                except:
                    if N.isnumeric() == False:
                        st.error('donner un entier en N!')
                    else:
                        st.error('donner une valeur!')
        elif user_input == 'entier'  : 
            rn4 = randint(1,100)
            N = (st.text_input("donner un entier : ",rn4))
            if N != "             " and N != "" :
                try:
                    n = int(N)
                    if st.button("Run code"): st.code(f'{n}')
                except:
                    if N.isnumeric()== False:
                        st.error('donner un entier!')
                    else:
                        st.error('donner une valeur!')
        elif user_input == 'reel'  : 
            R = (st.text_input("donner un reel :"))
            if R != "             " and R != "" :
                try:
                    r = float(R)
                    if st.button("Run code"): st.code(f'{r}')
                except:
                    st.error('donner une valeur!')
        elif user_input == 'afficher':
            if st.button("Run code"):
                st.code("bacmath")
    else:
        # Find the closest matching word
        closest_word, similarity_score = find_closest_word(user_input, algorithm_data)
        closest_word_exe, max_similarity_exe = get_example(user_input, definition)
        if closest_word and similarity_score or closest_word_exe and max_similarity_exe > 60 :  
            st.info(f"Did you mean '{closest_word}'? (Similarity: {similarity_score}%)")
            st.code(algorithm_data["Algorithms"][closest_word])
            st.code(definition["Algorithms_exe"][closest_word_exe])
            if closest_word_exe == 'lire()' and st.checkbox("test code"):
                test = st.text_input("Exemple: ","")
                if st.button("Run code"):
                    st.code(f"Output: {test}")
            else:
                pass
        else:
            st.warning("Algorithm not found. Please try a different input.")
    
    st.markdown("[Learn Qt Designer](#soon)")
    st.write("Free Research Preview. [Algorithm.ai August 4 Version](#).")
    if st.button("Open Sidebar for Show New August 6 Version "):
        with st.sidebar:
            st.markdown("### New August 6 Version")
            st.write("You Can Test Code Now")
    st.write("---")
    col1, col2 = st.columns([2, 5])
    with col2:

        st.write(":copyright:2023 by Algorithm.ai | DevTunisian")

    col4, col3 = st.columns([3, 7])
    c1, c2 = st.columns([5, 8])
    with col3:
        st.write("Follow us on our social media:")
        with c2:
            st.markdown("[Facebook](https://www.facebook.com/groups/6772196932792430)")
        with c2:
            st.markdown("[Instagram](https://www.instagram.com/jasserabedrazzek/)")
        with c2:
            st.markdown("[Discord](https://discord.gg/HFtfNdFv)")
        with c2:
            st.markdown("[DevTunisian Web](https://devtunisian.netlify.app/)")


if __name__ == "__main__":
    main()
