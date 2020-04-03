from alg.chessboard import ChessBoard
from alg.evaluation import evaluation_state
import numpy as np


def alpha_beta_pruning1(tier1_index, tier2_index, tier3_index, states, next_move_dict, current_player):
    if len(next_move_dict) == 1:
        for i in next_move_dict:
            return next_move_dict[i]
    time1 = 0
    t2_score = 100000
    t2_eva_index = {}
    best_move_index = 0
    for i in tier1_index[0]:
        t2_eva_index[i] = 0
        if time1 == 0:
            t3_score = -100000
            t2_eva = {}
            time2 = 0
            for j in tier2_index[i]:
                if time2 == 0:
                    for k in tier3_index[j]:
                        e_state = states[k]
                        score = evaluation_state(e_state, current_player)
                        if score >= t3_score:
                            t2_eva[j] = score
                            t3_score = score
                    time2 += 1
                else:
                    for k in tier3_index[j]:
                        e_state = states[k]
                        score = evaluation_state(e_state, current_player)
                        t2_eva[j] = score
                        if score >= t3_score:
                            break
                        else:
                            t3_score = score
                if t3_score < t2_score:
                    t2_score = t3_score
                    t2_eva_index[i] = t2_score

        else:
            t3_score1 = -100000
            t2_eva1 = {}
            time2 = 0
            for j in tier2_index[i]:
                if time2 == 0:
                    for k in tier3_index[j]:
                        e_state = states[k]
                        score = evaluation_state(e_state, current_player)
                        if score >= t3_score1:
                            t2_eva1[j] = score
                            t3_score1 = score
                    time2 += 1
                else:
                    for k in tier3_index[j]:
                        e_state = states[k]
                        score = evaluation_state(e_state, current_player)
                        t2_eva1[j] = score
                        if score >= t3_score1:
                            best_move_index = i
                            break
                        else:
                            t3_score1 = score
                if t3_score1 < t2_score:
                    t2_score = t3_score1
                    t2_eva_index[i] = t2_score
                    best_move_index = i
                    break
        time1 += 1
    best_move = next_move_dict[best_move_index]
    return best_move


def alpha_beta_pruning(tier1_index, tier2_index, tier3_index, states, next_move_dict, current_player):
    tier3_states_eva = {}
    # max for tier3
    for tier3_id in tier3_index:
        tier3_states_eva[tier3_id] = -200000
        for t3 in tier3_index[tier3_id]:
            score = evaluation_state(states[t3], current_player)
            if score >= tier3_states_eva[tier3_id]:
                tier3_states_eva[tier3_id] = score
                break
    # min for tier2
    tier2_states_eva = {}
    for tier2_id in tier2_index:
        tier2_states_eva[tier2_id] = 200000
        for t2 in tier2_index[tier2_id]:
            score = tier3_states_eva[t2]
            if score <= tier2_states_eva[tier2_id]:
                tier2_states_eva[tier2_id] = score
                break

    best_move_index = 0
    best_move = "0,0"
    tier1_states_eva = {}
    for tier1_id in tier1_index:
        tier1_states_eva[tier1_id] = 0
        for t1 in tier1_index[tier1_id]:
            score = tier2_states_eva[t1]
            if score >= tier1_states_eva[tier1_id]:
                tier1_states_eva[tier1_id] = score
                best_move_index = t1
                best_move = next_move_dict[best_move_index]
    return best_move


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


def generate_one_node(currentstate_id, chessboard, currentplayer, tree_dict, states_dic, max_state_id, next_move_dict=None, round=0, count=0):
    next_states, count1 = chessboard.create_next_states(currentplayer, round)

    tree_dict[currentstate_id] = []
    states_dic[currentstate_id] = chessboard.board
    max_id = max_state_id[-1]
    for i in next_states:
        max_id += 1
        tree_dict[currentstate_id].append(max_id)
        states_dic[max_id] = i[0]
        max_state_id.append(max_id)
        if round == 1:
            next_move_dict[max_id] = i[1]

        sorted(max_state_id)


def mini_max_alg(chessboard: ChessBoard, current_player):
    # return the next place coordinate
    states = {}
    tier1_index = {}
    player = current_player
    max_state_id = [0]
    count_max = [0]
    current_state_id = max_state_id[-1]
    next_move_dict = {}

    # depth 1 <- us play
    generate_one_node(current_state_id, chessboard, player, tier1_index, states, max_state_id, next_move_dict, 1)
    #del states[0]
    # depth 2 <- opp play
    tier2_index = {}
    player = switch_player(player)
    for i in tier1_index[0]:
        new_state = ChessBoard(12, 12)
        new_state.import_from_board(states[i])
        generate_one_node(i, new_state, player, tier2_index, states, max_state_id)
        del states[i]

    # depth 3 <- us play
    tier3_index = {}
    player = switch_player(player)
    for i in tier2_index:
        for j in tier2_index[i]:
            new_state = ChessBoard(12, 12)
            new_state.import_from_board(states[j])
            count = len(states)
            generate_one_node(j, new_state, player, tier3_index, states, max_state_id, count)
            del states[j]

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
    next_move = alpha_beta_pruning(tier1_index, tier2_index, tier3_index, states, next_move_dict, current_player)
    return next_move


if __name__ == '__main__':
    dic = {"moves":[
                    {"moveX":"1", "moveY":"1","symbol":"O"},
                    {"moveX": "1", "moveY": "2","symbol":"X"},
                    {"moveX": "2", "moveY": "2","symbol":"O"},
        {"moveX": "0", "moveY": "0", "symbol": "X"},
                      ],
             "code":"OK"}

    c = ChessBoard(12, 6)
    c.place_chess(5, 5, 1)
    c.place_chess(6, 6, 2)
    c.place_chess(5, 6, 1)
    #c.import_from_moves(dic)
    #c.import_from_moves(dic)
    current_player = 2
    #next_move = mini_max_alg(c, current_player)
    c.place_chess(7, 5, 2)
    c.place_chess(5, 7, 1)
    next_move1 = mini_max_alg(c, current_player)
    pass