from time import sleep
from alg.chessboard import ChessBoard
from alg.randomPlace import random_place
from alg.minimax import mini_max_alg
# play with computer
import numpy as np

def player_first():
    chessboard = ChessBoard(12, 6)
    while True:
        n = 0
        print("round %d: player turn" % n)
        xy = input("input x y:")
        x = int(xy.split(" ")[0])
        y = int(xy.split(" ")[1])

        chessboard.place_chess(int(x), int(y), 1)

        print("you place chess at", x, ",", y)
        x = str(n)
        print("round %d: computer turn" % n)
        computer_move = mini_max_alg(chessboard, 2)
        x1 = int(computer_move.split(",")[0])
        y1 = int(computer_move.split(",")[1])
        chessboard.place_chess(x1, y1, 2)
        print("computer place chess at", x1, ",", y1)
        winner = chessboard.evaluate_win()
        sleep(1)
        n += 1
        if winner != 0:
            break



def test():
    chessBoard = ChessBoard(12,6)
    winner = 0
    counter = 1
    print(chessBoard.get_board())
    #sleep(1)

    while winner == 0:
        for player in [1, 2]:
            x, y, player = random_place(chessBoard.board, player)
            chessBoard.place_chess(x, y, player)
            print("Board after " + str(counter) + " move")
            print(chessBoard.board)
            #sleep(1)
            counter += 1
            winner = chessBoard.evaluate_win()
            if winner != 0:
                break
    return winner

if __name__ == '__main__':
    player_first()