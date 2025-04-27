import streamlit as st
from gtts import gTTS
import os

st.title("Türkçe Seslendirme")

# prompt text
text = st.text_area("Söylemek istediğini aşağıya yaz:")

if st.button("Seslendir"):
    if text.strip() != "":
        tts = gTTS(text, lang='tr')
        tts.save("output.mp3")
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("Lütfen bir metin girin.")
