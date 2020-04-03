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
                x1, y1 = agent.findBestChess(chess_board.board, 2)
                next_move = str(y1)+","+str(x1)
                result = make_move(gid, next_move)
            # else:
            #     # try to move as first
            #     next_move = mini_max_alg(chess_board, 1)
            #     result = make_move(gid, next_move)

        time.sleep(1)


if __name__ == '__main__':
    main()
