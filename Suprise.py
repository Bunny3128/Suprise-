import streamlit as st

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_started = False

# Define quiz questions
quiz_questions = [
    {
        'question': "What’s the best way to start a day?",
        'options': ["Jumping out of bed yelling 'I'm late!'", "Snoozing the alarm 5 times", "Dancing to your favorite song", "Checking emails immediately"],
        'answer': "Dancing to your favorite song"
    },
    {
        'question': "If you were a fruit, what would you be?",
        'options': ["Banana – always slipping up", "Apple – keeping doctors away", "Grapes – hanging in bunches", "Pineapple – sweet with a tough exterior"],
        'answer': "Pineapple – sweet with a tough exterior"
    },
    {
        'question': "What's your spirit animal?",
        'options': ["Sloth – master of relaxation", "Cheetah – always on the move", "Owl – wise and nocturnal", "Cat – independent and curious"],
        'answer': "Sloth – master of relaxation"
    }
]

# Function to display the quiz
def display_quiz():
    question = quiz_questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}: {question['question']}")
    selected_option = st.radio("Choose your answer:", question['options'])

    if st.button("Submit Answer"):
        if selected_option == question['answer']:
            st.success("Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Oops! The correct answer was: {question['answer']}")
        
        st.session_state.current_question += 1

        if st.session_state.current_question < len(quiz_questions):
            st.experimental_rerun()
        else:
            st.balloons()
            st.success(f"Quiz Completed! Your Score: {st.session_state.score} / {len(quiz_questions)}")
            if st.button("Restart Quiz"):
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.experimental_rerun()

# Main App
st.title("👋 Hello, Bestie!")
st.write("Hi there! Just wanted to say hello and see how you're doing.")

if not st.session_state.quiz_started:
    if st.button("Are you bored? Let's find out!"):
        st.session_state.quiz_started = True
        st.experimental_rerun()
else:
    display_quiz()
