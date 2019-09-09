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


def search(max, cctv, maps):
    global min_count
    if max >= len(cctv):
        count = 0
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
                    if temp[x+dx[i]][y+dy[i]] == 6:
                        break
                    elif temp[x+dx[i]][y+dy[i]] == 0:
                        temp[x+dx[i]][y+dy[i]] = '#'
                    x += dx[i]
                    y += dy[i]
                search(max+1, cctv, temp)

    elif cctv[max][0] == 2:
        for i in range(0, 2):
            temp = []
            for k in range(n):
                temp.append([])
                for l in range(m):
                    temp[k].append(maps[k][l])
            for j in range(i, len(dx), 2):
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
            for j in range(i, i+2):
                x, y = cctv[max][1], cctv[max][2]
                while 0 <= x + dx[j%4] < n and 0 <= y + dy[j%4] < m:
                    if temp[x + dx[j%4]][y + dy[j%4]] == 6:
                        break
                    elif temp[x + dx[j%4]][y + dy[j%4]] == 0:
                        temp[x + dx[j%4]][y + dy[j%4]] = '#'
                    x += dx[j%4]
                    y += dy[j%4]
            search(max + 1, cctv, temp)

    elif cctv[max][0] == 4:
        for i in range(len(dx)):
            temp = []
            for k in range(n):
                temp.append([])
                for l in range(m):
                    temp[k].append(maps[k][l])
            for j in range(i, i+3):
                x, y = cctv[max][1], cctv[max][2]
                while 0 <= x + dx[j%4] < n and 0 <= y + dy[j%4] < m:
                    if temp[x + dx[j%4]][y + dy[j%4]] == 6:
                        break
                    elif temp[x + dx[j%4]][y + dy[j%4]] == 0:
                        temp[x + dx[j%4]][y + dy[j%4]] = '#'
                    x += dx[j%4]
                    y += dy[j%4]
            search(max + 1, cctv, temp)

    elif cctv[max][0] == 5:
        temp = []
        for j in range(n):
            temp.append([])
            for k in range(m):
                temp[j].append(maps[j][k])
        for i in range(len(dx)):
            x, y = cctv[max][1], cctv[max][2]
            while 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
                # print(x+dx[i], y+dy[i])
                if temp[x+dx[i]][y+dy[i]] == 6:
                    break
                elif temp[x+dx[i]][y+dy[i]] == 0:
                    temp[x+dx[i]][y+dy[i]] = '#'
                x += dx[i]
                y += dy[i]
        search(max+1, cctv, temp)










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
print(min_count)


'''
4 5
0 2 0 0 0
0 0 0 0 0
0 0 4 0 0
0 5 0 0 0


'''