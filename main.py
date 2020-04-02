from api.apis import get_board_map, get_board_string, get_games, get_moves, make_move


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
            move = get_moves(gid)
            board = get_board_map(gid)

            # get next move function
            # check if my turn by team id: O first
            # next_move = get_next_move(board, move)

            # 3. do the alg
            next_move = "1,3"
            if next_move:
                result = make_move(gid, next_move)
            else:
                pass
        pass


if __name__ == '__main__':
    main()
