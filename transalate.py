import streamlit as st
from googletrans import Translator

st.header("Machine Translation Demo")                 #header part
input=st.text_area("Please enter the text",value="")     #text area for multiple lines
option=st.selectbox(                                       #dropdown menu
    "To which language you wish to translate this text to?",("Malayalam","Hindi","Tamil"))

if st.button("Translate"):                 #checking if translate button clicked
    translator=Translator()                 #calling Translator
    translation=translator.translate(input,dest=option)      #translate the given text to which option selected
    st.write(translation.text)                               #write the text which is translated