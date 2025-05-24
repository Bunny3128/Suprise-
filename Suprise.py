import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Chapri Greeter",
    page_icon="🎉",
    layout="wide"
)

# Title of the dashboard
st.title("Chapri Greeter for My Best Friend!")

# Initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'uploaded_song' not in st.session_state:
    st.session_state.uploaded_song = None
if 'uploaded_song_type' not in st _

# Function to toggle clicked state
def toggle_click():
    st.session_state.clicked = True
    st.balloons()  # Trigger balloon effect
    st.write("Debug: Greet button clicked")

# Function to reset clicked state
def reset_click():
    st.session_state.clicked = False
    st.experimental_rerun()  # Force refresh

# Button to trigger greeting
if st.button("Greet Chapri!", key="greet_button", on_click=toggle_click):
    pass

# When button is clicked, display greeting, back button, and file uploader
if st.session_state.clicked:
    # Greeting message
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

    # File uploader for song
    uploaded_file = st.file_uploader("Upload a song (MP3 or WAV)", type=["mp3", "wav"], key="file_uploader")
    if uploaded_file is not None:
        st.session_state.uploaded_song = uploaded_file.read()
        st.session_state.uploaded_song_type = uploaded_file.type
        st.write("Debug: Song uploaded and stored")

    # Play Song button
    if st.button("Play Song", key="play_song"):
        if st.session_state.uploaded_song is not None:
            try:
                st.audio(st.session_state.uploaded_song, format=st.session_state.uploaded_song_type)
                st.write("Debug: Playing uploaded song")
            except Exception as e:
                st.error(f"Error playing song: {str(e)}")
        else:
            st.error("Please upload a song.")

# Debugging information
st.write(f"Debug: App is in {'clicked' if st.session_state.clicked else 'initial'} state")
