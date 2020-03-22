import numpy as np
import random
from time import sleep

class ChessBoard(object):

    def __init__(self, size, target):
        self.board = np.full((size, size), 0)
        self.target = target
        self.lastChess = []
        self.chessboard_size = size
        self.player = 1
        self.lastPlayer = self.player

    def chessboard_validation(self):
        if self.target > len(self.board):
            return "Please set target <= size!"

    def get_board(self):
        """
        :return: full chess board info as list
        """
        return self.board

    def place_chess(self, x, y, player):

        self.board[x, y] = player
        self.lastChess = [x, y]
        self.lastPlayer = player

    def get_moves(self, dic):
        a = dic["moves"]
        for i in a:
            x = int(i["moveX"])
            y = int(i["moveY"])
            player = i["symbol"]
            if player == "O":
                player = 1
            if player == "X":
                player = 2
            self.place_chess(x, y, player)
        return self.board
    # def random_place(self, player):
    #     l = []
    #
    #     for i in range(len(self.board)):
    #         for j in range(len(self.board)):
    #
    #             if self.board[i][j] == 0:
    #                 l.append([i, j])
    #
    #     current_loc = random.choice(l)
    #     self.board[current_loc[0], current_loc[1]] = player
    #     self.lastChess = [current_loc[0], current_loc[1]]
    #     self.lastPlayer = player

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

    def win(self):
        x_min = max(0, self.lastChess[0] - (self.target - 1))
        x_max = min(self.chessboard_size - 1, self.lastChess[0] + (self.target - 1))
        y_min = max(0, self.lastChess[1] - (self.target - 1))
        y_max = min(self.chessboard_size - 1, self.lastChess[1] + (self.target - 1))

        x = self.lastChess[0]
        y = self.lastChess[1]
        con_chesses = 1

        #row_win
        for i in range(1, self.target):
            if y - i >= y_min and self.board[x][y - i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, self.target):
            if y + i <= y_max and self.board[x][y + i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= self.target:
            return True
        else:
            con_chesses = 1

        #col_win
        for i in range(1, self.target):
            if x - i >= x_min and self.board[x - i][y] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, self.target):
            if x + i <= x_max and self.board[x - i][y] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= self.target:
            return True
        else:
            con_chesses = 1

        #dia1_win
        for i in range(1, self.target):
            if x - i >= x_min and y - i >= y_min and self.board[x - i][y - i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, self.target):
            if x + i <= x_max and y + i <= y_max and self.board[x + i][y + i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= self.target:
            return True
        else:
            con_chesses = 1

        #dia2_win
        for i in range(1, self.target):
            if x - i >= x_min and y + i <= y_max and self.board[x - i][y + i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        for i in range(1, self.target):
            if x + i <= x_max and y - i >= y_min and self.board[x + i][y - i] == self.lastPlayer:
                con_chesses += 1
            else:
                break
        if con_chesses >= self.target:
            return True
        else:
            return False

    def evaluate_win(self):
        winner = 0
        if self.win():
            winner = self.lastPlayer
        if np.all(self.board != 0) and winner == 0:
            winner = -1
        return winner

    # def play_game(self):
    #     winner = 0
    #     counter = 1
    #     print(self.board)
    #     sleep(1)
    #
    #     while winner == 0:
    #         for player in [1, 2]:
    #             self.random_place(player)
    #             print("Board after " + str(counter) + " move")
    #             print(self.board)
    #             sleep(1)
    #             counter += 1
    #             winner = self.evaluate_win()
    #             if winner != 0:
    #                 break
    #     return winner

    # def is_end(self):
    #     """
    #
    #     :return: True if end, else False
    #     """
    #     pass

dic = {"moves":[{"moveId":"17","gameId":"16","teamId":"1194","move":"5,7","symbol":"O","moveX":"5","moveY":"7"},
                  {"moveId":"15","gameId":"16","teamId":"1192","move":"3,3","symbol":"X","moveX":"3","moveY":"3"},
                  {"moveId":"13","gameId":"16","teamId":"1194","move":"5,3","symbol":"O","moveX":"5","moveY":"3"},
                  {"moveId":"11","gameId":"16","teamId":"1192","move":"3,2","symbol":"X","moveX":"3","moveY":"2"}],
         "code":"OK"}

c = ChessBoard(12,6)
print(c.get_moves(dic))








