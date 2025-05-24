import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Hello Bestie! 🎉", layout="centered")

# ---- Style ----
st.markdown("""
    <style>
    .big-font {
        font-size: 48px !important;
        color: #ff6b6b;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        animation: float 2s ease-in-out infinite;
    }
    .fun-button {
        background-color: #ff6b6b;
        color: white;
        font-size: 20px;
        padding: 15px 30px;
        border-radius: 12px;
        display: block;
        margin: 50px auto;
        transition: transform 0.3s;
    }
    .fun-button:hover {
        transform: scale(1.1);
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    .footer {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Sound Effect Function ----
def autoplay_audio(file_path: str, key: str = "audio"):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay id="{key}">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"⚠️ Audio file '{file_path}' not found! Please place 'hello.mp3' in the same directory as hello_bestie.py.")
    except Exception as e:
        st.error(f"⚠️ Error loading audio '{file_path}': {str(e)}")

# ---- Dashboard ----
if 'show_greeting' not in st.session_state:
    st.session_state.show_greeting = False

if not st.session_state.show_greeting:
    if st.button("Say Hello Bestie! 🎉", key="greet_button", help="Click to see the magic!"):
        st.session_state.show_greeting = True
        autoplay_audio("hello.mp3", key="hello_audio")
        try:
            st.confetti()
        except AttributeError:
            st.balloons()
        st.rerun()
else:
    st.markdown("<p class='big-font'>Hello Bestie!</p>", unsafe_allow_html=True)
    try:
        st.confetti()
    except AttributeError:
        st.balloons()

# ---- Footer ----
st.markdown("<p class='footer'>Made with 💖 and Streamlit Sparkle</p>", unsafe_allow_html=True)
