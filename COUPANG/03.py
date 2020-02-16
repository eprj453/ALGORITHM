dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
max_price = 0
def dijk(q):
    x, y, t = q[0][0], q[0][1], q[0][2]
    for k in range(4):
        xk, yk = x + dx[k], y + dy[k]
        if 0 <= xk < r and 0 <= yk < r:
            if di[xk][yk] < di[x][y] + delivery[xk][yk][0]:
                if t <= delivery[xk][yk][[1]]:
                    q.append([xk, yk, t+1])
                    max_price = max()


def solution(r, delivery):
    delev = [[]] * r
    n = 0
    for i in range(0, r):
        for j in range(0, r):
            delev[i][j] = delivery[n]
            n += 1
    print(delev)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    q = [[0, 0, 0]]
    di = [[0xfffffff, ] * r for _ in range(r)]
    max_price = 0
    while q:
        x, y, t = q[0][0], q[0][1], q[0][2]
        for k in range(4):
            xk, yk = x + dx[k], y + dy[k]
            if 0 <= xk < r and 0 <= yk < r:
                if di[xk][yk] < di[x][y] + delivery[xk][yk][0]:
                    if t <= delivery[xk][yk][[1]]:
                        q.append([xk, yk, t+1])
                        max_price = max()

print(solution(r, [[1, 5],[8, 3],[4, 2],[2, 3],[3, 1],[3, 2],[4, 2],[5, 2],[4, 1]]))