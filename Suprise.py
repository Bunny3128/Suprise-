import streamlit as st
import time
import random
import base64

# Set page configuration (must be first Streamlit command)
st.set_page_config(page_title="Bestie Fun Fiesta 🎉", layout="centered")

# ---- Style ----
st.markdown("""
    <style>
    .big-font {
        font-size: 32px !important;
        color: #ff2e63;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .emoji {
        font-size: 60px;
        text-align: center;
        animation: bounce 1s infinite;
    }
    .fun-button {
        background-color: #ff6f61;
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 12px;
        transition: transform 0.2s;
    }
    .fun-button:hover {
        transform: scale(1.1);
    }
    .progress-bar {
        background-color: #ffe6e6;
        border-radius: 10px;
        padding: 5px;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    </style>
""", unsafe_allow_html=True)

# ---- Sound Effect Function ----
def autoplay_audio(file_path: str, key: str = None):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay id="{key or 'audio'}">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"⚠️ Audio file '{file_path}' not found! Please ensure it’s in the same directory as Suprise.py.")
    except Exception as e:
        st.error(f"⚠️ Error loading audio '{file_path}': {str(e)}")

# ---- Welcome Section ----
st.title("🎉 Bestie Fun Fiesta! 🎈")
st.markdown("<p class='big-font'>Lights, Camera, Tollywood Action, Bestie! 💃🕺</p>", unsafe_allow_html=True)
st.markdown("<p class='emoji'>🥳</p>", unsafe_allow_html=True)

if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    if st.button("🎤 Yell 'Tollywood Superstar!'", key="start_button", help="Start the party!"):
        st.session_state.start = True
        autoplay_audio("hello.mp3", key="hello_audio")
        st.balloons()
        st.rerun()
