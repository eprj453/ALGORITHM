
# from collections import deque
#
# col, row = map(int, input().split())
# maps = [list(input()) for _ in range(col)]
# print(maps)
# q = deque()
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# visited = [[False] * row for _ in range(col)]
# # print(visited)
# # for i in range(col):
# #     visited.append([False] * row)
# max_val = 0
# for i in range(col):
#     for j in range(row):
#         if maps[i][j] == 'L':
#             print('find : ',i, j)
#             q.append([i,j,0])
#             # x, y = q[0][0], q[0][1]
#             visited[i][j] = True
#             while len(q) > 0:
#                 print(q)
#                 for k in range(len(dx)):
#                     if q[0][0] + dx[k] >= 0 and q[0][0] + dx[k] < col and q[0][1] + dy[k] >= 0 and q[0][1] + dy[k] < row:
#                         if maps[q[0][0]+dx[k]][q[0][1]+dy[k]] == 'L' and visited[q[0][0]+dx[k]][q[0][1]+dy[k]] == False:
#                            q.append([q[0][0]+dx[k], q[0][1]+dy[k], q[0][2]+1])
#                            print(q[0][2]+1)
#                            visited[q[0][0]+dx[k]][q[0][1]+dy[k]] = True
#                            print(visited)
#                            if q[0][2] > max_val:
#                                max_val = q[0][2]
#                 q.popleft()
#
#             for k in range(col):
#                 for l in range(row):
#                     visited[k][l] = False
#
# print(max_val+1)

from collections import deque

col, row = map(int, input().split())
maps = [list(input()) for _ in range(col)]
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * row for _ in range(col)]
max_val = 0
for i in range(col):
    for j in range(row):
        if maps[i][j] == 'L':

            q.append([i,j,0])
            visited[i][j] = True
            while len(q) > 0:
                for k in range(len(dx)):
                    if q[0][0] + dx[k] >= 0 and q[0][0] + dx[k] < col and q[0][1] + dy[k] >= 0 and q[0][1] + dy[k] < row:
                        if maps[q[0][0]+dx[k]][q[0][1]+dy[k]] == 'L' and visited[q[0][0]+dx[k]][q[0][1]+dy[k]] == False:
                           q.append([q[0][0]+dx[k], q[0][1]+dy[k], q[0][2]+1])
                           visited[q[0][0]+dx[k]][q[0][1]+dy[k]] = True
                           if q[0][2]+1 > max_val:
                               max_val = q[0][2]+1

            # print('find : ',i,j)
            q.append([i,j,0])
            visited[i][j] = True
            while len(q) > 0:
                # print(q[0])
                for k in range(len(dx)):
                    if q[0][0] + dx[k] >= 0 and q[0][0] + dx[k] < col and q[0][1] + dy[k] >= 0 and q[0][1] + dy[k] < row:
                        if maps[q[0][0]+dx[k]][q[0][1]+dy[k]] == 'L' and \
                            visited[q[0][0]+dx[k]][q[0][1]+dy[k]] == False:
                           q.append([q[0][0]+dx[k], q[0][1]+dy[k], q[0][2]+1])
                           visited[q[0][0]+dx[k]][q[0][1]+dy[k]] = True
                           if q[0][2] > max_val:
                               max_val = q[0][2]
                               # print('max_val : ', max_val)

                q.popleft()

            for k in range(col):
                for l in range(row):
                    visited[k][l] = False

print(max_val+1)

