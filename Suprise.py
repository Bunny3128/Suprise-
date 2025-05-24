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

# Generate a 440 Hz sine wave sound (2 seconds)
def generate_sound():
    sample_rate = 44100  # Samples per second
    seconds = 2  # Duration
    frequency = 440  # 440 Hz (A4 note)
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    note = np.sin(frequency * t * 2 * np.pi)
    return note, sample_rate

# Button to trigger the effect
if st.button("Click Here", on_click=toggle_click):
    pass

# When button is clicked, display message, play sound button, and audio
if st.session_state.clicked:
    # Full-screen message with Play Sound button
    st.markdown(
        """
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
        display: flex; flex-direction: column; justify-content: center; align-items: center; 
        background-color: rgba(0, 0, 0, 0.8); z-index: 1000;">
            <h1 style="color: white; font-size: 5rem; text-align: center; margin-bottom: 20px;">
                Hello Chapri
            </h1>
            <button onclick="document.getElementById('audio').play()" 
                style="padding: 10px 20px; font-size: 1.2rem; cursor: pointer; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
                Play Sound
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Generate and play sound
    note, sample_rate = generate_sound()
    st.audio(note, sample_rate=sample_rate, autoplay=True)