else:
    st.success("🎬 You’re the Mahesh Babu of Fun, Bestie! 🌟")
    st.markdown("### Bored? Let’s Unleash Tollywood Chaos! 🔥")
    mood = st.radio("Feeling like a dull scene?", ["Yes, spice it up!", "Nah, I'm a blockbuster!"], key="mood_radio")

    if mood == "Yes, spice it up!":
        st.markdown("---")
        st.header("😂 Tollywood Laugh Riot Quiz! 🎭")
        autoplay_audio("quiz_start.mp3", key="quiz_audio")
        questions = {
            "What does a Tollywood hero do when he sees a villain?": ["Strikes a pose with BGM!", "Runs away", "Eats popcorn"],
            "Why did the ladoo join a Telugu movie?": ["To roll into the heroine’s heart!", "To be a prop", "To start a food fight"],
            "What’s Pawan Kalyan’s Power Star secret?": ["Epic slow-mo walk!", "Singing skills", "Math genius"],
            "How does Brahmanandam steal the show?": ["With one epic expression!", "By directing", "With a boring speech"]
        }

        q_num = st.session_state.get("q_num", 0)
        score = st.session_state.get("score", 0)
        q_keys = list(questions.keys())

        # Progress bar
        progress = (q_num / len(q_keys)) * 100
        st.progress(progress)
        st.markdown(f"<div class='progress-bar'>Progress: {q_num}/{len(q_keys)} Questions</div>", unsafe_allow_html=True)

        if q_num < len(q_keys):
            current_q = q_keys[q_num]
            options = questions[current_q]

            st.write(f"**Q{q_num+1}:** {current_q}")
            answer = st.radio("Pick the funniest answer, Bestie!", options, key=f"quiz_{q_num}")
            if st.button("Lock It In! 🚀", key=f"next_q_{q_num}", help="Submit your answer!"):
                if answer == options[0]:
                    score += 1
                    autoplay_audio("correct.mp3", key=f"correct_{q_num}")
                    st.success(f"🎉 Blockbuster Hit! You're a Tollywood legend!")
                    st.image(f"https://media.giphy.com/media/{random.choice(['3o7btPCcdNniyf0ArS', 'l0IudoJ7oVvvyiG1O'])}/giphy.gif", width=300)
                    st.balloons()
                else:
                    autoplay_audio("wrong.mp3", key=f"wrong_{q_num}")
                    st.warning(f"😂 Cut! That’s a blooper! Try again, Superstar!")
                    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", width=300)
                st.session_state.q_num = q_num + 1
                st.session_state.score = score
                time.sleep(1)  # Brief pause for GIF and sound
                st.rerun()
        else:
            st.success(f"🎥 You’re a Tollywood Titan! Scored {score}/{len(q_keys)}! 😎")
            autoplay_audio("clap.mp3", key="clap_audio")
            try:
                st.confetti()
            except AttributeError:
                st.balloons()
            if "show_puzzle_button" not in st.session_state:
                st.session_state.show_puzzle_button = True

            if st.session_state.show_puzzle_button:
                if st.button("🎲 Jump to Puzzle Mania!", key="puzzle_button", help="More Tollywood fun!"):
                    st.session_state.puzzle = True
                    st.session_state.show_puzzle_button = False
                    autoplay_audio("game_start.mp3", key="game_start_audio")
                    st.rerun()

    # ---- Puzzle Games Section ----
    if st.session_state.get("puzzle", False):
        st.markdown("---")
        st.header("🎮 Tollywood Puzzle Palooza! 🧩")
        st.markdown("<p class='emoji'>🎲</p>", unsafe_allow_html=True)
        game_choice = st.radio("Choose your Tollywood adventure:", [
            "Jigsaw Word Puzzle",
            "Emoji Movie Decode",
            "Hero Face Builder"
        ], key="game_choice_radio")

        if game_choice == "Jigsaw Word Puzzle":
            st.write("🔤 Unscramble this Tollywood-inspired word: **ABUMHES**")
            st.markdown("**Hint**: It’s a Tollywood superstar’s first name!")
            word_ans = st.text_input("Your answer:", key="word_input").lower()
            if st.button("Check Word! ✅", key="check_word"):
                if word_ans == "mahesh":
                    st.success("🎉 Superstar! You got 'MAHESH'! 🌟")
                    autoplay_audio("win.mp3", key="word_win")
                    st.image("https://media.giphy.com/media/l0IudoJ7oVvvyiG1O/giphy.gif", width=300)
                    st.balloons()
                else:
                    st.error("😅 Oof, not quite! Think of a Tollywood prince!")
                    autoplay_audio("try_again.mp3", key="word_try")

        elif game_choice == "Emoji Movie Decode":
            st.write("🎥 Guess this Tollywood movie from emojis: 🦁👑🔥")
            st.markdown("**Hint**: It’s a roaring epic!")
            emoji_ans = st.text_input("Your guess:", key="emoji_input").lower()
            if st.button("Submit Emoji Guess! 🎬", key="check_emoji"):
                if "baahubali" in emoji_ans:
                    st.success("🥳 Epic! It’s 'Baahubali'! You’re a director’s dream!")
                    autoplay_audio("win.mp3", key="emoji_win")
                    st.image("https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif", width=300)
                    st.balloons()
                else:
                    st.error("😜 Missed the mark! Hint: Think epic battles and crowns!")
                    autoplay_audio("try_again.mp3", key="emoji_try")

        elif game_choice == "Hero Face Builder":
            st.write("🦸‍♂️ Build a Tollywood Hero’s Face!")
            st.markdown("Pick features to create a superstar’s face (think Prabhas vibes)!")
            eyes = st.selectbox("Choose the eyes:", ["Intense Gaze", "Sparkling Charm", "Squinting Hero"], key="eyes_input")
            nose = st.selectbox("Choose the nose:", ["Sharp Regal", "Bold Warrior", "Cute Button"], key="nose_input")
            mouth = st.selectbox("Choose the mouth:", ["Smirking Grin", "Heroic Shout", "Romantic Smile"], key="mouth_input")
            if st.button("Reveal Hero! 🌟", key="check_hero"):
                if eyes == "Intense Gaze" and nose == "Bold Warrior" and mouth == "Heroic Shout":
                    st.success("🔥 It’s a Prabhas-level Superstar! You nailed the hero look!")
                    autoplay_audio("win.mp3", key="hero_win")
                    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", width=300)
                    st.balloons()
                    st.confetti()
                else:
                    st.warning("😂 Almost a hero, but not quite! Try Intense Gaze, Bold Warrior, Heroic Shout!")
                    autoplay_audio("try_again.mp3", key="hero_try")
                    st.image("https://media.giphy.com/media/26BRzozg4TCVr32QU/giphy.gif", width=300)

    # ---- Wrap-Up Section ----
    if not st.session_state.get("puzzle") and mood == "Yes, spice it up!" and st.session_state.get("show_puzzle_button") == False:
        st.markdown("---")
        st.header("🎉 You’re the Baahubali of Fun, Bestie! 🌟")
        autoplay_audio("victory.mp3", key="victory_audio")
        st.markdown("You’ve smashed the Tollywood Fun Fiesta! Come back for more! 💖")
        st.snow()
        try:
            st.confetti()
        except AttributeError:
            st.balloons()
        if st.button("Replay the Blockbuster? 🔄", key="play_again"):
            st.session_state.start = False
            st.session_state.q_num = 0
            st.session_state.score = 0
            st.session_state.puzzle = False
            st.session_state.show_puzzle_button = False
            st.rerun()

    elif mood == "Nah, I'm a blockbuster!":
        st.info("😎 You’re already a Tollywood chartbuster! Here’s a mega hug! 🤗")
        st.image("https://media.giphy.com/media/l2Sqc3POpzkj5rWGs/giphy.gif", width=300)
        autoplay_audio("happy_vibe.mp3", key="happy_vibe_audio")

# ---- Footer ----
st.markdown("---")
st.caption("💃 Made with Tollywood Masala & Streamlit Swag! 🎬")
