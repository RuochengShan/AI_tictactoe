from time import sleep, time
import datetime
from alg.chessboard import ChessBoard
from alg.randomPlace import random_place
from alg.minimax import mini_max_alg
from alg.ChessAI import ChessAI
# play with computer
import numpy as np


def player_first():
    chessboard = ChessBoard(12, 6)
    chessAI = ChessAI(12)
    while True:
        n = 0
        print("round %d: player turn" % n)
        xy = input("input x y:")
        x = int(xy.split(" ")[0])
        y = int(xy.split(" ")[1])

        chessboard.place_chess(int(x), int(y), 1)
        print("you place chess at", x, ",", y)
        print("\n")

        print("round %d: computer turn" % n)
        time1 = datetime.datetime.now()
        x1, y1 = chessAI.findBestChess(chessboard.board, 2)
        time2 = datetime.datetime.now()
        duration = time2 - time1
        time_s = duration.total_seconds()
        chessboard.place_chess(y1, x1, 2)
        print("computer place chess at", x1, ",", y1)
        print("computer runtime for this move is: %s" % time_s, "seconds")
        print(chessboard.board)
        print("\n")
        winner = chessboard.evaluate_win()
        sleep(1)
        n += 1
        if winner != 0:
            if winner == 1:
                print("You Win")
            else:
                print("You lose")
            break


def computer_first():
    chessboard = ChessBoard(12, 6)
    chessAI = ChessAI(12)
    while True:
        n = 0
        print("round %d: computer turn" % n)
        if n == 0:
            computer_move = mini_max_alg(chessboard, 1)
            x1 = int(computer_move.split(",")[0])
            y1 = int(computer_move.split(",")[1])
        else:
            x1, y1 = chessAI.findBestChess(chessboard.board, 1)

        chessboard.place_chess(x1, y1, 1)
        print(chessboard.board)
        print("computer place chess at", x1, ",", y1)
        print("\n")

        print("round %d: player turn" % n)
        xy = input("input x y:")
        x = int(xy.split(" ")[0])
        y = int(xy.split(" ")[1])
        chessboard.place_chess(int(x), int(y), 2)
        print(chessboard.board)
        print("you place chess at", x, ",", y)
        print("\n")

        sleep(1)
        n += 1
        winner = chessboard.evaluate_win()
        if winner != 0:
            if winner == 1:
                print("You Win")
            else:
                print("You lose")
            break


if __name__ == '__main__':
    player_first()
    #computer_first()