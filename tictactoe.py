import random


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)




    board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
computer = 'X'

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True 
    return False 

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter 
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit() 
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return 
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return    

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False 
    return True 

def playerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return 

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insertLetter(computer, bestMove)
    return 
def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1 
    elif checkWhichMarkWon(player):
        return -1 
    elif checkDraw():
        return 0
        
    if isMaximizing:
        bestScore = -800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer 
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player 
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore


while not checkWin():
    compMove()
    playerMove()