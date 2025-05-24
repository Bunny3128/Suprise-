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

# Initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'uploaded_song' not in st.session_state:
    st.session_state.uploaded_song = None
if 'uploaded_song_type' not in st.session_state:
    st.session_state.uploaded_song_type = None

# Function to toggle clicked state
def toggle_click():
    st.session_state.clicked = True
    st.balloons()  # Trigger balloon effect
    st.write("Debug: Click Here button triggered")

# Function to reset clicked state
def reset_click():
    st.session_state.clicked = False
    st.write("Debug: Back button triggered")
    st.experimental_rerun()  # Force refresh

# Generate a soothing sound (220 Hz + 440 Hz chord, 3 seconds) as WAV
def generate_soothing_sound():
    try:
        sample_rate = 44100
        seconds = 3
        t = np.linspace(0, seconds, int(seconds * sample_rate), False)
        note = 0.5 * np.sin(220 * t * 2 * np.pi) + 0.5 * np.sin(440 * t * 2 * np.pi)
        note = np.int16(note / np.max(np.abs(note)) * 32767)
        
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
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

# When button is clicked, display message, back button, file uploader, and play sound
if st.session_state.clicked:
    # Full-screen message
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

    # Back button styling
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
            margin-top: 55vh;
            display: block;
            text-align: center;
            z-index: 1001;
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
            st.write("Debug: Soothing sound attempted")
        except Exception as e:
            st.error(f"Error playing soothing sound: {str(e)}")
    else:
        st.error("Failed to generate soothing sound")

    # File uploader for song
    uploaded_file = st.file_uploader("Upload a song (MP3 or WAV)", type=["mp3", "wav"], key="file_uploader")
    if uploaded_file is not None:
        st.session_state.uploaded_song = uploaded_file.read()  # Store file in session state
        st.session_state.uploaded_song_type = uploaded_file.type
        st.write("Debug: Song uploaded and stored in session state")

    # Play Song button
    if st.button("Play Song", key="play_song"):
        if st.session_state.uploaded_song is not None:
            try:
                st.audio(st.session_state.uploaded_song, format=st.session_state.uploaded_song_type)
                st.write("Debug: Playing uploaded song")
            except Exception as e:
                st.error(f"Error playing uploaded song: {str(e)}")
        else:
            st.error("Please upload a song.")

# Debugging information
st.write(f"Debug: App is in {'clicked' if st.session_state.clicked else 'initial'} state")
