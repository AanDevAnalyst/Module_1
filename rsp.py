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

# Radio with emojis
user_choice = st.radio("Choose:", choices, format_func=lambda x: f"{emojis[x]} {x.capitalize()}")

# Computer choice
computer_choice = random.choice(choices)

# Add a unique key to button
if st.button("Play", key="play_button"):
    st.write(f"You chose: {emojis[user_choice]} **{user_choice.capitalize()}**")
    st.write(f"Computer chose: {emojis[computer_choice]} **{computer_choice.capitalize()}**")

    if user_choice == computer_choice:
        st.info("It's a draw! 🤝")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 Congratulations, You win! 😎")
    else:
        st.error("😈 Computer wins!")
