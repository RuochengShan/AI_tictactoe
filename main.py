from api.apis import get_board_map, get_board_string, get_games, get_moves, make_move
from alg.chessboard import ChessBoard
from alg.minimax import mini_max_alg
from alg.ChessAI import ChessAI
import time


def main():

    while True:
        # 1. get games
        agent = ChessAI(12)
        games = get_games()
        game_ids = []
        for g in games:
            for g_id in g:
                if "O" in g[g_id] and g_id != "1135" and g_id != "32":
                    game_ids.append(g_id)
        # 2. get boards and moves
        for gid in game_ids:
            result = False
            print("check game %s" % gid)
            move = get_moves(gid)
            chess_board = ChessBoard(12, 6)
            if move:
                chess_board.import_from_moves(move)
                x1, y1 = agent.findBestChess(chess_board.board, 2)
                next_move = str(y1)+","+str(x1)
                result = make_move(gid, next_move)
                if result:
                    move = get_moves(gid)
                    chess_board.import_from_moves(move)
                    print(chess_board.board)
                    print("move for:", gid)
                    print("move", move)
                else:
                    print("not your turn or game ended")
        time.sleep(1)


if __name__ == '__main__':
    main()
