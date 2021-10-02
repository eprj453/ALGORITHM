from pprint import pprint

dist = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def rotate_array_clockwise(arr):
    n, m, = len(arr), len(arr[0])
    rotated_arr = []
    for i in range(m):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(arr[j][i])
        rotated_arr.append(temp)

    return rotated_arr

def rotate_array_countclockwise(arr):
    n, m, = len(arr), len(arr[0])
    rotated_arr = []

    for i in range(m-1, -1, -1):
        temp = []
        for j in range(n):
            temp.append(arr[j][i])
        rotated_arr.append(temp)

    return rotated_arr


def get_distance(start, target):
    return [
        start[0] - target[0],
        start[1] - target[1]
    ]


def get_step(board, i, j, flag):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True

    start, step = [i, j], []

    q = [start]
    while q:
        x, y = q.pop(0)
        for d in dist:
            dx, dy = d

            x_dx, y_dy = x+dx, y+dy
            # print('xdx ydy : ', x_dx, y_dy)
            if 0 <= x_dx < n and 0 <= y_dy < n and \
                    board[x_dx][y_dy] == flag and not visited[x_dx][y_dy]:
                q.append([x_dx, y_dy])
                step.append(get_distance(start, [x+dx, y+dy]))
                visited[x_dx][y_dy] = True

    return sorted(step)


def mark_array(arr, i, j, flag):
    arr[i][j] = 2
    # print('eeee')
    n = len(arr)

    start = [i, j]
    q = [start]
    while q:
        x, y = q.pop()
        for d in dist:
            dx, dy = d
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if arr[x+dx][y+dy] == flag:
                    arr[x+dx][y+dy] = 2
                    q.append([x+dx, y+dy])

    return arr


def compare_with_table(board, table, step):
    n = len(board)
    rotate_count = 0
    # print('hello!')
    pprint(board)
    print()
    pprint(table)
    while rotate_count < 4:
        for i in range(n):
            for j in range(n):
                if table[i][j] == 1:
                    table_step = get_step(table, i, j, 1)
                    # print(i, j)
                    print(f'table_step : {table_step}')
                    # print()
                    if step == table_step:
                        table = mark_array(table, i, j, 1)
                        while rotate_count:
                            # print('hhh')
                            table = rotate_array_countclockwise(table)
                            rotate_count -= 1
                        return table

        table = rotate_array_clockwise(table)
        rotate_count += 1
    return False


# def mark_board(board, i, j):
#     n = len(board)
#
#     board[i][j] = 2
#     start = [i, j]
#     q = [start]
#
#     while q:
#         x, y = q.pop(0)
#         for d in dist:
#             dx, dy = d
#             if 0 <= x + dx < n and 0 <= y + dy < n:
#                 if board[x+dx][y+dy] == 0:
#                     board[x+dx][y+dy] = 2
#                     q.append([x+dx, y+dy])
#
#     return board


def solution(game_board, table):
    n = len(game_board)

    answer = 0
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                print(f'{i}, {j} is 0000!')
                step = get_step(game_board, i, j, 0)
                print(f'board step : {step}')
                result = compare_with_table(game_board, table, step)
                if result:
                    print(f'{i}, {j} is fit!')
                    print('======================')
                    answer += (len(step) + 1)
                    table = result

                game_board = mark_array(game_board, i, j, 0)
    return answer


a = solution(
        [
            [1,1,0,0,1,0],
            [0,0,1,0,1,0],
            [0,1,1,0,0,1],
            [1,1,0,1,1,1],
            [1,0,0,0,1,0],
            [0,1,1,1,0,0]],
        [
            [1,0,0,1,1,0],
            [1,0,1,0,1,0],
            [0,1,1,0,1,1],
            [0,0,1,0,0,0],
            [1,1,0,1,1,0],
            [0,1,0,0,0,0]
        ]
    )

# b = solution(
#     [
#         [0, 0, 0],
#         [1, 1, 0],
#         [1, 1, 1]
#     ],
#     [
#         [1, 1, 1],
#         [1, 0, 0],
#         [0, 0, 0]
#     ]
# )

print(
    a
)

'''
[[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
[[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
54
'''
