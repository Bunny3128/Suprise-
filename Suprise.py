import streamlit as st
import numpy as np
import io
import wave

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
    st.session_state.clicked = True
    st.balloons()  # Trigger balloon effect
    st.write("Debug: Click Here button triggered")  # Debug log

# Function to reset clicked state
def reset_click():
    st.session_state.clicked = False
    st.write("Debug: Back button triggered")  # Debug log
    st.experimental_rerun()  # Force refresh to ensure state reset

# Generate a soothing sound (220 Hz + 440 Hz chord, 3 seconds) as WAV
def generate_soothing_sound():
    try:
        sample_rate = 44100  # Samples per second
        seconds = 3  # Duration
        t = np.linspace(0, seconds, seconds * sample_rate, False)
        # Combine 220 Hz and 440 Hz for a soothing chord
        note = 0.5 * np.sin(220 * t * 2 * np.pi) + 0.5 * np.sin(440 * t * 2 * np.pi)
        # Normalize to 16-bit PCM format
        note = np.int16(note / np.max(np.abs(note)) * 32767)
        
        # Create WAV file in memory
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wav:
            wav.setnchannels(1)  # Mono
            wav.setsampwidth(2)  # 16-bit
            wav.setframerate(sample_rate)
            wav.writeframes(note.tobytes())
        
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"Error generating sound: {str(e)}")
        return None

# Button to trigger the effect
if st.button("Click Here", key="click_here", on_click=toggle_click):
    pass

# When button is clicked, display message, back button, file uploader, and play soothing sound
if st.session_state.clicked:
    # Full-screen message with space for buttons below
    st.markdown(
        """
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 50%; 
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
            margin-top: 55vh; /* Adjusted for smaller overlay */
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
    audio_buffer = generate_soothing_sound()
    if audio_buffer:
        try:
            st.audio(audio_buffer, format="audio/wav")
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
            st.error("Please upload a song.")  # Removed default song to avoid FileNotFoundError

# Debugging information
st.write(f"Debug: App is in {'clicked' if st.session_state.clicked else 'initial'} state")
