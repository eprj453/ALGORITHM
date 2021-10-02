import itertools
import copy

dists = [(0, 1), (1, 0), (0, -1), (-1, 0)]

min_press_count = 0xffffffff


def get_min_press(board, curr, target):
    n = len(board)
    cx, cy = curr
    q = [curr]
    # print(curr)
    dijk = [[0xffffff] * 4 for _ in range(4)]
    dijk[cx][cy] = 0

    if curr == target:
        return 1

    while q:
        # print(len(q))
        x, y = q.pop(0)
        # print(f'x, y : {x, y}')
        for d in dists:
            dx, dy = d
            if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                if dijk[x + dx][y + dy] > dijk[x][y] + 1:
                    dijk[x + dx][y + dy] = dijk[x][y] + 1
                    # print(f'append : {[x+dx, y+dy]}')
                    q.append([x + dx, y + dy])

            ctl_x, ctl_y = x, y
            # print('x ,y',x ,y)
            while True:
                # if not 0 <= ctl_x < 4 or not 0 <= ctl_y < 4:
                #     break

                if [ctl_x, ctl_y] != [x, y] and board[ctl_x][ctl_y] != 0:
                    break

                if ctl_x in [0, 3] or ctl_y in [0, 3]:
                    break

                ctl_x += dx
                ctl_y += dy

                # print('ctl_x, ctl_y', ctl_x, ctl_y)
                # print('ctl_x + dx, ctl_y + dy', ctl_x+dx, ctl_y+dy)
                # if not 0 <= ctl_x + dx < 4 or not 0 <= ctl_y + dy < 4:
                #     break
                # # print(ctl_x, ctl_y)
                # if board[ctl_x][ctl_y] != 0:
                #     # ctl_x += dx
                #     # ctl_y += dy
                #     break

            # print(ctl_x, ctl_y)
            if (ctl_x != x or ctl_y != y) and dijk[ctl_x][ctl_y] > dijk[x][y] + 1:
                dijk[ctl_x][ctl_y] = dijk[x][y] + 1
                q.append([ctl_x, ctl_y])

    # for d in range(4):
    #     print(dijk[d])
    # print()
    tx, ty = target
    return dijk[tx][ty] + 1


def card_move(board, card_pos, start):
    global min_press_count
    # print('========')
    # print(card_pos)
    # print(start)
    # print('========')
    press_count = 0
    curr = start
    # print(card_pos)
    board_copy = copy.deepcopy(board)

    for idx, pos in enumerate(card_pos):
        # if idx % 2:
        board_copy[card_pos[idx][0]][card_pos[idx][1]] = 0
        # board_copy[card_pos[idx - 1][0]][card_pos[idx - 1][1]] = 0
        # print(g)
        press_count += get_min_press(board_copy, curr, pos)
        if curr == pos:
            press_count -= 1
        curr = pos

    # print(press_count)
    min_press_count = min(min_press_count, press_count)


def get_path_by_recursive(board, card_pos, curr_pos, idx):
    if len(card_pos) <= idx:
        print(card_pos)
        card_move(board, card_pos, curr_pos)
        return

    # card = board[card_pos[idx][0]][card_pos[idx][1]]
    #
    # first_move = get_min_press(board, curr_pos, card_pos[idx])
    # second_move = get_min_press(board, card_pos[idx], card_pos[idx + 1])

    # curr = None if idx == len(card_pos) - 2 else card_pos[idx + 2]
    get_path_by_recursive(board, card_pos, curr_pos, idx + 2)

    card_pos[idx], card_pos[idx + 1] = card_pos[idx + 1], card_pos[idx]

    # first_move = get_min_press(board, curr_pos, card_pos[idx])
    # second_move = get_min_press(board, card_pos[idx], card_pos[idx + 1])
    get_path_by_recursive(board, card_pos, curr_pos, idx + 2)
    card_pos[idx], card_pos[idx + 1] = card_pos[idx + 1], card_pos[idx]


def get_card_pos(board, card):
    pos = []
    # print('board : ', board)
    for i in range(4):
        for j in range(4):
            if board[i][j] == card:
                pos.append([i, j])

    return pos


def get_all_card_pos(board, path, start):
    n = len(path)

    card_pos = []

    for card in path:
        # print()
        # print('aaaa', get_card_pos(board, card))
        for card_p in get_card_pos(board, card):
            card_pos.append(card_p)
        # card_pos.append(get_card_pos(board, p))
    # print('get_all_card_pos cardPos: ', card_pos)
    print(card_pos)
    get_path_by_recursive(board, card_pos, start, 0)
    # print(min_press_count)
    # append_all_card_pos(board, card_pos, 0)


def solution(board, r, c):
    answer = 0
    n = max(list(itertools.chain(*board)))
    start = [r, c]

    available_path_permutation = list(itertools.permutations([x for x in range(1, n + 1)], 3))

    for path in available_path_permutation:
        # print("path : ", path)
        get_all_card_pos(board, path, [r, c])

    return min_press_count
    # print(available_path_permutation)

    # print(min_press_count)
    # print()

    # print(get_min_press(board, [0, 3], [3, 0]))
    # return answer

    # for p in available_paths:
    #     print(p)
    # print(available_paths)


# solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)



print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1, 0))
