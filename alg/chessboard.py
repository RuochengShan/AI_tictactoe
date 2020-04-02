import numpy as np
import copy


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

    def import_from_moves(self, dic):
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

    def import_from_board(self, board):
        self.board = board

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

    def get_neighbors(self, radius, coordinate):
        # coordinate <- [x, y]
        board = self.get_board()
        row_col = 2 * radius + 1
        neighbor_list = []
        x = coordinate[0]
        y = coordinate[1]
        result = [([0] * row_col) for i in range(row_col)]
        array_row = len(board)
        array_col = len(board[0])

        for i in range(result.__len__()):
            for j in range(result.__len__()):
                if (i + x - radius < 0 or j + y - radius < 0 or
                        i + x - radius >= array_row or j + y - radius >= array_col):
                    pass
                else:
                    neighbor_list.append([i + x - radius, j + y - radius])
        while [x, y] in neighbor_list:
            neighbor_list.remove([x, y])

        return neighbor_list

    def non_zero_coordinates(self):
        board = self.board
        non_zero_list = []
        non_zero_pair = board.nonzero()
        for i in range(len(non_zero_pair[0])):
            non_zero_list.append([int(non_zero_pair[0][i]), int(non_zero_pair[1][i])])
        return non_zero_list

    def create_next_states(self, player):
        board = self.get_board()
        new_states_list = []
        if np.all(board == 0):
            new_board = copy.copy(board)
            center = self.chessboard_size//2
            new_board[center, center] = player
            new_states_list.append(new_board)

        else:
            non_zero_list = self.non_zero_coordinates()
            available_list = []
            for i in non_zero_list:
                neighbor_list = self.get_neighbors(3, i)
                available_list += neighbor_list

            for coordinate in available_list:
                new_board = copy.copy(board)
                new_board[coordinate[0], coordinate[1]] = player
                new_states_list.append(new_board)

        return new_states_list


if __name__ == '__main__':

    dic = {"moves":[{"moveId":"17","gameId":"16","teamId":"1194","move":"5,7","symbol":"O","moveX":"5","moveY":"7"},
                      {"moveId":"15","gameId":"16","teamId":"1192","move":"3,3","symbol":"X","moveX":"3","moveY":"3"},
                      {"moveId":"13","gameId":"16","teamId":"1194","move":"5,3","symbol":"O","moveX":"5","moveY":"3"},
                      {"moveId":"11","gameId":"16","teamId":"1192","move":"3,2","symbol":"X","moveX":"3","moveY":"2"}],
             "code":"OK"}

    c = ChessBoard(5,5)
    a = c.get_neighbors(2, [1,1])
    print(c.import_from_moves(dic))








