import sys
from collections import deque
sys.setrecursionlimit(10000000)

min_distance = 1000*1000
# def bfs(x, y, can_break, distance):
#     global min_distance
#
#     if distance >= min_distance:
#         return
#
#     if x == n-1 and y == m-1:
#         min_distance = min(min_distance, distance)
#         return
#
#     for k in range(4):
#         xk, yk = x + dx[k], y + dy[k]
#         if 0 <= xk < n and 0 <= yk < m:
#             # print(xk, yk)
#             if maps[xk][yk] == 1:
#                 if can_break == 1 and visited[xk][yk] == False:
#                     can_break = 0
#                     visited[xk][yk] = True
#                     bfs(xk, yk, can_break, distance+1)
#                     # visited[xk][yk] = False
#                     # can_break = 1
#             else:
#                 if visited[xk][yk] == False:
#                     visited[xk][yk] = True
#                     bfs(xk, yk, can_break, distance+1)
#                     # visited[xk][yk] = False
#
#



n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
min_distance = 1000*1000
q = deque()
# x, y, 부순적이 있는가, 부술수 있는가, distance
q.append([0, 0, 0, 1, 1])
visited[0][0] = True
go = True
while q and go:
    x, y, isBreaked, b, d = q[0][0], q[0][1], q[0][2], q[0][3], q[0][4]
    for k in range(4):
        xk, yk = x + dx[k] , y + dy[k]
        if 0 <= xk < n and 0 <= yk < m:
            if xk == n - 1 and yk == m - 1:
                min_distance = min(min_distance, d + 1)
                go = False
                break
            elif maps[xk][yk] == 1 and visited[xk][yk] == False:
                if isBreaked == 0 and b == True:
                    visited[xk][yk] = True
                    q.append([xk, yk, 1, False, d+1])
            elif maps[xk][yk] == 0 and visited[xk][yk] == False:
                visited[xk][yk] = True
                q.append([xk, yk, isBreaked, b, d+1])
    q.popleft()

print(min_distance if min_distance != 1000*1000 else -1)