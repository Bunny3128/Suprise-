import streamlit as st
import numpy as np
import sounddevice as sd  # For generating valid audio
import scipy.io.wavfile as wavfile  # For saving audio to WAV format
import os

# Set page configuration
st.set_page_config(
    page_title="Chapri Dashboard",
    page_icon="🎈",
    layout="wide"
)

# Title of the dashboard
st.title("Welcome to the Chapri Dashboard!")

# Initialize session state for button click
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Function to toggle clicked state
def toggle_click():
    st.session_state.clicked = not st.session_state.clicked
    if st.session_state.clicked:
        # Trigger balloon effect when button is clicked
        st.balloons()

# Function to reset clicked state
def reset_click():
    st.session_state.clicked = False

# Generate a soothing sound (220 Hz + 440 Hz chord, 3 seconds) and save as WAV
def generate_soothing_sound():
    sample_rate = 44100  # Samples per second
    seconds = 3  # Duration
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    # Combine 220 Hz and 440 Hz for a soothing chord
    note = 0.5 * np.sin(220 * t * 2 * np.pi) + 0.5 * np.sin(440 * t * 2 * np.pi)
    # Normalize to 16-bit PCM format for WAV
    note = np.int16(note / np.max(np.abs(note)) * 32767)
    # Save to temporary WAV file
    wav_path = "temp_soothing_sound.wav"
    wavfile.write(wav_path, sample_rate, note)
    return wav_path

# Button to trigger the effect
if st.button("Click Here", key="click_here"):
    pass

# When button is clicked, display message, back button, file uploader, and play soothing sound
if st.session_state.clicked:
    # Full-screen message with space for buttons below
    st.markdown(
        """
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 60%; 
        display: flex; flex-direction: column; justify-content: center; align-items: center; 
        background-color: rgba(0, 0, 0, 0.8); z-index: 1000;">
            <h1 style="color: white; font-size: 5rem; text-align: center; margin-bottom: 20px;">
                Hello Chapri
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Back button styled for visibility
    st.markdown(
        """
        <style>
        .back-button {
            background-color: #ff4b4b; 
            color: white; 
            padding: 10px 20px; 
            border-radius: 5px; 
            font-size: 16px; 
            font-weight: bold;
            cursor: pointer;
            margin-top: 65vh; /* Adjusted for smaller overlay */
            display: block;
            text-align: center;
            z-index: 1001; /* Ensure button is above overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("Back", key="back_button", on_click=reset_click):
        pass

    # Generate and play soothing sound
    try:
        wav_path = generate_soothing_sound()
        with open(wav_path, "rb") as f:
            st.audio(f.read(), format="audio/wav")
        # Clean up temporary file
        os.remove(wav_path)
    except Exception as e:
        st.error(f"Error playing soothing sound: {str(e)}")

    # File uploader for song
    uploaded_file = st.file_uploader("Upload a song (MP3 or WAV)", type=["mp3", "wav"], key="file_uploader")
    
    # Play Song button
    if st.button("Play Song", key="play_song"):
        if uploaded_file is not None:
            try:
                st.audio(uploaded_file, format=uploaded_file.type)
            except Exception as e:
                st.error(f"Error playing uploaded song: {str(e)}")
        else:
            try:
                default_song = open("ambient_song.mp3", "rb").read()
                st.audio(default_song, format="audio/mpeg")
            except FileNotFoundError:
                st.error("Default song 'ambient_song.mp3' not found. Please upload a song.")
            except Exception as e:
                st.error(f"Error playing default song: {str(e)}")

# Debugging information
if st.session_state.clicked:
    st.write("Debug: App is in clicked state")
else:
    st.write("Debug: App is in initial state")
