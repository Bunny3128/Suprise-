import streamlit as st
import numpy as np

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

# Generate a soothing sound (220 Hz + 440 Hz chord, 3 seconds)
def generate_soothing_sound():
    sample_rate = 44100  # Samples per second
    seconds = 3  # Duration
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    # Combine 220 Hz and 440 Hz for a soothing chord
    note = 0.5 * np.sin(220 * t * 2 * np.pi) + 0.5 * np.sin(440 * t * 2 * np.pi)
    return note, sample_rate

# Button to trigger the effect
if st.button("Click Here", on_click=toggle_click):
    pass

# When button is clicked, display message, back button, file uploader, and play soothing sound
if st.session_state.clicked:
    # Full-screen message
    st.markdown(
        """
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
        display: flex; flex-direction: column; justify-content: center; align-items: center; 
        background-color: rgba(0, 0, 0, 0.8); z-index: 1000;">
            <h1 style="color: white; font-size: 5rem; text-align: center; margin-bottom: 20px;">
                Hello Chapri
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Back button to return to initial state
    if st.button("Back", on_click=reset_click):
        pass

    # Generate and play soothing sound automatically
    note, sample_rate = generate_soothing_sound()
    st.audio(note, sample_rate=sample_rate, autoplay=True)
    
    # File uploader for song
    uploaded_file = st.file_uploader("Upload a song (MP3 or WAV)", type=["mp3", "wav"])
    
    # Play Song button
    if st.button("Play Song"):
        if uploaded_file is not None:
            st.audio(uploaded_file, format=uploaded_file.type)
        else:
            try:
                default_song = open("ambient_song.mp3", "rb").read()
                st.audio(default_song, format="audio/mpeg")
            except FileNotFoundError:
                st.error("Default song 'ambient_song.mp3' not found. Please upload a song.")
