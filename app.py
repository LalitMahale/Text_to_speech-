
import streamlit as st
from gtts import gTTS 
import PyPDF2

st.header("Convert Your Text into Speech or Speech into Text and PDF to Speech ")

def audio_output(text,lan):
    text_obj = gTTS(text=text, lang=lan,slow=False)
    text_obj.save("temp.mp3")
    return st.audio("temp.mp3")

out = st.radio("",["Text To Speech","PDF To Speech","Developer"],horizontal=True)
if out == "Text To Speech":
    st.image("text.jpg")
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

elif out == "PDF To Speech":
    file = st.file_uploader('Choose your .pdf file', type="pdf")
    if file is not None:
        #file = open(uploaded_file)
        reader = PyPDF2.PdfFileReader(file,"rb")
        page = st.number_input("Enter Page Number",step=1,min_value=1)
        text = reader.getPage(page-1).extract_text()
        if st.button("Convert"):
            audio_output(text,"en")
            if st.button("View text"):
                st.write(text)
elif out == "Developer":

    st.image("developer.jpg")
    st.title("Developer ")
    st.header("""Hi, I'm **Lalit Mahale**, I have done My Post Graduate Diploma in Artificial Intelligence in Artificial Intelligent from CDAC (act's) Pune """)
    if st.button("Contact"):
        gits = "For see read and download code plz visite my github link \n **https://github.com/LalitMahale/Loan-Prediction.git**"
        lin = "Follow at Linkdin - **https://www.linkedin.com/in/lalitmahale1997**"
        email = "Email - **mahalelalit45@gmail.com**"
        st.write(gits)
        st.write(lin)
        st.write(email)
