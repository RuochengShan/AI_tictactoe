from api.apis import get_board_map, get_board_string, get_games, get_moves, make_move
from alg.chessboard import ChessBoard
from alg.minimax import mini_max_alg
import time


def main():

    while True:

        # 1. get games
        games = get_games()
        game_ids = []
        for g in games:
            for g_id in g:
                if "O" in g[g_id]:
                    game_ids.append(g_id)
        # 2. get boards and moves
        for gid in game_ids:
            result = False
            move = get_moves(gid)
            chess_board = ChessBoard(12, 6)
            if move:
                chess_board.import_from_moves(move)
                player = chess_board.get_symbol(move)
                next_move = mini_max_alg(chess_board, player)
                result = make_move(gid, next_move)
            else:
                # try to move as first
                next_move = mini_max_alg(chess_board, 1)
                result = make_move(gid, next_move)

        time.sleep(1)


if __name__ == '__main__':
    main()
