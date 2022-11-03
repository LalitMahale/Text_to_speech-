from email.mime import audio
from operator import gt
import streamlit as st
from gtts import gTTS 
import os 


st.title("Text To Speech Converter ")
text = st.text_area("Enter Text Here...")
if st.button("Convert"):

    text_obj = gTTS(text=text, lang="en",slow=False)
    text_obj.save("temp.mp3")
    os.system("temp.mp3")


