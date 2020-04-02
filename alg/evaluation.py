from alg.minimax import switch_player


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
        if check_list == v_list:
            count += 1
            score += base_score
            if start - 1 < 0:
                # left at edge
                if search_list[end + 1] == switch_player(player):
                    # right is opp
                    score -= two_block
                else:
                    score -= one_block

            elif end == len(search_list):
                # right at edge
                if search_list[start - 1] == switch_player(player):
                    score -= two_block
                else:
                    score -= one_block

            elif search_list[start - 1] == switch_player(player) or search_list[end + 1] == switch_player(player):
                # one side block by opp
                score -= one_block
            elif search_list[start - 1] == switch_player(player) and search_list[end + 1] == switch_player(player):
                # two side block by opp
                score -= two_block
        start += 1
        end += 1
    return score


def evaluate_score(array, player):

    array = list(array)
    score = 0
    # 6
    count_6 = search_continues(player, 6, array, 1000)
    count_5 = search_continues(player, 5, array, 500)
    count_4 = search_continues(player, 4, array, 100)
    count_3 = search_continues(player, 3, array, 20)
    count_2 = search_continues(player, 2, array, 10)
    score = score + count_6 + count_5 + count_4 + count_3 + count_2
    return score


def evaluation(state, player):
    """

    :param state: np 12x12
    :param player: int 1 or 2
    :return: value as int
    """
    score = 0

    checked_column = []
    rightdown_leftup = []
    rightup_leftdown = []
    for i in range(12):
        row = state[i]
        score += evaluate_score(row, player)
        for j in range(12):
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
                while index1 < 4:
                    right_down_x = i + index1
                    right_down_y = j + index1
                    if i != right_down_x and j != right_down_y:
                        if right_down_x < 4 and right_down_y < 4:
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
                while index2 < 4:
                    left_down_x = i - index2
                    left_down_y = j + index2
                    if i != left_down_x and j != left_down_y:
                        if left_down_x >= 0 and left_down_y < 4:
                            b.append(state[left_down_x, left_down_y])
                            rightup_leftdown.append([left_down_x, left_down_y])
                    right_up_x = i + index2
                    right_up_y = j - index2
                    if i != right_up_x and j != right_up_y:
                        if right_up_x < 4 and right_up_y >= 0:
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
    state = np.array([[1, 1, 1, 2,1], [0, 0, 0, 2,1], [0, 0, 0, 0,1], [1, 1, 2, 2,1]])
    a = evaluation(state, 1)
    print(a)