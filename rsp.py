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
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Function to reset the game
def reset_game():
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.round_num = 1
    st.session_state.game_over = False

# Game logic (only if game not over)
if not st.session_state.game_over:
    user_choice = st.radio("Choose:", choices, format_func=lambda x: f"{emojis[x]} {x.capitalize()}")
    computer_choice = random.choice(choices)

    if st.button("Play", key=f"play_round_{st.session_state.round_num}"):
        st.write(f"### Round {st.session_state.round_num}")
        st.write(f"You chose: {emojis[user_choice]} **{user_choice.capitalize()}**")
        st.write(f"Computer chose: {emojis[computer_choice]} **{computer_choice.capitalize()}**")

        if user_choice == computer_choice:
            st.info("It's a draw! 🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            st.success("🎉 You win this round!")
            st.session_state.user_score += 1
        else:
            st.error("😈 Computer wins this round!")
            st.session_state.computer_score += 1

        st.session_state.round_num += 1

        # Stop after 5 rounds
        if st.session_state.round_num > 5:
            st.session_state.game_over = True

# Display Scoreboard
st.markdown("---")
st.subheader("📊 Scoreboard")
st.write(f"**You:** {st.session_state.user_score} | **Computer:** {st.session_state.computer_score}")
st.write(f"**Round:** {min(st.session_state.round_num, 5)} / 5")

# Final results after 5 rounds
if st.session_state.game_over:
    st.subheader("🏁 Final Results")
    if st.session_state.user_score > st.session_state.computer_score:
        st.success("🎉 Congratulations! You won the game 🏆")
    elif st.session_state.user_score < st.session_state.computer_score:
        st.error("😈 Computer wins the game! Better luck next time.")
    else:
        st.info("🤝 It's a tie overall!")

    # Button to restart game
    if st.button("Play Again"):
        reset_game()
