import streamlit as st
from fuzzywuzzy import fuzz
import json
from random import randint
from numpy import array
from math import sqrt
from time import sleep

st.set_page_config(
    page_title="Algorithm AI | DevTunisian",
    page_icon=":computer:",
    layout="centered"
)

def visitor(n):
    with open("user.json", "r") as use:
        usern = json.load(use)
    num = usern["user"]

    if n:
        added = {"user": num+1}
    
    with open("user.json", "w") as add:
        json.dump(added, add)
    if usern["user"] > n:
        return usern["user"] +1         

if 'visits' not in st.session_state:
    st.session_state['visits'] = 0


st.session_state['visits'] += 1
user = st.session_state['visits']


visitor(user)

def likes():
    with open("Likes.json", "r") as usel:
        userl = json.load(usel)
    num_like = userl['user_likes']
    
    data_like = {"user_likes":num_like+1}
    with open("Likes.json", "w") as addl:
        json.dump(data_like, addl)
    if userl["user_likes"] :
        return userl["user_likes"] 




with open("algo.json", "r") as f:
    algorithm_data = json.load(f)
with open("algo_def.json", "r") as file:
    definition = json.load(file)
initial = "ecrire()"


with open("defini.json", "r") as files:
    Title = json.load(files)
    


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
          return '' ,''
    


l = likes()   

def algortitheme(user_input):
        if user_input:
            if user_input in algorithm_data["Algorithms"] and user_input in definition["Algorithms_exe"]:
                with st.chat_message("user"):
                    st.write(f"Je recherche **`{user_input}`** en Python.")
                result = algorithm_data["Algorithms"][user_input]
                with st.chat_message('assistant'):
                    st.write(f"Ok. **`{user_input}`** en Python c'est : **`{result}`** ")

                    st.code(definition["Algorithms_exe"][user_input])
                    if Title["Algorithms_def"][user_input] != "":
                         st.write("**def**")
                         st.write(Title["Algorithms_def"][user_input])
                    else:
                         pass
                    st.write("**output**")
                    if user_input == 'ecrire()':

                            st.code("Hello , World!")
                    elif user_input == '<-' :

                            st.code("19")
                    elif user_input == 'alors' or user_input == 'si' :
                        st.code(19)

                    elif user_input == "arrondi()": 
                        st.info("N.B. : En Python, si la partie fractionnaire est égale a 5, l'entier Pair le plus proche est retourne.")
                
                    elif user_input == 'afficher':
                    
                            st.code("bacmath")
                    elif user_input == "racine":
                     
                        st.code(sqrt(16))
                    elif user_input == "alea":
                        rn5 = randint(1,10)
                      
                        st.code(rn5)
                    elif user_input == "long":
                    
                        st.code(len("Bac Math"))
                    elif user_input == "ou":
                    
                        st.code(True)
                    elif user_input == "pos":
                    
                            st.code('bac'.find('a'))
                    elif user_input == "effacer":
                    
                            st.code("bcmath") 
                    elif user_input == "sous chaine":
                    
                        st.code("bac math"[0:3])
                    elif user_input == "majus":
                    
                            st.code('bac'.upper())
                
                    elif user_input == "pour" or user_input == "boucle pour":
                    
                        for i in range(3):
                            st.code(f"i = {i}")
                    elif user_input == "repeter" or user_input == "tant que":
                    
                        st.code(5)
                    elif user_input == "fonction":
                        st.code(2)
                    elif user_input == "procedeur":
                    
                        st.code("Python")
                    elif user_input == "hashtag":
                        im = Title["Algorithms_def"][user_input]
                        st.image(im)
                    elif user_input == "fonction":  
                      st.code("def nom_fonction():\n\ttrait\n\treturn")
                    elif user_input == "procedeur":  
                      st.code("def nom_procedeur():\n\ttrait")
                if user_input == "qt_designer":
                        videos = [
                            '<iframe width="100%" height="441" src="https://www.youtube.com/embed/T3MBb85n_hY?list=PLY-quDF0nYMwWO89XXjfZDxB4fKUlS073" title="e.com/embed/Bi-cg-2OqBg?list=PLY[PYTHON] - #Bac_3eme  Qt Design (Partie 1)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                            '<iframe width="100%" height="441" src="https://www.youtube.com/embed/Bi-cg-2OqBg?list=PLY-quDF0nYMwWO89XXjfZDxB4fKUlS073" title="[PYTHON] - #Bac_3eme  Qt design ( partie 2 )" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                            '<iframe width="100%" height="441" src="https://www.youtube.com/embed/uiC8iTyQB1k?list=PLY-quDF0nYMwWO89XXjfZDxB4fKUlS073" title="[PYTHON] - #Bac_3eme Qt Design (  partie 3 )" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
                            '<iframe width="100%" height="441" src="https://www.youtube.com/embed/fuV2zdAbUf4?list=PLY-quDF0nYMwWO89XXjfZDxB4fKUlS073" title="[PYTHON] - #Bac_3eme  Qt Design ( partie 4 )" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
                        ]

                        v = st.session_state.get('video_index', 0)

                        
                        if st.button("Previous Video"):
                            v = max(0, v - 1)
                            st.session_state.video_index = v

                        if st.button("Next Video"):
                            v = min(len(videos) - 1, v + 1)
                            st.session_state.video_index = v

                        if 0 <= v < len(videos):
                            st.write(f"[@Elios Academy](https://www.youtube.com/@EliosAcademy) : [PYTHON] - #Bac_3eme Qt Design ( partie {v + 1} )")
                            st.markdown(videos[v], unsafe_allow_html=True)
                            
                        if st.button(f"**{l} :thumbsup:**"):
                                 likes()
                                 
                
                            

            
                
                
    
def main():
    st.title("Algorithme.ai")
    Title="Algorithem :\nDans le but de developper le raisonnement et la capacite de resolution des problemes chez l'apprenant,\nle domaine < Pensee computationnelle et programmation > met l'accent sur l'algorithmique.\nL'ecriture de l'algorithme doit respecter les conventions citees dans ce document."

    user_input = st.selectbox("algorithm :",list(algorithm_data["Algorithms"])).lower()
    if user_input == "" or  user_input == '                ' or user_input == None:
        with st.chat_message("assistant" ):
            st.write("bonjour, puis-je vous aider  aujourd'huit ?")
            st.write("Vous pouvez rechercher n'importe quoi sur l'algorithme.")
            st.write(Title)
            st.write("Cet outil est gratuit et illimité.")
            st.write("Alternativement, vous pouvez visiter le site Web.[DevTunisian](https://devtunisian.netlify.app/)")
    if user_input != "" and  user_input != '                ' and user_input != None:
        algortitheme(user_input)
    
    st.sidebar.markdown("[Learn Qt Designer](#soon)")
    
    st.write("---")
    st.sidebar.write(f"**{visitor(user)} Total Visits made to the website.**")

    st.write("Free Research Preview. [Algorithm.ai August 14 Version](#).")
    col1, col2 = st.columns([2, 5])
    

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
        with col2:

            st.sidebar.write(":copyright:2023 by Algorithm.ai | DevTunisian")

    hide_st_style ="""
    <style>
    #MainMenu {visibility: hidden;}
    footer {vidibility: hidden;}
    header {visibility: hidden;}
    </style>"""
    st.markdown(hide_st_style, unsafe_allow_html=True)
if __name__ == "__main__":
    main()
