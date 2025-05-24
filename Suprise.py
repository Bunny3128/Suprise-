import streamlit as st
import random

st.set_page_config(page_title="Funny Friend Quiz", layout="centered")

# Title
st.title("🎉 Surprise for My Best Friend!")

# Greet your best friend
st.header("Hi, Hello! 👋")
st.write("Hope you're having a great day!")

# Ask if they're bored
bored = st.radio("Are you bored?", ["Yes", "No"])

# Show quiz if bored
if bored == "Yes":
    st.subheader("Let's lighten the mood with a FUNNY quiz! 🤪")

    questions = {
        "What fruit is known for being *a-peeling*?": [
            "Banana 🍌", "Apple 🍎", "Kiwi 🥝"
        ],
        "Why did the math book look sad?": [
            "It had too many problems 😢", "It failed algebra", "It got divided"
        ],
        "What's orange and sounds like a parrot?": [
            "A carrot 🥕", "An orange crow", "Pumpkin"
        ]
    }

    # Session state for quiz
    if "q_num" not in st.session_state:
        st.session_state.q_num = 0
        st.session_state.score = 0

    q_keys = list(questions.keys())

    if st.session_state.q_num < len(q_keys):
        current_q = q_keys[st.session_state.q_num]
        options = questions[current_q]

        st.write(f"**Q{st.session_state.q_num+1}:** {current_q}")
        answer = st.radio("Choose your answer:", options, key=f"q{st.session_state.q_num}")

        if st.button("Next"):
            if options[0] == answer:  # Always the first option is funny/correct
                st.session_state.score += 1
            st.session_state.q_num += 1
            st.rerun()
    else:
        st.success(f"🎉 Quiz Finished! You got {st.session_state.score} out of {len(q_keys)} right!")
        if st.button("Restart Quiz"):
            st.session_state.q_num = 0
            st.session_state.score = 0
            st.rerun()
else:
    st.write("Okay then, go touch grass 🌱 or drink water 🚰 😄")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
