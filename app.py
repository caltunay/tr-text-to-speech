import streamlit as st
from gtts import gTTS
import os
import streamlit.components.v1 as components

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

st.markdown("---")

st.subheader("🎤 Sesini kaydet ve dinle")

# Embed HTML for audio recording and playback
components.html("""
    <audio id="player" controls></audio>
    <br>
    <button onclick="startRecording()">Kayda Başla</button>
    <button onclick="stopRecording()">Kaydı Durdur</button>

    <script>
    let mediaRecorder;
    let audioChunks = [];

    async function startRecording() {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();
        
        mediaRecorder.ondataavailable = function(event) {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = function() {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);
            document.getElementById("player").src = audioUrl;
            audioChunks = [];
        };

        console.log("Recording started");
    }

    function stopRecording() {
        if (mediaRecorder && mediaRecorder.state !== "inactive") {
            mediaRecorder.stop();
            console.log("Recording stopped");
        }
    }
    </script>
""", height=400)
