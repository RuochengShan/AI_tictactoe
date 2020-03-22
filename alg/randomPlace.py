import random

def random_place(board, player):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append([i, j])

    current_loc = random.choice(l)
    board[current_loc[0], current_loc[1]] = player
    x = current_loc[0]
    y = current_loc[1]

    return x, y, player