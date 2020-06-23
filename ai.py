def findEmptySpace(board):
    for row in range(3):
        for i in range(3):
            if(board[row][i]["x"] == 0 and board[row][i]["o"] == 0):
                return [row, i]

def move(board):
    # # # CORNERS # # #
    # TL cases APPEARS OK
    if((board[0][0]["x"] == 0 and board[0][0]["o"] == 0) and ((board[0][1]["o"] == 1 and board[0][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][2]["o"] == 1) or (board[2][0]["o"] == 1 and board[1][0]["o"] == 1))):
        return [0, 0]
    # TR cases APPEARS OK
    elif((board[0][2]["x"] == 0 and board[0][2]["o"] == 0) and ((board[0][1]["o"] == 1 and board[0][0]["o"] == 1) or (board[2][0]["o"] == 1 and board[1][1]["o"] == 1) or (board[2][2]["o"] == 1 and board[1][2]["o"] == 1))):
        return [0, 2]
    # BR cases APPEARS OK
    elif((board[2][2]["x"] == 0 and board[2][2]["o"] == 0) and ((board[1][2]["o"] == 1 and board[0][2]["o"] == 1) or (board[0][0]["o"] == 1 and board[1][1]["o"] == 1) or (board[2][0]["o"] == 1 and board[2][1]["o"] == 1))):
        return [2, 2]
    # BL cases APPEARS OK
    elif((board[2][0]["x"] == 0 and board[2][0]["o"] == 0) and ((board[2][1]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][0]["o"] == 1 and board[0][0]["o"] == 1) or (board[0][2]["o"] == 1 and board[1][1]["o"] == 1))):
        return [2, 0]
    # # # CENTRE EDGES # # #
    # TM edge APPEARS OK
    elif((board[0][1]["x"] == 0 and board[0][1]["o"] == 0) and ((board[0][0]["o"] == 1 and board[0][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[2][1]["o"] == 1))):
        return [0, 1]
    # LM edge APPEARS OK
    elif((board[1][0]["x"] == 0 and board[1][0]["o"] == 0) and ((board[0][0]["o"] == 1 and board[2][0]["o"] == 1) or (board[1][1]["o"] == 1 and board[1][2]["o"] == 1))):
        return [1, 0]
    # BM edge CHANGED LAST CASE FIRST PART FROM [2][1] TO [0][1]
    elif((board[2][1]["x"] == 0 and board[2][1]["o"] == 0) and ((board[2][0]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][1]["o"] == 1 and board[0][1]["o"] == 1))):
        return [2, 1]
    # RM edge APPEARS OK
    elif((board[1][2]["x"] == 0 and board[1][2]["o"] == 0) and ((board[0][2]["o"] == 1 and board[2][2]["o"] == 1) or (board[1][0]["o"] == 1 and board[1][1]["o"] == 1))):
        return [1, 2]
    # # # DEAD CENTRE # # # CHANGED FIRST CHECK FIRST PART FROM [1][1] TO [0][1]
    elif((board[1][1]["x"] == 0 and board[1][1]["o"] == 0) and ((board[0][1]["o"] == 1 and board[2][1]["o"] == 1) or (board[1][0]["o"] == 1 and board[1][2]["o"] == 1) or (board[0][0]["o"] == 1 and board[2][2]["o"] == 1) or (board[0][2]["o"] == 1 and board[2][0]["o"] == 1))):
        return [1, 1]
    else:
        # # # # # # # # # # # # # # BLOCKING PLAYER WIN # # # # # # # # # # # # # # # # #
        # TL cases APPEAR FINE
        if((board[0][0]["x"] == 0 and board[0][0]["o"] == 0) and ((board[0][1]["x"] == 1 and board[0][2]["x"] == 1) or (board[1][1]["x"] == 1 and board[2][2]["x"] == 1) or (board[2][0]["x"] == 1 and board[1][0]["x"] == 1))):
            return [0, 0]
        # TR cases APPEAR FINE
        elif((board[0][2]["x"] == 0 and board[0][2]["o"] == 0) and ((board[0][1]["x"] == 1 and board[0][0]["x"] == 1) or (board[2][0]["x"] == 1 and board[1][1]["x"] == 1) or (board[2][2]["x"] == 1 and board[1][2]["x"] == 1))):
            return [0, 2]
        # BR cases APPEAR FINE
        elif((board[2][2]["x"] == 0 and board[2][2]["o"] == 0) and ((board[1][2]["x"] == 1 and board[0][2]["x"] == 1) or (board[0][0]["x"] == 1 and board[1][1]["x"] == 1) or (board[2][0]["x"] == 1 and board[2][1]["x"] == 1))):
            return [2, 2]
        # BL cases APPEAR FINE
        elif((board[2][0]["x"] == 0 and board[2][0]["o"] == 0) and ((board[2][1]["x"] == 1 and board[2][2]["x"] == 1) or (board[1][0]["x"] == 1 and board[0][0]["x"] == 1) or (board[0][2]["x"] == 1 and board[1][1]["x"] == 1))):
            return [2, 0]
        # # # CENTRE EDGES # # #
        # TM edge APPEAR FINE
        elif((board[0][1]["x"] == 0 and board[0][1]["o"] == 0) and ((board[0][0]["x"] == 1 and board[0][2]["x"] == 1) or (board[1][1]["x"] == 1 and board[2][1]["x"] == 1))):
            return [0, 1]
        # LM edge APPEAR FINE
        elif((board[1][0]["x"] == 0 and board[1][0]["o"] == 0) and ((board[0][0]["x"] == 1 and board[2][0]["x"] == 1) or (board[1][1]["x"] == 1 and board[1][2]["x"] == 1))):
            return [1, 0]
        # BM edge FINAL CHECK: EDITED, INCORRECT BOARD[X][Y] ON SECOND CHECK
        elif((board[2][1]["x"] == 0 and board[2][1]["o"] == 0) and ((board[2][0]["x"] == 1 and board[2][2]["x"] == 1) or (board[1][1]["x"] == 1 and board[0][1]["x"] == 1))):
            return [2, 1]
        # RM edge APPEAR FINE
        elif((board[1][2]["x"] == 0 and board[1][2]["o"] == 0) and ((board[0][2]["x"] == 1 and board[2][2]["x"] == 1) or (board[1][0]["x"] == 1 and board[1][1]["x"] == 1))):
            return [1, 2]
        # # # DEAD CENTRE # # # EDITED FIRST CHECK, FIRST PART: CHANGED BOARD[1][1] TO BOARD[0][1]
        elif((board[1][1]["x"] == 0 and board[1][1]["o"] == 0) and ((board[0][1]["x"] == 1 and board[2][1]["x"] == 1) or (board[1][0]["x"] == 1 and board[1][2]["x"] == 1) or (board[0][0]["x"] == 1 and board[2][2]["x"] == 1) or (board[0][2]["x"] == 1 and board[2][0]["x"] == 1))):
            return [1, 1]
        else:
            return findEmptySpace(board)