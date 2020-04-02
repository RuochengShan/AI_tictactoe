from alg.chessboard import ChessBoard
import numpy as np


def alpha_beta_pruning():
    pass


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


def generate_one_node(currentstate_id, chessboard, currentplayer, tree_dict, states_dic, max_state_id):
    next_states = chessboard.create_next_states(currentplayer)
    tree_dict[currentstate_id] = []
    states_dic[currentstate_id] = chessboard.board
    max_id = max_state_id[-1]
    for i in next_states:
        max_id += 1
        tree_dict[currentstate_id].append(max_id)
        states_dic[max_id] = i
        max_state_id.append(max_id)
        sorted(max_state_id)


def mini_max(chessboard: ChessBoard, current_player):
    # return the next place coordinate
    states = {}
    tree_index_dict = {}
    player = current_player
    max_state_id = [0]

    current_state_id = max_state_id[-1]

    # depth 1 <- us play
    generate_one_node(current_state_id, chessboard, player, tree_index_dict, states, max_state_id)

    # depth 2 <- opp play
    player = switch_player(player)
    for i in tree_index_dict[0]:
        tier2_state = states[i]
        new_state = ChessBoard(3, 3)
        new_state.import_from_board(tier2_state)
        generate_one_node(i, new_state, player, tree_index_dict, states, max_state_id)

    # depth 3 <- us play
    player = switch_player(player)
    for i in tree_index_dict[0]:
        for j in tree_index_dict[i]:
            tier3_state = states[j]
            new_state = ChessBoard(3, 3)
            new_state.import_from_board(tier3_state)
            generate_one_node(j, new_state, player, tree_index_dict, states, max_state_id)

    # depth 4 <- opp play
    # player = switch_player(player)
    # for i in tree_index_dict[0]:
    #     for j in tree_index_dict[i]:
    #         for k in tree_index_dict[j]:
    #             tier5_state = states[k]
    #             new_state = ChessBoard(3, 3)
    #             new_state.import_from_board(tier5_state)
    #             generate_one_node(k, new_state, player, tree_index_dict, states, max_state_id)
    #
    # # depth 5 <- us play
    # player = switch_player(player)
    # for i in tree_index_dict[0]:
    #     for j in tree_index_dict[i]:
    #         for k in tree_index_dict[j]:
    #             for l in tree_index_dict[k]:
    #                 tier3_state = states[l]
    #                 new_state = ChessBoard(3, 3)
    #                 new_state.import_from_board(tier3_state)
    #                 generate_one_node(l, new_state, player, tree_index_dict, states, max_state_id)

    pass


if __name__ == '__main__':
    dic = {"moves":[
                    {"moveX":"6", "moveY":"6","symbol":"O"},
                    {"moveX": "7", "moveY": "7","symbol":"X"},
                    {"moveX": "8", "moveY": "8","symbol":"O"},
        {"moveX": "8", "moveY": "9", "symbol": "X"},
                      ],
             "code":"OK"}

    c = ChessBoard(12,12)
    #c.import_from_moves(dic)
    c.import_from_moves(dic)
    current_player = 1
    mini_max(c, current_player)