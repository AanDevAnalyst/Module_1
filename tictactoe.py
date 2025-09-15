import random

# Initialize the board
def create_board():
    return ["-"] * 9

board = create_board()
currentPlayer = "X"
winner = None
gameRunning = True


def printBoard(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print("---------     ---------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print("---------     ---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def playerInput(board):
    global currentPlayer
    while True:
        try:
            choice = int(input("Enter a number 1-9: "))
            if 1 <= choice <= 9 and board[choice - 1] == "-":
                board[choice - 1] = currentPlayer
                break
            else:
                print("⚠️ Cell not vacant, try again.")
        except ValueError:
            print("⚠️ Invalid input, enter number 1–9.")


def checkWin(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != "-":
            return board[cond[0]]
    return None


def checkTie(board):
    return "-" not in board


def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"


# Improved AI
def computerMove(board):
    global currentPlayer
    if currentPlayer != "O":
        return

    # Winning move
    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            if checkWin(board) == "O":
                return
            board[i] = "-"

    # Block player
    for i in range(9):
        if board[i] == "-":
            board[i] = "X"
            if checkWin(board) == "X":
                board[i] = "O"
                return
            board[i] = "-"

    # Else random
    while True:
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = "O"
            break


def playGame():
    global board, gameRunning, winner, currentPlayer
    board = create_board()
    gameRunning = True
    winner = None
    currentPlayer = "X"

    while gameRunning:
        printBoard(board)

        if currentPlayer == "X":
            playerInput(board)
        else:
            computerMove(board)

        winner = checkWin(board)
        if winner:
            printBoard(board)
            print(f"🎉 The winner is {winner}! 🎉")
            gameRunning = False
        elif checkTie(board):
            printBoard(board)
            print("🤝 It's a Tie!")
            gameRunning = False
        else:
            switchPlayer()


# Main loop
while True:
    playGame()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
