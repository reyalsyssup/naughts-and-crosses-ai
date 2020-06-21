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

# Render Board
def renderBoard():
    global run
    newBoard = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # fills board
    for row in range(3):
        for j in range(3):
            if(board[row][j]["x"] == 1):
                newBoard[row][j] = "x"
            elif(board[row][j]["o"] == 1):
                newBoard[row][j] = "o"

    # Checking if board is full in which case end the game
    fullCheck = 0
    for row in newBoard:
        for i in row:
            if(i != " "): fullCheck += 1
    if(fullCheck == 9):
        print(f"{Fore.YELLOW}No Winner!")
        run = False
        quit()

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
        return
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

print(f"{Fore.MAGENTA}Player 1: x\nPlayer 2: 0\n")
while run:
    renderBoard()
    print(f"{Fore.MAGENTA}Player {player}, where do you go? x y > ", end="")
    loc = input()
    if(loc == "exit"):
        run = False
        quit()
    loc = list(loc.split(" "))
    updateBoard(player, loc)
    player = player%2+1