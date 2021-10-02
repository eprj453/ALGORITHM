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


def mark_array_with_trace(arr, start, trace):
    x, y = start
    arr[x][y] = 1

    n = len(arr)

    q = [start]
    while q:
        x, y = q.pop()
        for d in dist:
            dx, dy = d
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if arr[x+dx][y+dy] == 0:
                    arr[x+dx][y+dy] = 1
                    q.append([x+dx, y+dy])

    return arr


def tracking_table(table, trace):
    n = len(table)

    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if 0 <= i < n and 0 <= j < n:
                if table[i][j] == 1:
                    table_trace = trace_step(table, i, j)
                    if len(trace) == len(table_trace) and trace == table_trace:
                        table = mark_table_with_trace(table, [i, j], table_trace)
                        table =







def compare_board_and_table(board, table, trace):
    rotate_count = 0
    for _ in range(4):
        rotated_board = rotate_array_clockwise(board)

        rotate_count += 1

    pass



def trace_step(board, i, j):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True
    # for k in range(n):
    #     print(visited[k])

    start = [i, j]
    stack = [start]

    step = []
    while stack:
        x, y = stack[-1]
        # print(stack)
        for d in dist:
            dx, dy = d

            x_dx, y_dy = x+dx, y+dy
            # print('xdx ydy : ', x_dx, y_dy)
            if 0 <= x_dx < n and 0 <= y_dy < n:
                if board[x_dx][y_dy] == 1 and not visited[x_dx][y_dy]:
                    # print('gg')
                    stack.append([x_dx, y_dy])
                    step.append([dx, dy])
                    visited[x_dx][y_dy] = True
                    break
        else:
            stack.pop()
    return step


def mark_board(board, i, j):
    n = len(board)

    board[i][j] = 0
    start = [i, j]
    q = [start]

    while q:
        x, y = q.pop(0)
        for d in dist:
            dx, dy = d
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if board[x+dx][y+dy] == 1:
                    board[x+dx][y+dy] = 0
                    q.append([x+dx, y+dy])

    return board



def solution(game_board, table):
    answer = -1
    n = len(game_board)
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 1:
                trace = trace_step(game_board, i, j)

    return answer


# print(rotate_array([[1, 2, 3],[4, 5, 6]]))


# solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])