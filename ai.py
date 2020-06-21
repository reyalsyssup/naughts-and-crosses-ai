def findEmptySpace(board):
    for row in range(3):
        for i in range(3):
            if(board[row][i]["x"] == 0 and board[row][i]["o"] == 0):
                return [row, i]

def move(board):
    ########################## WINNING ########################
    # # # CORNERS # # #
    # TL cases
    if(((board[0][1]["o"] == 1 and board[0][2]["o"] == 1) and (board[0][1]["x"] == 0 and board[0][2]["x"] == 0)) or ((board[1][1]["o"] == 1 and board[2][2]["o"] == 1) and (board[1][1]["x"] == 0 and board[2][2]["x"] == 0)) or ((board[2][0]["o"] == 1 and board[1][0]["o"] == 1) and board[2][0]["x"] == 0 and board[1][0]["x"] == 0)):
        if board[0][0]["x"] == 0 and board[0][0]["o"] == 0: return [0, 0]
        else: return findEmptySpace(board)
    # TR cases
    elif((board[0][1]["o"] == 1 and board[0][0]["o"] == 1) or (board[2][0]["o"] == 1 and board[1][1]["o"] == 1) or (board[2][2]["o"] == 1 and board[1][2]["o"] == 1)):
        if board[0][2]["x"] == 0 and board[0][2]["o"] == 0: return [0, 2]
        else: return findEmptySpace(board)
    # BR cases
    elif((board[1][2]["o"] == 1 and board[0][2]["o"] == 1) or (board[0][0]["o"] == 1 and board[1][1]["o"] == 1) or (board[2][0]["o"] == 1 and board[2][1]["o"] == 1)):
        if board[2][2]["x"] == 0 and board[2][2]["o"] == 0: return [2, 2]
        else: return findEmptySpace(board)
    # BL cases
    elif((board[2][1]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][0]["o"] == 1 and board[0][0]["o"] == 1) or (board[0][2]["o"] == 1 and board[1][1]["o"] == 1)):
        if board[2][0]["x"] == 0 and board[2][0]["o"] == 0: return [2, 0]
        else: return findEmptySpace(board)
    # # # CENTRE EDGES # # #
    # TM edge
    elif((board[0][0]["o"] == 1 and board[0][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][1]["o"] == 1)):
        if board[0][1]["x"] == 0 and board[0][1]["o"] == 0: return [0, 1]
        else: return findEmptySpace(board)
    # LM edge
    elif((board[0][0]["o"] == 1 and board[2][0]["o"] == 1) or (board[1][1]["o"] == 1 and board[1][2]["o"] == 1)):
        if board[1][0]["x"] == 0 and board[1][0]["o"] == 0: return [1, 0]
        else: return findEmptySpace(board)
    # BM edge
    elif((board[2][0]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][1]["o"] == 1)):
        if board[2][1]["x"] == 0 and board[2][1]["o"] == 0: return [2, 1]
        else: return findEmptySpace(board)
    # RM edge
    elif((board[0][2]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][0]["o"] == 1 and board[1][1]["o"] == 1)):
        if board[1][2]["x"] == 0 and board[1][2]["o"] == 0: return [1, 2]
        else: return findEmptySpace(board)
    # DEAD CENTRE
    elif((board[1][1]["o"] == 1 and board[2][1]["o"] == 1) or (board[1][0]["o"] == 1 and board[1][2]["o"] == 1) or (board[0][0]["o"] == 1 and board[2][2]["o"] == 1) or (board[0][2]["o"] == 1 and board[2][0]["o"] == 1)):
        if board[1][1]["x"] == 0 and board[1][1]["o"] == 0: return [1, 1]
        else: return findEmptySpace(board)
    else:
        print(findEmptySpace(board))
        return findEmptySpace(board)