def findEmptySpace(board):
    for row in range(3):
        for i in range(3):
            if(board[row][i]["x"] == 0 and board[row][i]["o"] == 0):
                return [row, i]

def move(board):
    # # # CORNERS # # #
    # TL cases
    if((board[0][1]["o"] == 1 and board[0][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][2]["o"] == 1) or (board[2][0]["o"] == 1 and board[1][0]["o"] == 1)):
        if board[0][0]["x"] == 0 and board[0][0]["o"] == 0: return [0, 0]
    # TR cases
    elif((board[0][1]["o"] == 1 and board[0][0]["o"] == 1) or (board[2][0]["o"] == 1 and board[1][1]["o"] == 1) or (board[2][2]["o"] == 1 and board[1][2]["o"] == 1)):
        if board[0][2]["x"] == 0 and board[0][2]["o"] == 0: return [0, 2]
    # BR cases
    elif((board[1][2]["o"] == 1 and board[0][2]["o"] == 1) or (board[0][0]["o"] == 1 and board[1][1]["o"] == 1) or (board[2][0]["o"] == 1 and board[2][1]["o"] == 1)):
        if board[2][2]["x"] == 0 and board[2][2]["o"] == 0: return [2, 2]
    # BL cases
    elif((board[2][1]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][0]["o"] == 1 and board[0][0]["o"] == 1) or (board[0][2]["o"] == 1 and board[1][1]["o"] == 1)):
        if board[2][0]["x"] == 0 and board[2][0]["o"] == 0: return [2, 0]
    # # # CENTRE EDGES # # #
    # TM edge
    elif((board[0][0]["o"] == 1 and board[0][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][1]["o"] == 1)):
        if board[0][1]["x"] == 0 and board[0][1]["o"] == 0: return [0, 1]
    # LM edge
    elif((board[0][0]["o"] == 1 and board[2][0]["o"] == 1) or (board[1][1]["o"] == 1 and board[1][2]["o"] == 1)):
        if board[1][0]["x"] == 0 and board[1][0]["o"] == 0: return [1, 0]
    # BM edge
    elif((board[2][0]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][1]["o"] == 1)):
        if board[2][1]["x"] == 0 and board[2][1]["o"] == 0: return [2, 1]
    # RM edge
    elif((board[0][2]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][0]["o"] == 1 and board[1][1]["o"] == 1)):
        if board[1][2]["x"] == 0 and board[1][2]["o"] == 0: return [1, 2]
    # # # DEAD CENTRE # # #
    elif((board[1][1]["o"] == 1 and board[2][1]["o"] == 1) or (board[1][0]["o"] == 1 and board[1][2]["o"] == 1) or (board[0][0]["o"] == 1 and board[2][2]["o"] == 1) or (board[0][2]["o"] == 1 and board[2][0]["o"] == 1)):
        if board[1][1]["x"] == 0 and board[1][1]["o"] == 0: return [1, 1]
    else:
        ####################### AI WINNING ######################
        # # # CORNERS # # #
        # TL cases
        if((board[0][1]["x"] == 1 and board[0][2]["x"] == 1) or (board[1][1]["x"] == 1 and board[2][2]["x"] == 1) or (board[2][0]["x"] == 1 and board[1][0]["x"] == 1)):
            if board[0][0]["x"] == 0 and board[0][0]["o"] == 0: return [0, 0]
        # TR cases
        elif((board[0][1]["x"] == 1 and board[0][0]["x"] == 1) or (board[2][0]["x"] == 1 and board[1][1]["x"] == 1) or (board[2][2]["x"] == 1 and board[1][2]["x"] == 1)):
            if board[0][2]["x"] == 0 and board[0][2]["o"] == 0: return [0, 2]
        # BR cases
        elif((board[1][2]["x"] == 1 and board[0][2]["x"] == 1) or (board[0][0]["x"] == 1 and board[1][1]["x"] == 1) or (board[2][0]["x"] == 1 and board[2][1]["x"] == 1)):
            if board[2][2]["x"] == 0 and board[2][2]["o"] == 0: return [2, 2]
        # BL cases
        elif((board[2][1]["x"] == 1 and board[2][2]["x"] == 1) or (board[1][0]["x"] == 1 and board[0][0]["x"] == 1) or (board[0][2]["x"] == 1 and board[1][1]["x"] == 1)):
            if board[2][0]["x"] == 0 and board[2][0]["o"] == 0: return [2, 0]
        # # # CENTRE EDGES # # #
        # TM edge
        elif((board[0][0]["x"] == 1 and board[0][2]["x"] == 1) or (board[1][1]["x"] == 1 and board[2][1]["x"] == 1)):
            if board[0][1]["x"] == 0 and board[0][1]["o"] == 0: return [0, 1]
        # LM edge
        elif((board[0][0]["x"] == 1 and board[2][0]["x"] == 1) or (board[1][1]["x"] == 1 and board[1][2]["x"] == 1)):
            if board[1][0]["x"] == 0 and board[1][0]["o"] == 0: return [1, 0]
        # BM edge
        elif((board[2][0]["x"] == 1 and board[2][2]["x"] == 1) or (board[1][1]["x"] == 1 and board[2][1]["x"] == 1)):
            if board[2][1]["x"] == 0 and board[2][1]["o"] == 0: return [2, 1]
        # RM edge
        elif((board[0][2]["x"] == 1 and board[2][2]["x"] == 1) or (board[1][0]["x"] == 1 and board[1][1]["x"] == 1)):
            if board[1][2]["x"] == 0 and board[1][2]["o"] == 0: return [1, 2]
        # # # DEAD CENTRE # # #
        elif((board[1][1]["x"] == 1 and board[2][1]["x"] == 1) or (board[1][0]["x"] == 1 and board[1][2]["x"] == 1) or (board[0][0]["x"] == 1 and board[2][2]["x"] == 1) or (board[0][2]["x"] == 1 and board[2][0]["x"] == 1)):
            if board[1][1]["x"] == 0 and board[1][1]["o"] == 0: return [1, 1]
        else:
            # No wins, no blocks, random spot time
            print(findEmptySpace(board))
            return findEmptySpace(board)