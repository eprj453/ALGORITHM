from collections import deque
# def search(x, y, cost):
#     global ans
#     if cost >= ans:
#         return
#     for k in range(4):
#         if x + dx[k] == n-1 and y + dy[k] == n-1:
#             ans = min(cost, ans)
#             return
#         else:
#             if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n and visited[x+dx[k]][y+dy[k]] == False:
#                 visited[x+dx[k]][y+dy[k]] = True
#                 search(x+dx[k], y+dy[k], cost + maps[x+dx[k]][y+dy[k]])
#                 visited[x+dx[k]][y+dy[k]] = False
#     return



dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(1, int(input())+1):
    ans = 10000
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited = [[False]*n for _ in range(n)]
    dijk = [[0xffffff] * n for _ in range(n)]
    dijk[0][0] = 0
    while q:
        x, y = q[0][0], q[0][1]
        # print(x, y)
        for k in range(len(dx)):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if dijk[nx][ny] > dijk[x][y] + maps[nx][ny]:
                    dijk[nx][ny] = dijk[x][y] + maps[nx][ny]
                    q.append([nx, ny])
        q.popleft()
    print('#{} {}'.format(i, dijk[n-1][n-1]))