import streamlit as s

s.set_page_config(page_title="WILLIAM BUTCHER",page_icon=":collision:",layout="wide")
with s.container():
    s.title("VELTECH HIGHTECH Dr.RANGARAJAN Dr.SAKUNTHALA ENGINEERING COLLEGE")
    s.subheader("Aavishkaar Project Expo 2024 :heart_on_fire:")
    s.write("[About this Event >](https://velhightech.com)")
    s.title("Hi! I am William Butcher :speech_balloon: ")


from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure (api_key='AIzaSyCsKBsxEb95bQh31g8vbYwyu1ITsOwoJ3U')

model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_butcher_response(question):
    
    response=chat.send_message(question,stream=True)
    return response
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input(label="Ask")
submit=st.button("👍")

if submit and input:
    response=get_butcher_response(input)
    st.session_state['chat_history'].append(("You", input))

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Butcher", chunk.text))
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    
with st.container():
    st.write("---")
    left_column,right_column= st.columns(2)
    with left_column:
        st.header("OI!")
        #st.write("##")
        st.write("=>You can ask me anything.. ")  
        st.write("=>I will answer it...The best way possible")
        st.write("=>I have access to internet up to date")
        st.write("=>I am powered by generative ai api by google")
        st.write("=>I'm STRONGER ! I'm SMARTER ! I'm BETTER !")
        st.write("=>THALA for a reason")

    with right_column:
        image_url="https://cdna.artstation.com/p/assets/images/images/051/522/774/large/jonathan-kagimba-butcher2.jpg?1657528840"
        st.image(image_url,caption="Butcher",width=700)
