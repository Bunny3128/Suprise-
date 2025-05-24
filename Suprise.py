import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="Chapri Party Zone 🎉",
    page_icon="😎",
    layout="wide"
)

# Apply colorful and funny CSS styling
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #ff6ec4, #7873f5);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }
    .title {
        color: #ffffff;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 3.5rem;
        text-align: center;
        text-shadow: 2px 2px #ff0000;
        animation: bounce 2s infinite;
    }
    .greeting {
        color: #00ff00;
        font-size: 6rem;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        animation: pulse 1.5s infinite;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #ffeb3b;
        color: #d81b60;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: 2px solid #d81b60;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background-color: #d81b60;
        color: #ffeb3b;
    }
    .back-button {
        background-color: #ff1744;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        margin-top: 55vh;
        display: block;
        text-align: center;
        z-index: 1001;
    }
    .debug-text {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 5px;
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-20px); }
        60% { transform: translateY(-10px); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the dashboard
st.markdown('<h1 class="title">Welcome to the Chapri Party Zone! 🦄🎶</h1>', unsafe_allow_html=True)

# Initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Function to toggle clicked state
def toggle_click():
    st.session_state.clicked = True
    st.balloons()  # Trigger balloon effect
    st.write('<p class="debug-text">Debug: Yo, Chapri button smashed! 💥</p>', unsafe_allow_html=True)

# Function to reset clicked state
def reset_click():
    st.session_state.clicked = False
    st.write('<p class="debug-text">Debug: Back to the chill zone! 😎</p>', unsafe_allow_html=True)
    st.experimental_rerun()

# Function to save uploaded song permanently
def save_song(uploaded_file):
    try:
        song_path = "uploaded_song.mp3"  # Fixed name for simplicity
        with open(song_path, "wb") as f:
            f.write(uploaded_file.read())
        st.write(f'<p class="debug-text">Debug: Song saved forever at {song_path}! 🎵</p>', unsafe_allow_html=True)
        return song_path
    except Exception as e:
        st.error(f"Oops, couldn't save the song! 😿 Error: {str(e)}")
        return None

# Button to trigger greeting
if st.button("Smash for Chapri! 😜", key="greet_button", on_click=toggle_click):
    pass

# When button is clicked, display greeting, back button, and file uploader
if st.session_state.clicked:
    # Greeting message
    st.markdown(
        """
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 50%; 
        display: flex; flex-direction: column; justify-content: center; align-items: center; 
        background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff); z-index: 1000;">
            <h1 class="greeting">Hello Chapri! 🌈</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Back button
    if st.button("Back to Party Start! 🚀", key="back_button"):
        reset_click()

    # File uploader for song
    uploaded_file = st.file_uploader("Drop a banger (MP3 or WAV)! 🎧", type=["mp3", "wav"], key="file_uploader")
    if uploaded_file is not None:
        song_path = save_song(uploaded_file)
        if song_path:
            st.session_state.uploaded_song_path = song_path
            st.write('<p class="debug-text">Debug: Song locked in for eternity! 🥳</p>', unsafe_allow_html=True)

    # Play Song button
    if st.button("Crank Up the Jam! 🎉", key="play_song"):
        song_path = getattr(st.session_state, 'uploaded_song_path', None)
        if song_path and os.path.exists(song_path):
            try:
                with open(song_path, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                st.write('<p class="debug-text">Debug: Jammin’ to the saved song! 😍</p>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Whoa, song didn’t play! 😵 Error: {str(e)}")
        else:
            st.error("No banger uploaded yet! Drop a song, homie! 😎")

# Debugging information
st.write(f'<p class="debug-text">Debug: Party mode is {"ON 🔥" if st.session_state.clicked else "CHILL ❄️"}</p>', unsafe_allow_html=True)
