def solution(board):
    answer = 0
    n = len(board)
    dijk = [[n**2 * 500] * n for _ in range(n)]
    dijk[0][0] = 0
    dir_dict = {
        (0 ,1): 1,
        (1, 0): 2,
        (0, -1): 3,
        (-1, 0): 4
    }

    q = [[0, 0, 0]]

    while q:
        x, y, d = q.pop(0)
        for dir in dir_dict.keys():
            dx, dy = x + dir[0], y + dir[1]
            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] == 0:
                if d == 0 or d == dir_dict[dir]:
                    cost = 100
                    next_dir = dir_dict[dir] if d == 0 else d
                else:
                    cost = 600
                    next_dir = dir_dict[dir]
                if dijk[dx][dy] >= dijk[x][y] + cost:
                    dijk[dx][dy] = dijk[x][y] + cost
                    q.append([dx, dy, dir_dict[dir]])

                # else:
                #     if dijk[dx][dy] >= dijk[x][y] + 600:
                #         dijk[dx][dy] = dijk[x][y] + 600
                #         q.append([dx, dy, dir_dict[dir]])

    for dij in dijk:
        print(dij)
    answer = dijk[n-1][n-1]

    return answer

# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0]]))

# arr = solution(([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))