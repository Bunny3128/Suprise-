import streamlit as st
from streamlit.components.v1 import html

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

# Button to trigger the effect
if st.button("Click Here", on_click=toggle_click):
    pass

# When button is clicked, display message, button, and play sound
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
            <button onclick="var audio = new Audio('https://cdn.pixabay.com/audio/2023/06/08/audio_5d3a4b5e67.mp3'); audio.play();" 
                style="padding: 10px 20px; font-size: 1.2rem; cursor: pointer; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
                Play Sound
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # JavaScript for automatic audio playback
    audio_script = """
    <script>
        // Play confetti sound automatically
        document.addEventListener('DOMContentLoaded', function() {
            var audio = new Audio('https://cdn.pixabay.com/audio/2023/06/08/audio_5d3a4b5e67.mp3');
            audio.play().catch(function(error) {
                console.error('Audio playback failed:', error);
            });
        });
    </script>
    """
    html(audio_script, height=0)
