import ai
import colorama
from colorama import Fore, init
init(autoreset=True)

# Set up the board as a 2d matrix array
board = [
    [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}],
    [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}],
    [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}]
]

run = True
player = 1
useEnemyAI = False

# Print Win Screen
def printWin(newBoard, playerNum):
    print(Fore.YELLOW + str(newBoard[0]))
    print(Fore.YELLOW + str(newBoard[1]))
    print(Fore.YELLOW + str(newBoard[2]))
    print(f"{Fore.GREEN}We have a winner, congratulations player {playerNum}!")
    run = False
    quit()

# Check win
def checkWin(newBoard, playerNum):
    # Checking if anyone has won
    tlCheckingChar = newBoard[0][0]
    drCheckingChar = newBoard[2][2]
    mmCheckingChar = newBoard[1][1]
    trCheckingChar = newBoard[0][2]
    for row in newBoard:
        for i in row:
            if(tlCheckingChar != " "):
                # TL to TR
                if(newBoard[0][1] == tlCheckingChar and newBoard[0][2] == tlCheckingChar):
                    printWin(newBoard, playerNum)
                # TL to DL
                elif(newBoard[1][0] == tlCheckingChar and newBoard[2][0] == tlCheckingChar):
                    printWin(newBoard, playerNum)
                # Left to right diag
                # TL to DR
                elif(newBoard[1][1] == tlCheckingChar and newBoard[2][2] == tlCheckingChar):
                    printWin(newBoard, playerNum)
            if(drCheckingChar != " "):    
                # All wins from DR (Down Right)
                # DR to TR
                if(newBoard[1][2] == drCheckingChar and newBoard[0][2] == drCheckingChar):
                    printWin(newBoard, playerNum)
                # DR to DL
                elif(newBoard[2][1] == drCheckingChar and newBoard[2][0] == drCheckingChar):
                    printWin(newBoard, playerNum)
            if(mmCheckingChar != " "):
                # Up, down and left, right wins
                if(newBoard[0][1] == mmCheckingChar and newBoard[2][1] == mmCheckingChar):
                    printWin(newBoard, playerNum)
                elif(newBoard[1][0] == mmCheckingChar and newBoard[1][2]== mmCheckingChar):
                    printWin(newBoard, playerNum)
            if(trCheckingChar != " "):
                # TR to DL
                if(newBoard[1][1] == trCheckingChar and newBoard[2][0] == trCheckingChar):
                    printWin(newBoard, playerNum)

# Check if board is full
def fullCheck(newBoard):
    fullCounter = 0
    for row in newBoard:
        for i in row:
            if(i != ' '): fullCounter += 1
    if(fullCounter == 9): return True
    else: return False

def fillBoard():
    newBoard = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # fills board
    for row in range(3):
        for j in range(3):
            if(board[row][j]["x"] == 1): newBoard[row][j] = "x"
            elif(board[row][j]["o"] == 1): newBoard[row][j] = "o"
            else: newBoard[row][j] = " "
    return newBoard

# Render Board
def renderBoard():
    global run
    newBoard = fillBoard()

    # Checking if board is full in which case end the game
    fullCheck(newBoard)

    # prints board
    print(Fore.YELLOW + str(newBoard[0]))
    print(Fore.YELLOW + str(newBoard[1]))
    print(Fore.YELLOW + str(newBoard[2]))

def updateBoard(playerSymbol, loc):
    global player
    # Makes sure location input is in the correct format
    try: loc[0], loc[1] = int(loc[0]), int(loc[1])
    except:
        print(f"{Fore.RED}Invalid Input")
        player = player%2+1
        return False
    boardLoc = board[loc[0]][loc[1]]
    # Checks if player 1/2 is playing and making sure there isnt already a mark in their desired spot
    if playerSymbol == 1 and (boardLoc["x"] == 0 and boardLoc["o"] == 0):
        boardLoc["x"] = 1
    elif(boardLoc["o"] == 0 and boardLoc["x"] == 0):
        boardLoc["o"] = 1
    else:
        # If there is a mark in their spot, then tell them
        print(f"{Fore.RED}All ready a mark in that spot. Select another!")
        # Make sure the player doesnt change
        player = player%2+1

def useEnemyAIPrompt():
    global useEnemyAI
    print(f"{Fore.RED}Play with AI? y/n > ", end="")
    useEnemyAI = input()
    if(useEnemyAI == "y"): useEnemyAI = True

def restartOnFullCheck():
    global board
    global player
    global useEnemyAI
    # If the board is full there's no point in continuing, just quit the app
    if(fullCheck(fillBoard()) == True):
        renderBoard()
        print(f"{Fore.YELLOW}No Winner!\nRestart? y/n > ", end="")
        restart = input()
        if(restart == "y"):
            board = [
                [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}],
                [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}],
                [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}]
            ]
            player = 1
            useEnemyAIPrompt()
        else:
            quit()

if(__name__ == "__main__"):
    useEnemyAIPrompt()
    print(f"{Fore.MAGENTA}Player 1: x\nPlayer 2: 0\n")
    while run:
        restartOnFullCheck()
        renderBoard()
        print(f"{Fore.MAGENTA}Player {player}, where do you go? y x > ", end=""); loc = input()
        if(loc == "exit"):
            run = False
            quit()
        loc = list(loc.split(" "))
        updateBoard(player, loc)
        checkWin(fillBoard(), player)
        player = player%2+1
        restartOnFullCheck()
        if(useEnemyAI == True and player == 2):
            updateBoard(player, ai.move(board))
            player = player%2+1
            checkWin(fillBoard(), 2)