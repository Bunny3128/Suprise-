import streamlit as st
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="Chapri Dashboard",
    page_icon="🎉",
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

# Button to trigger the effect
if st.button("Click Here", on_click=toggle_click):
    pass

# When button is clicked, display message, confetti, and play sound
if st.session_state.clicked:
    # Full-screen message
    st.markdown(
        """
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
        display: flex; justify-content: center; align-items: center; 
        background-color: rgba(0, 0, 0, 0.8); z-index: 1000;">
            <h1 style="color: white; font-size: 5rem; text-align: center;">
                Hello Chapri
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # JavaScript for confetti effect and audio playback
    confetti_script = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.6.0/confetti.min.js"></script>
    <script>
        // Wait for the document to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Check if confetti is available
            if (typeof confetti === 'function') {
                confetti({
                    particleCount: 150,
                    spread: 80,
                    origin: { y: 0.6 }
                });
            } else {
                console.error('Confetti library not loaded');
            }
            // Play confetti sound
            var audio = new Audio('https://cdn.pixabay.com/audio/2023/06/08/audio_5d3a4b5e67.mp3');
            audio.play().catch(function(error) {
                console.error('Audio playback failed:', error);
            });
        });
    </script>
    """
    html(confetti_script, height=0)
