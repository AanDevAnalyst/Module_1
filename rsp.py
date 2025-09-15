import streamlit as st
import random


st.title("Rock Paper Scissors 🎮")

# Map choices to emojis
emojis = {
    "rock": "✊",
    "paper": "🤚",
    "scissors": "✌️"
}

choices = ["rock", "paper", "scissors"]

# Initialize session state variables (only once)
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "round_num" not in st.session_state:
    st.session_state.round_num = 1

# Radio with emojis
user_choice = st.radio("Choose:", choices, format_func=lambda x: f"{emojis[x]} {x.capitalize()}")

# Computer choice
computer_choice = random.choice(choices)

# Add a unique key to button
if st.button("Play", key="play_button"):
    st.write(f"### Round {st.session_state.round_num}")
    st.write(f"You chose: {emojis[user_choice]} **{user_choice.capitalize()}**")
    st.write(f"Computer chose: {emojis[computer_choice]} **{computer_choice.capitalize()}**")

    if user_choice == computer_choice:
        st.info("It's a draw! 🤝")
        st.session_state.user_score += 1
        st.session_state.computer_score += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 Congratulations, You win! 😎")
        st.session_state.user_score += 1
    else:
        st.error("😈 Computer wins!")
        st.session_state.computer_score += 1

    # Update round number
    st.session_state.round_num += 1

# Display Scoreboard
st.markdown("---")
st.subheader("📊 Scoreboard")
st.write(f"**You:** {st.session_state.user_score} | **Computer:** {st.session_state.computer_score}")
st.write(f"**Current Round:** {st.session_state.round_num}")
