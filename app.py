import streamlit as st
from gtts import gTTS 
import os 

st.image(image = "text.jpg")

def audio_output(text,lan):
    text_obj = gTTS(text=text, lang=lan,slow=False)
    text_obj.save("temp.mp3")
    return st.audio("temp.mp3")

list_lang= ["English","Hindi","Marathi","Gujarati","Malayalam","Tamil",
"Telugu","Kannada","Urdu","Bengali","French","German","Greek","Rassian"]

lang_dic = {"English":"en","Hindi":"hi","Marathi":"mr","Gujarati":"gu",
"Malayalam":"ml","Tamil":"ta","Telugu":"te","Urdu":"ur","Bengali":"bn",
"French":"fr","German":"de","Greek":"el","Kannada":"kn","Rassian":"ru"}



start = st.selectbox("Select Language",list_lang)
text = st.text_area("Enter Text Here...")
lang_code = lang_dic.get(start)

if st.button("Convert"):
        audio_output(text,lang_code)
