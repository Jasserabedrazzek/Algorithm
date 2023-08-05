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
            if user_input == 'lire()' :
                test = st.text_input("Example: ","")
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
            elif user_input == "racine":
                if st.button("Run code"):  
                    st.code(sqrt(16))
            elif user_input == "alea":
                rn5 = randint(1,10)
                if st.button("Run code"):  
                    st.code(rn5)
            elif user_input == "long":
                if st.button("Run code"):
                    st.code(len("Bac Math"))
            elif user_input == "pos":
                if st.button("Run code"):
                    st.code('bac'.find('a'))
            if user_input == "effacer":
                if st.button("Run code") :
                    st.code("bcmath") 
            if user_input == "sous chaine":
                if st.button("Run code"):
                    st.code("bac math"[0:3])
            if user_input == "majus":
                if st.button("Run code"):
                    st.code('bac'.upper())
            if user_input == "tab" or user_input == "tableau":
                    n = st.text_input("Enter the size of the array (1 to 5):")
                    if n != "":
                        if int(n) >= 5 :
                            st.error("donner un entier entre 1 et 5")
                    if n and int(n) <= 5 :
                        nb = int(n)
                        T = array([int]*nb)
                        for i in  range(int(nb) ):
                            T[i] = st.text_input(f"T[{i}]")
                        st.write("output")
                        for j in range(nb):
                            st.code(f"T[{j}] = {T[j]}")
            if user_input == "pour" or user_input == "boucle pour":
                if st.button("Run code"):
                    for i in range(3):
                        st.code(f"i = {i}")
            if user_input == "repeter" or user_input == "tant que":
                if st.button("Run code"):
                    st.code(5)
            if user_input == "fonction":
                if st.button("Run code"):
                    st.code(2)
            if user_input == "procedeur":
                if st.button("Run code"):
                    st.code("Python")
            if user_input == "tableau avec sous programme":
                n = st.text_input("Enter the size of the array (1 to 5):")
                if n != "":
                    if int(n) >= 5 :
                        st.error("donner un entier entre 1 et 5")
                if n and int(n) <= 5 :
                    nb = int(n)
                    T = array([int]*nb)
                    for i in  range(int(nb) ):
                        T[i] = st.text_input(f"T[{i}]")
                    st.write("output")
                    for j in range(nb):
                        st.code(f"T[{j}] = {T[j]}")
                            

        else:
            # Find the closest matching word
            closest_word, similarity_score = find_closest_word(user_input, algorithm_data)
            closest_word_exe, max_similarity_exe = get_example(user_input, definition)
            if closest_word and similarity_score or closest_word_exe and max_similarity_exe > 60 :  
                st.info(f"Did you mean '{closest_word}'?")
                st.code(algorithm_data["Algorithms"][closest_word])
                st.code(definition["Algorithms_exe"][closest_word_exe])
                if closest_word == 'lire()' :
                    test = st.text_input("Example: ","")
                    if st.button("Run code"):
                        st.code(f"Output: {test}")
                elif closest_word == 'ecrire()':
                    if st.button("Run code"):
                        st.code("Hello , World!")
                elif closest_word == '<-' :
                    if st.button("Run code"):
                        st.code("19")
                elif closest_word == 'alors' or closest_word == 'si' :
                    if st.button("Run code"): st.code(19)
                elif closest_word == 'valeur'  :
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
                elif closest_word == 'entier'  : 
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
                elif closest_word == 'reel'  : 
                    R = (st.text_input("donner un reel :"))
                    if R != "             " and R != "" :
                        try:
                            r = float(R)
                            if st.button("Run code"): st.code(f'{r}')
                        except:
                            st.error('donner une valeur!')
                elif closest_word == 'afficher':
                    if st.button("Run code"):
                        st.code("bacmath")
                elif closest_word == "racine":
                    if st.button("Run code"):  
                        st.code(sqrt(16))
                elif closest_word == "alea":
                    rn5 = randint(1,10)
                    if st.button("Run code"):  
                        st.code(rn5)
                elif closest_word == "long":
                    if st.button("Run code"):
                        st.code(len("Bac Math"))
                elif closest_word == "pos":
                    if st.button("Run code"):
                        st.code('bac'.find('a'))
                if closest_word == "effacer":
                    if st.button("Run code") :
                        st.code("bcmath") 
                if closest_word == "sous chaine":
                    if st.button("Run code"):
                        st.code("bac math"[0:3])
                if closest_word == "majus":
                    if st.button("Run code"):
                        st.code('bac'.upper())
                if closest_word == "tab" or closest_word == "tableau":
                        n = st.text_input("Enter the size of the array (1 to 5):")
                        if n != "":
                            if int(n) >= 5 :
                                st.error("donner un entier entre 1 et 5")
                        if n and int(n) <= 5 :
                            nb = int(n)
                            T = array([int]*nb)
                            for i in  range(int(nb) ):
                                T[i] = st.text_input(f"T[{i}]")
                            st.write("output")
                            for j in range(nb):
                                st.code(f"T[{j}] = {T[j]}")
                if closest_word == "pour" or closest_word == "boucle pour":
                    if st.button("Run code"):
                        for i in range(3):
                            st.code(f"i = {i}")
                if closest_word == "repeter" or closest_word == "tant que":
                    if st.button("Run code"):
                        st.code(5)
                if closest_word == "fonction":
                    if st.button("Run code"):
                        st.code(2)
                if closest_word == "procedeur":
                    if st.button("Run code"):
                        st.code("Python")
                if closest_word == "tableau avec sous programme":
                    n = st.text_input("Enter the size of the array (1 to 5):")
                    if n != "":
                        if int(n) >= 5 :
                            st.error("donner un entier entre 1 et 5")
                    if n and int(n) <= 5 :
                        nb = int(n)
                        T = array([int]*nb)
                        for i in  range(int(nb) ):
                            T[i] = st.text_input(f"T[{i}]")
                        st.write("output")
                        for j in range(nb):
                            st.code(f"T[{j}] = {T[j]}")
                else:
                    pass
            else:
                st.warning("Algorithm not found. Please try a different input.")
    
def main():
    # Algorithm
    
    algortitheme()
    st.sidebar.write("New version")
    st.sidebar.write("added : tableau avec sous programme")
    st.sidebar.write("added : boucle pour")
    st.sidebar.write("added : sous programme")
    st.sidebar.write("added : test code")
    
        
    
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
