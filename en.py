import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz, process
from googletrans import Translator
import json
from random import randint

st.set_page_config(
    page_title="Irregular Verbs | DevTunisian",
    page_icon=":bookmark_tabs:",
    layout="centered"
)

def find_close_matches(verb, data):
    verb_choices = data['Infinitive']
    close_matches = process.extract(verb, verb_choices, scorer=fuzz.partial_ratio, limit=5)
    return [match[0] for match in close_matches]





def translate_with_error_handling(text, src='en', dest='ar'):
    try:
        if text:
            translator = Translator()
            translation = translator.translate(text, src=src, dest=dest)
            return translation.text
        
    except Exception as e:
        return f"Translation Error: {e}"

def main():
    st.title("English Irregular Verbs Table")
    st.info(":point_left: Open Sidebar for search verb and translate")
    st.sidebar.title("English Irregular Verbs, search and translate. ")
    verb = st.sidebar.text_input("Find verb:", "be")

    # Sample data of irregular verbs (You can replace this with your own data)
    data = {
        'Infinitive': ['arise', 'awake', 'be','beat','become','begin','bend','bet','bit','bleed','blow','break','bring','build','burn','burst','buy','catch','choose','come','cost','cut','dig','do','draw','dream','drive','eat','fall','feed','feel','fight','find','fly','forget','get','give','go','grow','have','hear','hit','hold','hurt','keep','know','lead','learn','leave','let','lie','lose','make','meet','pay','put','read','ride','ring','run','say','see','sell','send','shoot','show','shut','sing','sit','sleep','speak','spend','stand','steal','swim','take','teach','tear','tell','think','throw','understand','wear','win','write'],
        'Simple Past': ['arose', 'awoke', 'was/were','beat','became','began','bent','bet','bit','bled','blew','broke','brought','built','burned/burnt','burst','bought','caught','chose','came','cost','cut','dug','did','drew','dreamed/dreamt','drove','ate','fell','fed','felt','fought','found','flew','forgot','got','gave','went','grew','had','heard','hit','held','hurt','kept','knew','led','learned/learnt','left','let','lay','lost','made','met','paid','put','read','rode','rang','ran','said','saw','sold','sent','shot','showed/showed','shut','sang','sat','slept','spoke','spent','stood','stole','swam','took','taught','tore','told','thought','threw','understood','wore','won','wrote'],
        'Past Participle': ['arisen', 'awoken', 'been','beaten','become','begun','bent','bet','bitten','bled','blown','broken','brought','built','burned/burnt','burst','bought','caught','chosen','come','cost','cut','dug','done','drawn','dreamed/dreamt','driven','eaten','fallen','fed','felt','fought','found','flown','forgotten','got','given','gone','grown','had','heard','hit','held','hurt','kept','known','led','learned/learnt','left','let','lain','lost','made','met','paid','put','read','ridden','rung','run','said','seen','sold','sent','shot','shown','shut','sung','sat','slept','spoken','spent','stood','stolen','swum','taken','taught','torn','told','thought','thrown','understood','worn','won','written'],
    }

    if verb == "                  ":
        pass
    elif verb in data['Infinitive']:
        # If the exact verb exists in the data, use it directly
        verb_index = data['Infinitive'].index(verb)
        simple_past = data['Simple Past'][verb_index]
        past_participle = data['Past Participle'][verb_index]

        # Translate verb forms with error handling
        verb_translated = translate_with_error_handling(verb, src='en', dest='ar')
        simple_past_translated = translate_with_error_handling(simple_past, src='en', dest='ar')
        past_participle_translated = translate_with_error_handling(past_participle, src='en', dest='ar')

    else:
        # If the exact verb doesn't exist, find the closest matches
        close_matches = find_close_matches(verb, data)
        if len(close_matches) > 0:
            verb_index = data['Infinitive'].index(close_matches[0])
            simple_past = data['Simple Past'][verb_index]
            past_participle = data['Past Participle'][verb_index]

            # Translate verb forms with error handling
            verb_translated = translate_with_error_handling(verb, src='en', dest='ar')
            simple_past_translated = translate_with_error_handling(simple_past, src='en', dest='ar')
            past_participle_translated = translate_with_error_handling(past_participle, src='en', dest='ar')
        else:
            simple_past = "Not found"
            past_participle = "Not found"
            verb_translated = "Not found"
            simple_past_translated = "Not found"
            past_participle_translated = "Not found"
            st.sidebar.write("No matches found for the entered verb.")

    st.sidebar.write('---')
    st.sidebar.write("verb (Translated):", verb_translated)
    st.sidebar.write("Simple Past:", simple_past)
    st.sidebar.write("Past Participle:", past_participle)
    

    # Create a DataFrame using the data
    df = pd.DataFrame(data)

    # Specify the width of the table (e.g., 700 pixels)
    table_width = 1300

    # Display the DataFrame as a table using Streamlit
    st.dataframe(df, width=table_width, height=3012)

    st.write("Free Research Preview. [Irregular Verbs Table August 3 Version](#).")

if __name__ == "__main__":
    main()

st.sidebar.write('---')
st.sidebar.write(":copyright:2023 by Irregular Verbs Table | DevTunisian")
col4, col3 = st.columns([3, 7])
c1, c2 = st.columns([5, 8])
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


