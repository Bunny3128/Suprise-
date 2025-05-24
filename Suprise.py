import streamlit as st
from streamlit.components.v1 import html

08

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

# When button is clicked, display message and play sound button
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
            <button onclick="playSound()" 
                style="padding: 10px 20px; font-size: 1.2rem; cursor: pointer; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
                Play Sound
            </button>
        </div>
        <script>
            function playSound() {
                try {
                    var audio = new Audio('https://cdn.pixabay.com/audio/2022/03/24/00-16-27-297_140.mp3');
                    audio.play().then(() => {
                        console.log('Audio playback successful');
                    }).catch(error => {
                        console.error('Audio playback failed:', error);
                    });
                } catch (error) {
                    console.error('Error in playSound:', error);
                }
            }
            // Attempt automatic playback
            document.addEventListener('DOMContentLoaded', function() {
                try {
                    var audio = new Audio('https://cdn.pixabay.com/audio/2022/03/24/00-16-27-297_140.mp3');
                    audio.play().then(() => {
                        console.log('Automatic audio playback successful');
                    }).catch(error => {
                        console.error('Automatic audio playback failed:', error);
                    });
                } catch (error) {
                    console.error('Error in auto-play:', error);
                }
            });
        </script>
        """,
        unsafe_allow_html=True
    )
