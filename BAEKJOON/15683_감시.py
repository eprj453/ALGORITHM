# def perm(k, temp):
# # #     global min_count
# # #     if k >= l:
# # #         maps_temp = maps
# # #         print(temp)
# # #         c = 0
# # #         for i in range(n):
# # #             for j in range(m):
# # #                 if visited[i][j] == False and maps[i][j] != 0 and maps[i][j] != 6:
# # #                     visited[i][j] == True
# # #                     x, y = i, j
# # #                     for
# # #
# # #         # # c += 1
# # #         # c = 0
# # #         # temp_count = 0
# # #         # for i in range(n):
# # #         #     for j in range(m):
# # #         #         if maps_temp[i][j] == 1:
# # #         #             x, y = i, j
# # #         #             while 0 <= x < n and 0 <= y < n: #
# # #         #                 if maps_temp[x + temp[c][0]][y + temp[c][1]] == 6:
# # #         #                     break
# # #         #                 else:
# # #         #                     maps_temp[x + temp[c][0]][y + temp[c][1]] = '#'
# # #         #                 x += temp[c][0]
# # #         #                 y += temp[c][1]
# # #         #             c += 1
# # #         #
# # #         #         elif maps_temp[i][j] == 2:
# # #         #             temp2 = [temp[c][0], [-(temp[c][0]), -(temp[c][1])]]
# # #         #             for t in temp2:
# # #         #                 x, y = i, j
# # #         #                 while 0 <= x < n and 0 <= y < n:
# # #         #                     if maps_temp[x + t[0]][y+t[1]] == 6:
# # #         #                         break
# # #         #                     else:
# # #         #                         maps_temp[x + t[0]][y+t[1]] = '#'
# # #         #                 x += t[0]
# # #         #                 y += t[1]
# # #         #             c += 1
# # #         #         elif maps_temp[i][j] == 3:
# # #         #         elif maps_temp[i][j] == 4:
# # #         #         elif maps_temp[i][j] == 5:
# # #
# # #
# # #
# # #
# # #     else:
# # #         for i in range(k, len(cctv)):
# # #             for j in range(len(cctv[i])):
# # #                 temp[k] = cctv[i][j]
# # #                 # print(temp)
# # #                 perm(k+1, temp)
# # #             return


# def search(maps):
#     global min_count
#     for k in range(n):
#         for j in range(m):
#             if maps[k][j] != 0 and maps[k][j] != 6 and maps[k][j] != '#' and visited[k][j] == False:
#                 x, y = k, j
#                 visited[k][j] = True
#                 if maps[x][y] == 1:
#                     for i in range(len(dx)):
#                         maps_temp = []
#                         for b in range(n):
#                             maps_temp.append([])
#                         for b in range(n):
#                             for g in range(m):
#                                 maps_temp[b].append(maps[b][g])
#                         if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
#                             while 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
#                                 if maps_temp[x+dx[i]][y+dy[i]] == 6:
#                                     break
#                                 if maps_temp[x+dx[i]][y+dy[i]] == 0:
#                                     maps_temp[x+dx[i]][y+dy[i]] = '#'
#                                 x += dx[i]
#                                 y += dy[i]
#                             x, y = k, j
#                             # print(i, maps_temp)
#                             search(maps_temp)
#
#                 elif maps[x][y] == 2:
#                     maps_temp = []
#                     for b in range(n):
#                         maps_temp.append([])
#                     for b in range(n):
#                         for g in range(m):
#                             maps_temp[b].append(maps[b][g])
#                     for i in range(0, len(dx), 2):
#                         if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
#                             for j in range(i, i+2):
#                                 while 0 <= x + dx[j] < n and 0 <= y + dy[j] < n:
#                                     if maps_temp[x + dx[j]][y+dy[j]] == 6:
#                                         break
#                                     if maps_temp[x + dx[j]][y + dy[j]] == 0:
#                                         maps_temp[x+dx[j]][y+dy[j]] = '#'
#                                     x += dx[j]
#                                     y += dy[j]
#                             search(maps_temp)
#
#                 elif maps[x][y] == 3:
#                     for i in range(len(dx)):
#                         maps_temp = []
#                         for b in range(n):
#                             maps_temp.append([])
#                         for b in range(n):
#                             for g in range(m):
#                                 maps_temp[b].append(maps[b][g])
#                         if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n:
#                             for j in range(i, i+2):
#                                 while 0 <= x + dx[j] < n and 0 <= y + dy[j] < n:
#                                     if maps_temp[x + dx[j]][y+dy[j]] == 6:
#                                         break
#                                     if maps_temp[x + dx[j]][y + dy[j]] == 0:
#                                         maps_temp[x+dx[j]][y+dy[j]] = '#'
#                                     x += dx[j]
#                                     y += dy[j]
#                             search(maps_temp)
#
#                 elif maps[x][y] == 4:
#                     for i in range(len(dx)):
#                         maps_temp = []
#                         for b in range(n):
#                             maps_temp.append([])
#                         for b in range(n):
#                             for g in range(m):
#                                 maps_temp[b].append(maps[b][g])
#                         if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
#                             for j in range(i, i+3):
#                                 while 0 <= x + dx[j%4] < n and 0 <= y + dy[j%4] < n:
#                                     if maps_temp[x + dx[j%4]][y + dy[j%4]] == 6:
#                                         break
#                                     if maps_temp[x + dx[j%4]][y + dy[j%4]] == 0:
#                                         maps_temp[x + dx[j%4]][y + dy[j%4]] = '#'
#                                     x += dx[j%4]
#                                     y += dy[j%4]
#                             search(maps_temp)
#
#                 elif maps[x][y] == 5:
#                     maps_temp = []
#                     for b in range(n):
#                         maps_temp.append([])
#                     for b in range(n):
#                         for g in range(m):
#                             maps_temp[b].append(maps[b][g])
#                     for i in range(len(dx)):
#                         if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
#                             while 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
#                                 if maps_temp[x + dx[i]][y + dy[i]] == 6:
#                                     break
#                                 if maps_temp[x + dx[i]][y + dy[i]] == 0:
#                                     maps_temp[x + dx[i]][y + dy[i]] = '#'
#                                 x += dx[i]
#                                 y += dy[i]
#                         search(maps_temp)
#     print(maps)
#     z_count = 0
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] == 0:
#                 z_count += 1

    # min_count = min(min_count, z_count)

