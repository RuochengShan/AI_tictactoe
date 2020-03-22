from time import sleep
from alg.chessboard import ChessBoard
from alg.randomPlace import random_place

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

print(test())