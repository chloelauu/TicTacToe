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
        print("Oops, other player has already occupied that spot!")

# check for win / tie

# switch between player 1 & 2

# check for win / tie again

while gameRunning:
    printBoard(board)
    playerInput(board)

