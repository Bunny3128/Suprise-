import streamlit as st
import time
import random

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

# ---- Welcome ----
st.title("🎈 Hello Bestie! 🎈")
st.markdown("<p class='big-font'>Welcome to the Most FUN App Made Just for You! 💖</p>", unsafe_allow_html=True)

if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    if st.button("Say Hello 👋"):
        st.session_state.start = True
        st.balloons()
        time.sleep(1)
        st.rerun()
else:
    st.success("Yayyy! You're here, Bestie!")
    st.markdown("### Are you bored? Let's fix that! 🧠💥")
    mood = st.radio("Are you feeling a bit bored?", ["Yes", "Nope, I'm good!"])

    if mood == "Yes":
        st.markdown("---")
        st.header("🤣 Time for Some Comedy Questions!")
        questions = {
            "Why can't your nose be 12 inches long?": ["Because then it would be a foot!", "Because it smells too much", "Because it grows"],
            "Why did the chicken join a band?": ["Because it had the drumsticks!", "Because it could cluck to rhythm", "To be egg-cellent"],
            "What do you call cheese that isn't yours?": ["Nacho cheese!", "My cheese", "Stolen cheese"]
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
            st.session_state.q_num = 0
            st.session_state.score = 0
            if st.button("🎲 Let's Play a Puzzle Now"):
                st.session_state.puzzle = True
                st.rerun()

    # ---- Puzzles ----
    if st.session_state.get("puzzle", False):
        st.markdown("---")
        st.header("🧩 Mini Puzzle Time!")
        riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
        answer = st.text_input("Solve this riddle:", "")

        if answer.lower().strip() == "echo":
            st.success("Correct! You're a genius bestie! 🧠💡")
            st.balloons()
            st.session_state.puzzle = False
        elif answer:
            st.error("Oops! Try again 😊")

    # ---- Wrap Up ----
    if not st.session_state.get("puzzle") and mood == "Yes" and q_num == len(q_keys):
        st.markdown("---")
        st.header("🎉 Great Job My Friend! 🎉")
        st.markdown("You made it through the fun zone! Thanks for playing! 💕")
        st.snow()

    elif mood == "Nope, I'm good!":
        st.info("Aww, glad you're not bored! Here's a hug anyway 🤗")
        st.image("https://media.giphy.com/media/l2Sqc3POpzkj5rWGs/giphy.gif", width=300)

# Footer
st.markdown("---")
st.caption("Made with ❤️ and lots of giggles using Streamlit")
