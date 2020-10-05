def dijkstra(board, dijk, q, dir_dict):
    n = len(board)
    while q:
        x, y, value, d = q.pop(0)
        for dir in dir_dict.keys():
            dx, dy = x + dir[0], y + dir[1]
            if 0 <= dx < n and 0 <= dy < n and not board[dx][dy]:
                next_dir = dir_dict[dir]
                cost = 100 if d == next_dir else 600

                if dijk[dx][dy] >= value + cost or dijk[dx][dy] == -1:
                    dijk[dx][dy] = value + cost
                    q.append([dx, dy, value + cost, next_dir])

    return dijk[n - 1][n - 1]


def solution(board):
    answer = 0
    n = len(board)
    dijk = [[-1] * n for _ in range(n)]
    dijk[0][0] = 0
    dir_dict = {
        (0, 1): 1,
        (1, 0): 2,
        (0, -1): 3,
        (-1, 0): 4
    }

    result1 = dijkstra(board, dijk, [[0, 0, 0, 1]], dir_dict)
    result2 = dijkstra(board, dijk, [[0, 0, 0, 2]], dir_dict)

    return min(result1, result2)