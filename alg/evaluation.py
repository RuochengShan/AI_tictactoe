import numpy as np


def switch_player1(player):
    if player == 1:
        return 2
    else:
        return 1


def check_block(search_list, player, start, end):
    left_block = False
    right_block = False
    if start == 0:
        left_block = True
    else:
        if end == len(search_list):
            right_block = True
        else:
            if search_list[start - 1] == switch_player1(player):
                left_block = True
            if search_list[end] == switch_player1(player):
                right_block = True

    if left_block and right_block:
        return 2
    elif left_block or right_block:
        return 1
    else:
        return 0


def search_continues(player, times, search_list, base_score):
    v = player
    n = times
    v_list = [v] * n
    start = 0
    end = start + n
    count = 0
    score = 0
    one_block = base_score*0.2
    two_block = base_score*0.8
    while end <= len(search_list):
        check_list = search_list[start:end]
        block = check_block(search_list, player, start, end)
        if check_list == v_list:
            count += 1
            score += base_score
            if block == 1:
                score -= one_block
            if block == 2:
                score -= two_block

        start += 1
        end += 1
    return score


def evaluate_score(array, player):

    array = list(array)

    # 6
    count_6 = search_continues(player, 6, array, 100000)
    count_6_opp = search_continues(switch_player1(player), 6, array, 100000)
    count_5 = search_continues(player, 5, array, 50000)
    count_5_opp = search_continues(switch_player1(player), 5, array, 50000)
    count_4 = search_continues(player, 4, array, 1000)
    count_4_opp = search_continues(switch_player1(player), 4, array, 1000)
    count_3 = search_continues(player, 3, array, 200)
    count_3_opp = search_continues(switch_player1(player), 3, array, 200)
    count_2 = search_continues(player, 2, array, 10)
    count_2_opp = search_continues(switch_player1(player), 2, array, 10)

    score = count_6 + count_5 + count_4 + count_3 + count_2
    score_opp = count_6_opp + count_5_opp + count_4_opp + count_3_opp + count_2_opp
    score = score - score_opp*0.8
    return score


def evaluation_state(state, player):
    """

    :param state: np 12x12
    :param player: int 1 or 2
    :return: value as int
    """
    score = 0
    score += np.count_nonzero(state == player)
    checked_column = []
    rightdown_leftup = []
    rightup_leftdown = []
    for i in range(len(state)):
        row = state[i]
        score += evaluate_score(row, player)
        for j in range(len(state)):
            column = state[:, j]
            if j not in checked_column:
                checked_column.append(j)
                score += evaluate_score(column, player)
            a = []
            b = []
            a.append(state[i, j])
            b.append(state[i, j])

            if [i, j] not in rightdown_leftup:
                index1 = 1
                while index1 < len(state):
                    right_down_x = i + index1
                    right_down_y = j + index1
                    if i != right_down_x and j != right_down_y:
                        if right_down_x < len(state) and right_down_y < len(state):
                            a.append(state[right_down_x, right_down_y])
                            rightdown_leftup.append([right_down_x, right_down_y])

                    left_up_x = i - index1
                    left_up_y = j - index1
                    if i != left_up_x and j != left_up_y:
                        if left_up_x >= 0 and left_up_y >= 0:
                            a.append(state[left_up_x, left_up_y])
                            rightdown_leftup.append([left_up_x, left_up_y])
                    index1 += 1
                rightdown_leftup.append([i, j])

            if [i, j] not in rightup_leftdown:
                index2 = 1
                while index2 < len(state):
                    left_down_x = i - index2
                    left_down_y = j + index2
                    if i != left_down_x and j != left_down_y:
                        if left_down_x >= 0 and left_down_y < len(state):
                            b.append(state[left_down_x, left_down_y])
                            rightup_leftdown.append([left_down_x, left_down_y])
                    right_up_x = i + index2
                    right_up_y = j - index2
                    if i != right_up_x and j != right_up_y:
                        if right_up_x < len(state) and right_up_y >= 0:
                            b.append(state[right_up_x, right_up_y])
                            rightup_leftdown.append([right_up_x, right_up_y])
                    index2 += 1
                rightup_leftdown.append([i, j])

            if len(a) > 1:
                score += evaluate_score(a, player)
            if len(b) > 1:
                score += evaluate_score(b, player)

    return score


if __name__ == '__main__':
    import numpy as np
    state = np.array([
        [1,2,3,4,5],
        [6,7,8,9,0],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,26]
    ])
    a = evaluation_state(state, 1)
    print(a)