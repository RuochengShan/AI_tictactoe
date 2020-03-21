import numpy as np
import random
from time import sleep

class ChessBoard(object):

    def __init__(self, size):
        self.board = np.full((size, size), 0)
        self.lastChess = []
        self.chessboard_size = size
        self.player = 1
        self.lastPlayer = self.player

    def get_board(self):
        """
        :return: full chess board info as list
        """
        return self.board

    def place_chess(self, x, y, player):
        """
        :return:
        """
        self.board[x, y] = player
        self.lastChess = [x, y]
        self.lastPlayer = player

    def random_place(self, player):
        l = []

        for i in range(len(self.board)):
            for j in range(len(self.board)):

                if self.board[i][j] == 0:
                    l.append([i, j])

        current_loc = random.choice(l)
        self.board[current_loc[0], current_loc[1]] = player
        self.lastChess = [current_loc[0], current_loc[1]]
        self.lastPlayer = player

    # def get_point(self, x, y):
    #     """
    #     :param x: x-coordinate
    #     :param y: y-coordinate
    #     :return: a string indicator
    #     """
    #     if self.board[x, y] != 0:
    #         return True
    #     else:
    #         return False

    def row_win(self):
        y_min = max(0, self.lastChess[1] - 5)
        y_max = min(self.chessboard_size - 1, self.lastChess[1] + 5)

        x = self.lastChess[0]
        y = self.lastChess[1]
        con_chesses = 1

        for i in range(1, 6):
            if y - i >= y_min and self.board[x][y - i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, 6):
            if y + i <= y_max and self.board[x][y + i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= 6:
            return True
        else:
            return False

    def col_win(self):
        x_min = max(0, self.lastChess[0] - 5)
        x_max = min(self.chessboard_size - 1, self.lastChess[0] + 5)

        x = self.lastChess[0]
        y = self.lastChess[1]
        con_chesses = 1

        for i in range(1, 6):
            if x - i >= x_min and self.board[x - i][y] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, 6):
            if x + i <= x_max and self.board[x - i][y] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= 6:
            return True
        else:
            return False

    def dia1_win(self):
        x_min = max(0, self.lastChess[0] - 5)
        x_max = min(self.chessboard_size - 1, self.lastChess[0] + 5)
        y_min = max(0, self.lastChess[1] - 5)
        y_max = min(self.chessboard_size - 1, self.lastChess[1] + 5)

        x = self.lastChess[0]
        y = self.lastChess[1]
        con_chesses = 1

        for i in range(1, 6):
            if x - i >= x_min and y - i >= y_min and self.board[x - i][y - i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, 6):
            if x + i <= x_max and y + i <= y_max and self.board[x + i][y + i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= 6:
            return True
        else:
            return False

    def dia2_win(self):
        x_min = max(0, self.lastChess[0] - 5)
        x_max = min(self.chessboard_size - 1, self.lastChess[0] + 5)
        y_min = max(0, self.lastChess[1] - 5)
        y_max = min(self.chessboard_size - 1, self.lastChess[1] + 5)

        x = self.lastChess[0]
        y = self.lastChess[1]
        con_chesses = 1

        for i in range(1, 6):
            if x - i >= x_min and y + i <= y_max and self.board[x - i][y + i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, 6):
            if x + i <= x_max and y - i >= y_min and self.board[x + i][y - i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= 6:
            return True
        else:
            return False

    def evaluate_win(self):
        winner = 0
        if self.row_win() or self.col_win() or self.dia1_win() or self.dia2_win():
            winner = self.lastPlayer
        if np.all(self.board != 0) and winner == 0:
            winner = -1
        return winner

    def play_game(self):
        winner = 0
        counter = 1
        print(self.board)
        sleep(1)

        while winner == 0:
            for player in [1, 2]:
                self.random_place(player)
                print("Board after " + str(counter) + " move")
                print(self.board)
                sleep(1)
                counter += 1
                winner = self.evaluate_win()
                if winner != 0:
                    break
        return winner

    # def is_end(self):
    #     """
    #
    #     :return: True if end, else False
    #     """
    #     pass

a = ChessBoard(12)
print(a.play_game())