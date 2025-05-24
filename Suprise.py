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
        background: linear-gradient(135deg, #ff6ec4, #7873f5, #00f7ff);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
    }
    .title {
        color: #ffffff;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 3.5rem;
        text-align: center;
        text-shadow: 3px 3px #ff1744;
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
        margin: 10px;
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
        display: block;
        text-align: center;
        margin: 20px auto;
    }
    .debug-text {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 5px;
        text-align: center;
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
    .fullscreen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff);
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Directory to store uploaded songs
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Initialize session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'song_path' not in st.session_state:
    # Check for existing audio files in the upload directory
    audio_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.mp3', '.wav', '.ogg'))]
    st.session_state.song_path = os.path.join(UPLOAD_DIR, audio_files[0]) if audio_files else None

# Function to toggle clicked state
def toggle_click():
    st.session_state.clicked = True
    st.balloons()

# Function to reset clicked state
def reset_click():
    st.session_state.clicked = False

# Home page
if not st.session_state.clicked:
    # Title of the dashboard
    st.markdown('<h1 class="title">Welcome to the Dashboard! 🦄🎶</h1>', unsafe_allow_html=True)

    # Create two columns for buttons
    col1, col2 = st.columns([1, 1])

    # Smash for Chapri button in the first column
    with col1:
        st.button("Smash for Chapri! 😜", key="greet_button", on_click=toggle_click)

    # Play Saved Banger button in the second column if a song exists
    if st.session_state.song_path and os.path.exists(st.session_state.song_path):
        with col2:
            if st.button("Play Saved Banger! 🎵", key="play_saved_song"):
                try:
                    with open(st.session_state.song_path, "rb") as f:
                        st.audio(f.read(), format="audio/mp3")
                    st.markdown('<p class="debug-text">Debug: Rockin’ the saved song! 🤘</p>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Can’t play the saved song! 😿 Error: {str(e)}")

# Greeting page
if st.session_state.clicked:
    # Full-screen greeting
    with st.container():
        st.markdown(
            """
            <div class="fullscreen">
                <h1 class="greeting">Hello Chapri! 🌈</h1>
                <button class="back-button" onclick="window.location.reload()">Back to Party Start! 🚀</button>
            </div>
            """,
            unsafe_allow_html=True
        )
    # Streamlit button for functionality (hidden by CSS)
    st.button("Back to Party Start! 🚀", key="back_button", on_click=reset_click)
