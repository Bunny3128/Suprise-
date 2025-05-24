import streamlit as st
import time
import random
import base64

# Set page configuration
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
        padding: 10px 20px;
        border-radius: 10px;
        transition: transform 0.2s;
    }
    .fun-button:hover {
        transform: scale(1.1);
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
        st.warning(f"⚠️ Audio file '{file_path}' not found. Skipping sound effect.")

# ---- Welcome Section ----
st.title("🎉 Bestie Fun Fiesta! 🎈")
st.markdown("<p class='big-font'>Get Ready for a Tollywood Party, Bestie! 💃🕺</p>", unsafe_allow_html=True)
st.markdown("<p class='emoji'>🥳</p>", unsafe_allow_html=True)

if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    if st.button("🎤 Say 'Hello, Superstar!'", key="start_button", help="Kick off the fun!"):
        st.session_state.start = True
        autoplay_audio("hello.mp3", key="hello_audio")
        st.balloons()
        st.experimental_rerun()
else:
    st.success("🎬 You're the Hero of This Fun Show, Bestie! 🌟")
    st.markdown("### Feeling Bored? Let’s Light Up Your Day! 🔥")
    mood = st.radio("Are you feeling a bit bored?", ["Yes, save me!", "Nah, I'm vibing!"], key="mood_radio")

    if mood == "Yes, save me!":
        st.markdown("---")
        st.header("😂 Tollywood Comedy Quiz Time! 🎭")
        autoplay_audio("quiz_start.mp3", key="quiz_audio")
        questions = {
            "What is Brahmanandam most famous for in his roles?": ["His expressions and comic timing!", "Dance moves", "Serious dialogues"],
            "Why did the chicken cross the road in a Telugu movie?": ["To become a hero in the next scene!", "To find biryani", "To escape villain"],
            "What happens when a Telugu hero enters the scene?": ["Background music and slow motion guaranteed!", "Everyone claps", "Hero takes a nap"],
            "What’s Venkatesh’s go-to movie genre?": ["Family drama with a punch!", "Sci-fi thrillers", "Silent movies"]
        }

        q_num = st.session_state.get("q_num", 0)
        score = st.session_state.get("score", 0)
        q_keys = list(questions.keys())

        if q_num < len(q_keys):
            current_q = q_keys[q_num]
            options = questions[current_q]

            st.write(f"**Q{q_num+1}:** {current_q}")
            answer = st.radio("Pick the funniest answer:", options, key=f"quiz_{q_num}")
            if st.button("Next Question! 🚀", key=f"next_q_{q_num}", help="Submit your answer!"):
                if answer == options[0]:
                    score += 1
                    autoplay_audio("correct.mp3", key=f"correct_{q_num}")
                    st.success("🎉 Correct! You're a Tollywood genius!")
                else:
                    autoplay_audio("wrong.mp3", key=f"wrong_{q_num}")
                    st.warning("😂 Oops, not quite! Try the next one!")
                st.session_state.q_num = q_num + 1
                st.session_state.score = score
                st.experimental_rerun()
        else:
            st.success(f"🎥 Quiz Done! You scored {score} out of {len(q_keys)}! 😎")
            autoplay_audio("clap.mp3", key="clap_audio")
            st.confetti()
            if "show_puzzle_button" not in st.session_state:
                st.session_state.show_puzzle_button = True

            if st.session_state.show_puzzle_button:
                if st.button("🎲 Dive into Puzzle Mania!", key="puzzle_button", help="More fun awaits!"):
                    st.session_state.puzzle = True
                    st.session_state.show_puzzle_button = False
                    autoplay_audio("game_start.mp3", key="game_start_audio")
                    st.experimental_rerun()

    # ---- Puzzle Games Section ----
    if st.session_state.get("puzzle", False):
        st.markdown("---")
        st.header("🎮 Puzzle Party Zone! 🧩")
        st.markdown("<p class='emoji'>🎲</p>", unsafe_allow_html=True)
        game_choice = st.radio("Pick your puzzle adventure:", [
            "Jigsaw Word Puzzle",
            "Number Maze",
            "Emoji Movie Decode",
            "Tollywood Trivia Guess",
            "Dialogue Mash-Up"
        ], key="game_choice_radio")

        if game_choice == "Jigsaw Word Puzzle":
            st.write("🔤 Unscramble this Tollywood-inspired word: **LCOHESO**")
            word_ans = st.text_input("Your answer:", key="word_input").lower()
            if st.button("Check Word! ✅", key="check_word"):
                if word_ans == "school":
                    st.success("🎉 You nailed it! It's 'SCHOOL'! 📚")
                    autoplay_audio("win.mp3", key="word_win")
                    st.balloons()
                else:
                    st.error("😅 Try again, Bestie! Hint: Think education!")
                    autoplay_audio("try_again.mp3", key="word_try")

        elif game_choice == "Number Maze":
            st.write("🧠 Find the next number in this sequence: 5, 10, 20, 40, ?")
            num_ans = st.number_input("Enter your answer:", min_value=0, step=1, key="num_input")
            if st.button("Submit Number! 🔢", key="check_number"):
                if num_ans == 80:
                    st.success("💥 Woohoo! You cracked it! It's 80!")
                    autoplay_audio("win.mp3", key="num_win")
                    st.balloons()
                else:
                    st.warning("🤔 Give it another shot! Hint: Double the fun!")
                    autoplay_audio("try_again.mp3", key="num_try")

        elif game_choice == "Emoji Movie Decode":
            st.write("🎥 Guess this Tollywood movie from emojis: 🕺💃🌧️")
            emoji_ans = st.text_input("Your guess:", key="emoji_input").lower()
            if st.button("Submit Emoji Guess! 🎬", key="check_emoji"):
                if "happy days" in emoji_ans:
                    st.success("🥳 Yesss! It’s 'Happy Days'! You’re a star!")
                    autoplay_audio("win.mp3", key="emoji_win")
                    st.balloons()
                else:
                    st.error("😜 Oops! Hint: Dance + College + Rain = Epic Movie!")
                    autoplay_audio("try_again.mp3", key="emoji_try")

        elif game_choice == "Tollywood Trivia Guess":
            st.write("🌟 Guess the Tollywood star from this clue: 'Known for mass dialogues and mega dance moves!'")
            trivia_ans = st.text_input("Your guess:", key="trivia_input").lower()
            if st.button("Submit Star Guess! ⭐", key="check_trivia"):
                if "chiranjeevi" in trivia_ans:
                    st.success("🎉 Megastar Chiranjeevi! You got it, Bestie!")
                    autoplay_audio("win.mp3", key="trivia_win")
                    st.balloons()
                else:
                    st.error("😉 Not quite! Hint: Think 'Mega' vibes!")
                    autoplay_audio("try_again.mp3", key="trivia_try")

        elif game_choice == "Dialogue Mash-Up":
            st.write("🎤 Combine these words to form a famous Tollywood dialogue: **'Okka', 'Chance', 'Ista'**")
            dialogue_ans = st.text_input("Your answer:", key="dialogue_input").lower()
            if st.button("Check Dialogue! 🎙️", key="check_dialogue"):
                if dialogue_ans == "okka chance ista":
                    st.success("🔥 Wow! 'Okka Chance Ista' is spot on!")
                    autoplay_audio("win.mp3", key="dialogue_win")
                    st.balloons()
                else:
                    st.error("😆 Try again! Hint: It’s a fiery one-liner!")
                    autoplay_audio("try_again.mp3", key="dialogue_try")

    # ---- Wrap-Up Section ----
    if not st.session_state.get("puzzle") and mood == "Yes, save me!" and st.session_state.get("show_puzzle_button") == False:
        st.markdown("---")
        st.header("🎉 You’re a Tollywood Superstar, Bestie! 🌟")
        autoplay_audio("victory.mp3", key="victory_audio")
        st.markdown("You’ve conquered the Fun Fiesta! Thanks for rocking it! 💖")
        st.snow()
        st.confetti()
        if st.button("Play Again? 🔄", key="play_again"):
            st.session_state.start = False
            st.session_state.q_num = 0
            st.session_state.score = 0
            st.session_state.puzzle = False
            st.session_state.show_puzzle_button = False
            st.experimental_rerun()

    elif mood == "Nah, I'm vibing!":
        st.info("😎 You’re already in the Tollywood groove! Here’s a celebratory hug! 🤗")
        st.image("https://media.giphy.com/media/l2Sqc3POpzkj5rWGs/giphy.gif", width=300)
        autoplay_audio("happy_vibe.mp3", key="happy_vibe_audio")

# ---- Footer ----
st.markdown("---")
st.caption("💃 Made with Tollywood Swag & Streamlit Magic! 🎬")
