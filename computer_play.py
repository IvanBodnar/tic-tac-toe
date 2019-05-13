from math import inf as infinity


def empty_squares(board):
    return {k: v for k, v in board.items() if v is None}


def minimax(board, depth, player):
    if player == 1:
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]

    # if depth == 0:
    #     score = evaluate(state)
    #     return [-1, -1, score]

    for square in empty_squares(board).items():
        # print(square[0])
        k, v = square[0], square[1]
        board[k] = player
        score = minimax(board, depth - 1, -player)
        # print(score)
        board[k] = 0
        score[0] = k

        if player == 1:
            if score[1] > best[1]:
                best = score # max value
        else:
            if score[1] < best[1]:
                best = score # min value
    # print(best)
    return best