def search(max, cctv, maps):
    global min_count
    if max >= len(cctv):
        count = 0
        print(maps)
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    count += 1
        min_count = min(min_count, count)
        return
    if cctv[max][0] == 1:
        for i in range(len(dx)):
            x, y = cctv[max][1], cctv[max][2]
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                temp = []
                for j in range(n):
                    temp.append([])
                    for k in range(m):
                        temp[j].append(maps[j][k])
                while 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
                    # print(x+dx[i], y+dy[i])
                    if temp[x+dx[i]][y+dy[i]] == 6:
                        break
                    elif temp[x+dx[i]][y+dy[i]] == 0:
                        temp[x+dx[i]][y+dy[i]] = '#'
                    x += dx[i]
                    y += dy[i]
                search(max+1, cctv, temp)

    elif cctv[max][0] == 2:
        for i in range(0, len(dx), 2):
            temp = []
            for k in range(n):
                temp.append([])
                for l in range(m):
                    temp[k].append(maps[k][l])
            for j in range(i, i+2):
                x, y = cctv[max][1], cctv[max][2]
                while 0 <= x+dx[j] < n and 0 <= y+dy[j] < m:
                    if temp[x+dx[j]][y+dy[j]] == 6:
                        break
                    elif temp[x+dx[j]][y+dy[j]] == 0:
                        temp[x+dx[j]][y+dy[j]] = '#'
                    x += dx[j]
                    y += dy[j]
            search(max+1, cctv, temp)

    elif cctv[max][0] == 3:
        for i in range(len(dx)):
            temp = []
            for k in range(n):
                temp.append([])
                for l in range(m):
                    temp[k].append(maps[k][l])
            for j in range(i, i+1):
                x, y = cctv[max][1], cctv[max][2]
                if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                    while 0 <= x + dx[j%4] < n and 0 <= y + dy[j%4] < m:
                        if temp[x + dx[j%4]][y + dy[j%4]] == 6:
                            break
                        elif temp[x + dx[j%4]][y + dy[j%4]] == 0:
                            temp[x + dx[j%4]][y + dy[j%4]] = '#'
                        x += dx[j%4]
                        y += dy[j%4]
            search(max + 1, cctv, temp)










dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cctv = []
min_count = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] != 0 and maps[i][j] != 6:
            cctv.append([maps[i][j], i, j])
        if maps[i][j] == 0:
            min_count += 1
search(0, cctv, maps)
# print(cctv)
print(min_count)


'''
3 5
0 2 0 0 0
0 0 0 0 0
0 0 2 0 0



'''