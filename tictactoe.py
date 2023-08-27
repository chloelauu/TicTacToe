board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# print board for tic tac toe game
def printBoard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("--- --- ---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("--- --- ---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# take player input
def playerInput(board):
    #prompts user to enter number (which will be in string type initially), then converts it into an integer using int()
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops, other player has already occupied that spot!\n")

# check for win / tie

# check for horizontal lines
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
# check for vertical lines
def checkVertic(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
# check for diagonal lines
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie! End of game.")
        gameRunning = False

def checkWin(board):
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkVertic(board):
        print(f"The winner is {winner}")
        gameRunning = False
    
# switch between player 1 & 2
def SwitchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# check for win / tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    SwitchPlayer()

