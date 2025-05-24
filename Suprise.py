import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Hello Bestie! 🐾", layout="centered")

# ---- Style ----
st.markdown("""
    <style>
    .big-font {
        font-size: 40px !important;
        color: #ff4d94;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    .emoji {
        font-size: 60px;
        text-align: center;
        animation: bounce 1s infinite;
    }
    .cat-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    </style>
""", unsafe_allow_html=True)

# ---- Sound Effect Function ----
def autoplay_audio(file_path: str, key: str = None, loop: bool = False):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            loop_attr = "loop" if loop else ""
            md = f"""
                <audio autoplay id="{key or 'audio'}" {loop_attr}>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        if 'audio_warning_shown' not in st.session_state:
            st.session_state.audio_warning_shown = set()
        if file_path not in st.session_state.audio_warning_shown:
            st.warning(f"⚠️ Audio file '{file_path}' not found! Place it in the same directory as hello_bestie.py.")
            st.session_state.audio_warning_shown.add(file_path)
    except Exception as e:
        st.error(f"⚠️ Error loading audio '{file_path}': {str(e)}")

# ---- Dashboard ----
st.markdown("<p class='emoji'>🐾</p>", unsafe_allow_html=True)
st.markdown("<p class='big-font'>Hello Bestie!</p>", unsafe_allow_html=True)

# Display cat image
st.markdown("<div class='cat-container'>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=2043&auto=format&fit=crop", width=400, caption="Your Bestie Cat! 😺")
st.markdown("</div>", unsafe_allow_html=True)

# Play greeting sound and background music
autoplay_audio("hello.mp3", key="hello_audio")
autoplay_audio("background_music.mp3", key="bg_music", loop=True)

# ---- Footer ----
st.markdown("---")
