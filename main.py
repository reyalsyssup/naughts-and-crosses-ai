import ai
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Set up the board as a 2d matrix array
board = [
    [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}],
    [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}],
    [{"x": 0, "o": 0},{"x": 0, "o": 0},{"x": 0, "o": 0}]
]

player = 1
useEnemyAI = False

# Print Win Screen
def printWin(newBoard, playerNum):
    print(Fore.YELLOW + str(newBoard[0]))
    print(Fore.YELLOW + str(newBoard[1]))
    print(Fore.YELLOW + str(newBoard[2]))
    print(f"{Fore.GREEN}We have a winner, congratulations player {playerNum}!")
    quit()

# Check win
def checkWin(newBoard, playerNum):
    for row in newBoard:
        for i in row:
            if(newBoard[0][0] != " "):
                # TL to TR
                if((newBoard[0][1] == newBoard[0][0] and newBoard[0][2] == newBoard[0][0]) or (newBoard[1][1] == newBoard[0][0] and newBoard[2][2] == newBoard[0][0]) or (newBoard[1][0] == newBoard[0][0] and newBoard[2][0] == newBoard[0][0])):
                    printWin(newBoard, playerNum); return
            if(newBoard[2][2] != " "):    
                # All wins from DR (Down Right)
                # DR to TR
                if((newBoard[1][2] == newBoard[2][2] and newBoard[0][2] == newBoard[2][2]) or (newBoard[2][1] == newBoard[2][2] and newBoard[2][0] == newBoard[2][2])):
                    printWin(newBoard, playerNum); return
            if(newBoard[1][1] != " "):
                # Up, down and left, right wins
                if((newBoard[0][1] == newBoard[1][1] and newBoard[2][1] == newBoard[1][1]) or (newBoard[1][0] == newBoard[1][1] and newBoard[1][2]== newBoard[1][1])):
                    printWin(newBoard, playerNum); return
            if(newBoard[0][2] != " "):
                # TR to DL
                if(newBoard[1][1] == newBoard[0][2] and newBoard[2][0] == newBoard[0][2]):
                    printWin(newBoard, playerNum); return

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
    # Checking if board is full in which case end the game
    fullCheck(fillBoard())
    # prints board
    print(Fore.YELLOW + str(fillBoard()[0]))
    print(Fore.YELLOW + str(fillBoard()[1]))
    print(Fore.YELLOW + str(fillBoard()[2]))

def updateBoard(playerNum, loc):
    global player
    # Makes sure location input is in the correct format
    try: loc[0], loc[1] = int(loc[0]), int(loc[1])
    except:
        print(f"{Fore.RED}Invalid Input")
        return False
    boardLoc = board[loc[0]][loc[1]]
    # Checks if player 1/2 is playing and making sure there isnt already a mark in their desired spot
    if(playerNum == 1 and (boardLoc["x"] == 0 and boardLoc["o"] == 0)): boardLoc["x"] = 1
    elif(boardLoc["o"] == 0 and boardLoc["x"] == 0): boardLoc["o"] = 1
    else:
        # If there is a mark in their spot, then tell them
        print(f"{Fore.RED}All ready a mark in that spot. Select another!")
        # Make sure the player doesnt change
        player = playerNum
        return
    checkWin(fillBoard(), playerNum)
    player = player%2+1

def useEnemyAIPrompt():
    global useEnemyAI
    print(f"{Fore.RED}Play with AI? y/n > ", end=""); useEnemyAI = input()
    if(useEnemyAI == "y"): useEnemyAI = True
    else: useEnemyAI = False

def restartOnFullCheck():
    global board
    global player
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
    print(f"{Fore.MAGENTA}Player 1: x\nPlayer 2: o\n")
    while True:
        renderBoard()
        restartOnFullCheck()
        print(f"{Fore.MAGENTA}Player {player}, where do you go? y x > ", end=""); loc = input()
        if(loc == "exit"): quit()
        loc = list(loc.split(" "))
        updateBoard(player, loc)
        restartOnFullCheck()
        if(useEnemyAI and player == 2):
            updateBoard(2, ai.move(board))