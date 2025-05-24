import streamlit as st
import time
import random
import base64

st.set_page_config(page_title="Bestie Fun App", layout="centered")

# ---- Style ----
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        color: #f63366;
    }
    .emoji {
        font-size: 50px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Sound Effect ----
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# ---- Welcome ----
st.title("🎈 Hello Bestie! 🎈")
st.markdown("<p class='big-font'>Welcome to the Most FUN App Made Just for You! ✨</p>", unsafe_allow_html=True)

if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    if st.button("Say Hello 👋"):
        st.session_state.start = True
        autoplay_audio("hello.mp3")  # Add a file named 'hello.mp3' to the directory
        st.balloons()
        time.sleep(1.5)
        st.rerun()
else:
    st.success("Yayyy! You're here, Bestie!")
    st.markdown("### Are you bored? Let's fix that! 🧠💥")
    mood = st.radio("Are you feeling a bit bored?", ["Yes", "Nope, I'm good!"])

    if mood == "Yes":
        st.markdown("---")
        st.header("🤣 Time for Some Comedy Questions! (Tollywood Edition)")
        questions = {
            "What is Brahmanandam most famous for in his roles?": ["His expressions and comic timing!", "Dance moves", "Serious dialogues"],
            "Why did the chicken cross the road in a Telugu movie?": ["To become a hero in the next scene!", "To find biryani", "To escape villain"],
            "What happens when a Telugu hero enters the scene?": ["Background music and slow motion guaranteed!", "Everyone claps", "Hero takes a nap"]
        }

        q_num = st.session_state.get("q_num", 0)
        score = st.session_state.get("score", 0)
        q_keys = list(questions.keys())

        if q_num < len(q_keys):
            current_q = q_keys[q_num]
            options = questions[current_q]

            st.write(f"**Q{q_num+1}:** {current_q}")
            answer = st.radio("Choose the funniest answer:", options, key=f"quiz_{q_num}")
            if st.button("Next Question 👉"):
                if answer == options[0]:
                    score += 1
                st.session_state.q_num = q_num + 1
                st.session_state.score = score
                st.rerun()
        else:
            st.success(f"Haha! You scored {score} out of {len(q_keys)} 😂")
            if "show_puzzle_button" not in st.session_state:
                st.session_state.show_puzzle_button = True

            if st.session_state.show_puzzle_button:
                if st.button("🧩 Play Fun Puzzle Games"):
                    st.session_state.puzzle = True
                    st.session_state.show_puzzle_button = False
                    st.rerun()

    # ---- Puzzles ----
    if st.session_state.get("puzzle", False):
        st.markdown("---")
        st.header("🎮 Fun Puzzle Game!")
        game_choice = st.radio("Choose your puzzle:", ["Match the Pattern", "Guess the Number", "Solve Emoji Meaning"])

        if game_choice == "Match the Pattern":
            st.write("🔢 Fill in the missing number: 2, 4, 8, 16, ?")
            match_ans = st.number_input("Enter your answer:", min_value=0, step=1, key="match")
            if st.button("Submit Pattern Answer"):
                if match_ans == 32:
                    st.success("Correct! Doubling pattern! 🧠")
                    st.balloons()
                else:
                    st.error("Nope, try again!")

        elif game_choice == "Guess the Number":
            if "secret" not in st.session_state:
                st.session_state.secret = random.randint(1, 10)
            guess = st.number_input("Guess the number between 1 and 10:", min_value=1, max_value=10, step=1, key="guess")
            if st.button("Guess 🎯"):
                if guess == st.session_state.secret:
                    st.success("Woohoo! You got it!")
                    st.balloons()
                else:
                    st.warning("Try again, bestie!")

        elif game_choice == "Solve Emoji Meaning":
            st.write("🧠 What movie is this? 🍿👮‍♂️🔫")
            emoji_ans = st.text_input("Your answer:").lower()
            if st.button("Submit Emoji Guess"):
                if "gabbar singh" in emoji_ans:
                    st.success("Bang on! It’s Gabbar Singh! 🎬")
                    st.balloons()
                else:
                    st.error("Oops! Think of a police + action movie!")

    # ---- Wrap Up ----
    if not st.session_state.get("puzzle") and mood == "Yes" and st.session_state.get("show_puzzle_button") == False:
        st.markdown("---")
        st.header("🎉 Great Job My Friend! 🎉")
        autoplay_audio("clap.mp3")  # Add a file named 'clap.mp3' to the directory
        st.markdown("You made it through the fun zone! Thanks for playing! ")
        st.snow()

    elif mood == "Nope, I'm good!":
        st.info("Why the hell you are not boared 😡")
        st.image("https://media.giphy.com/media/l2Sqc3POpzkj5rWGs/giphy.gif", width=300)

# Footer
st.markdown("---")
