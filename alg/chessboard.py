import numpy as np
import copy
from math import sqrt
import random

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

    def get_symbol(self, move_dic):
        for i in move_dic:
            team_id = i["teamId"]
            symbol = i["symbol"]
            if team_id == "1194":
                if symbol == "O":
                    player = 1
                    return player
                else:
                    player = 2
                    return player
            else:
                if symbol == "O":
                    player = 1
                    return player
                else:
                    player = 2
                    return player

    def place_chess(self, x, y, player):
        if self.board[x, y] != 0:
            print("fail")
        else:
            self.board[x, y] = player
            self.lastChess = [x, y]
            self.lastPlayer = player


    def import_from_moves(self, dic):
        a = dic
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
        board = self.board
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

    def create_next_states(self, player, tier, count=0):

        board = self.board
        new_states_list = []
        if count > 50000:
            return new_states_list, 50000
        if np.all(board == 0):
            # first move as O, place at center
            new_board = copy.copy(board)
            center = self.chessboard_size//2
            new_board[center, center] = player
            move = str(center)
            move_code = move + "," + move
            new_states_list.append([new_board, move_code])
        elif np.count_nonzero(board == 1) == 1 and np.count_nonzero(board == 2) == 0:
            # first move as X, place at O's neighbor where closest to center
            new_board = copy.copy(board)
            center = self.chessboard_size // 2
            non_zero_coordinate = self.non_zero_coordinates()[0]
            neighbor_list = self.get_neighbors(1, non_zero_coordinate)
            x_2 = 0
            y_2 = 0
            min_dis = 100
            for n in neighbor_list:
                dis_x = (n[0] - center) * (n[0] - center)
                dis_y = (n[1] - center) * (n[1] - center)
                distance = sqrt(dis_x + dis_y)
                if distance < min_dis:
                    min_dis = distance
                    x_2 = n[0]
                    y_2 = n[1]
            new_board[x_2, y_2] = player
            move_code = str(x_2) + "," + str(y_2)
            new_states_list.append([new_board, move_code])

        else:
            non_zero_list = self.non_zero_coordinates()
            available_list = []
            for i in non_zero_list:
                if tier == 1:
                    neighbor_list = self.get_neighbors(2, i)
                else:
                    neighbor_list = self.get_neighbors(1, i)
                for neighbor in neighbor_list:
                    if neighbor not in non_zero_list:
                        available_list.append(neighbor)

            for coordinate in available_list:
                new_board = copy.copy(board)
                new_board[coordinate[0], coordinate[1]] = player
                move_x = str(coordinate[0])
                move_y = str(coordinate[1])
                move_code = move_x + "," + move_y

                t_f_list = [True, False, True, True]
                select = random.sample(t_f_list, 1)
                if select:
                    new_states_list.append([new_board, move_code])
                count += 1

        return new_states_list, count


if __name__ == '__main__':

    dic = {"moves":[{"moveId":"17","gameId":"16","teamId":"1194","move":"5,7","symbol":"O","moveX":"5","moveY":"7"},
                      {"moveId":"15","gameId":"16","teamId":"1192","move":"3,3","symbol":"X","moveX":"3","moveY":"3"},
                      {"moveId":"13","gameId":"16","teamId":"1194","move":"5,3","symbol":"O","moveX":"5","moveY":"3"},
                      {"moveId":"11","gameId":"16","teamId":"1192","move":"3,2","symbol":"X","moveX":"3","moveY":"2"}],
             "code":"OK"}

    c = ChessBoard(5,5)
    a = c.get_neighbors(2, [1,1])
    print(c.import_from_moves(dic))








