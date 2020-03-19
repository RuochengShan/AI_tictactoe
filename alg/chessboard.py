import numpy as np


class ChessBoard(object):

    def __init__(self, size):
        self.board = np.full((size, size), 2)

    def get_board(self):
        """

        :return: full chess board info as list
        """
        return self.board

    def place_chess(self, x, y, who):
        """

        :return:
        """
        self.board[x, y] = who

    def get_point(self, x, y):
        """

        :param x: x-coordinate
        :param y: y-coordinate
        :return: a string indicator
        """
        if self.board[x, y] != 0:
            return True
        else:
            return False

    def is_end(self):
        """

        :return: True if end, else False
        """
        pass


