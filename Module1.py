import random
import time


computer_score = 0
users_score = 0
round_num = 0


print("Let's Play Rock ✊, Paper 🤚, Scissor ✌")
print("We Will Be Playing For Five Rounds")
time.sleep(2)
print("Game Start!!!🙂 .................")
choices = ['rock', 'paper', 'scissor']
emojis = {"rock": "✊", "paper": "🤚", "scissor": "✌"}


while round_num !=5:
    print(f"Round {round_num + 1}!")
    computer_choice = random.choice((choices))
    users_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    
    if users_choice not in choices: 
        print("⚠️ Wrong Input 😧")
        print("Let's Try Again But This Time Chose The Right Input i.e. rock/paper/scissor 😉")
        continue

    print(f"Current Score → You: {users_score} | Computer: {computer_score}")
    print(f"You Chose: {users_choice} {emojis[users_choice]}")
    print(f"Computer Chose: {computer_choice} {emojis[computer_choice]}")


    if computer_choice == users_choice:
        print("It's a Draw 🤨")
        print("+1 Point to both players")
        computer_score += 1
        users_score += 1

    elif computer_choice == 'rock' and users_choice == 'scissor':
        print("Computer Wins 😇!!!")
        print("+1 Point to Computer")
        computer_score += 1

    elif computer_choice == 'scissor' and users_choice == 'rock':
        print("You Win 😎!!!")
        print("+1 Point to You")
        users_score += 1

    elif computer_choice == 'paper' and users_choice == 'rock':
        print("Computer Wins 😇!!!")
        print("+1 Point to Computer")
        computer_score += 1    

    elif computer_choice == 'rock' and users_choice == 'paper':
        print("You Win 😎!!!")
        print("+1 Point to You")
        users_score += 1    

    elif computer_choice == 'scissor' and users_choice == 'paper':
        print("Computer Wins 😇!!!")
        print("+1 Point to Computer")
        computer_score += 1    

    elif computer_choice == 'paper' and users_choice == 'scissor':
        print("You Win 😎!!!")
        print("+1 Point to You")
        users_score += 1    
    
    round_num += 1
    print("***************************************************************************************")

print("------------------------------------Game Result--------------------------------------------")
print(f"Your Score: {users_score}")
print(f"Computer's Score: {computer_score}")

if computer_score > users_score:
    print(f"You Lose To Computer By {computer_score - users_score} Score 😞")


elif computer_score < users_score:
    print(f"🎆👏Congratulations YOU WON!!! By {users_score - computer_score } Score 🤩🥳")

else:
    print(f"The Game Was a Tie With Both Score {users_score} 🤝.......")
    print("Wow What a nice game are you up for a rematch 😏")