def melt(melt_count):
    # print('함수호출')
    global min_melt
    #
    # if melt_count > min_melt:
    #     # min_melt = 0
    #     return

    visited = []
    melt_ice = []
    for i in range(n):
        temp = [False] * m
        temp2 = [0] * m
        visited.append(temp)
        melt_ice.append(temp2)

    temp_melt = 0
    result = False
    for i in range(n):
        if temp_melt >= 2:
            min_melt = min(min_melt, melt_count)
            return
        for j in range(m):
            if icebergs[i][j] != 0 and visited[i][j] == False:
                result = True
                q = [[i, j]]
                visited[i][j] = True
                while q:
                    ice_count = 0
                    x, y = q[0][0], q[0][1]
                    for k in range(len(dx)):
                        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
                            if icebergs[x+dx[k]][y+dy[k]] == 0:
                                ice_count += 1
                            elif icebergs[x+dx[k]][y+dy[k]] != 0 and visited[x+dx[k]][y+dy[k]] == False:
                                visited[x+dx[k]][y+dy[k]] = True
                                q.append([x+dx[k], y+dy[k]])
                    melt_ice[x][y] = ice_count
                    q.pop(0)
                temp_melt += 1

    for i in range(n):
        for j in range(m):
            icebergs[i][j] -= melt_ice[i][j]
            if icebergs[i][j] <= 0:
                icebergs[i][j] = 0
    #     print(icebergs[i])
    #
    # print(melt_count)
    # print()
    if result == False:
        min_melt = 0
        return

    # if temp_melt >= 2:
    #     min_melt = min(min_melt, melt_count)
    #     return

    else:
        melt(melt_count+1)




dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
n, m = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(n)]
min_melt = 10000
melt(0)
print(min_melt)


'''

8 8
0 0 0 0 0 0 0 0
0 4 5 0 0 0 0 0
0 0 3 3 0 0 0 0
0 0 0 4 3 0 0 0 
0 0 0 3 5 0 0 0
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0





'''


# def melt(melt_count):
#     # print('함수호출')
#     global min_melt
#
#     if melt_count > 10:
#         min_melt = 0
#         return
#
#     visited = []
#     melt_ice = []
#     for i in range(n):
#         temp = [False] * m
#         temp2 = [0] * m
#         visited.append(temp)
#         melt_ice.append(temp2)
#
#     temp_melt = 0
#     for i in range(n):
#         for j in range(m):
#             if icebergs[i][j] != 0 and visited[i][j] == False:
#                 q = [[i, j]]
#                 visited[i][j] = True
#                 while q:
#                     ice_count = 0
#                     x, y = q[0][0], q[0][1]
#                     for k in range(len(dx)):
#                         if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
#                             if icebergs[x+dx[k]][y+dy[k]] == 0:
#                                 ice_count += 1
#                             elif icebergs[x+dx[k]][y+dy[k]] != 0 and visited[x+dx[k]][y+dy[k]] == False:
#                                 visited[x+dx[k]][y+dy[k]] = True
#                                 q.append([x+dx[k], y+dy[k]])
#                     melt_ice[x][y] = ice_count
#                     q.pop(0)
#                 temp_melt += 1
#
#     for i in range(n):
#         for j in range(m):
#             icebergs[i][j] -= melt_ice[i][j]
#             if icebergs[i][j] <= 0:
#                 icebergs[i][j] = 0
#
#     if temp_melt >= 2:
#         min_melt = min(min_melt, melt_count)
#         return
#
#     else:
#         melt(melt_count+1)
#
#
#
#
# dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# n, m = map(int, input().split())
# icebergs = [list(map(int, input().split())) for _ in range(n)]
# min_melt = 10
# melt(0)
# print(min_melt)
