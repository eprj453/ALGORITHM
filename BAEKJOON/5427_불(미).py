# for i in range(1, int(input())+1):
# #     w, h = map(int, input().split())
# #     start_x, start_y = 0, 0
# #     maps = []
# #     fires = []
# #     visited = []
# #     q = []
# #     dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# #     c = 0
# #     while c < h:
# #         temp = list(input())
# #         temp2 = [False] * w
# #         maps.append(temp)
# #         visited.append(temp2)
# #         for j in range(len(temp)):
# #             if temp[j] == '@':
# #                 start_x, start_y = c, j
# #                 visited[start_x][start_y] = True
# #             if temp[j] == '*':
# #                 q.append([c, j, 1, 0])
# #                 visited[c][j] = True
# #         c += 1
# #     q.append([start_x, start_y, 0, 0])
# #     min_distance = 0
# #     # 0 > 나, 1 > 불
# #     while q:
# #         x, y, which, count = q[0][0], q[0][1], q[0][2], q[0][3]
# #         if (x == 0 or y == 0 or x == h-1 or y == w-1) and which == 0:
# #             min_distance = count
# #             break
# #
# #         if which == 1:
# #             for k in range(len(dx)):
# #                 if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
# #                     if maps[x+dx[k]][y+dy[k]] == '.' and visited[x+dx[k]][y+dy[k]] == False:
# #                         q.append([x+dx[k], y+dy[k], which, count+1])
# #                         visited[x+dx[k]][y+dy[k]] = True
# #
# #             q.pop(0)
# #
# #
# #         elif which == 0:
# #             for k in range(len(dx)):
# #                 if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
# #                     if (x == 0 or y == 0 or x == h or y == w) and which == 0:
# #                         min_distance = count
# #                         break
# #                     if maps[x+dx[k]][y+dy[k]] != '#' and visited[x+dx[k]][y+dy[k]] == False:
# #                         q.append([x+dx[k], y+dy[k], which, count+1])
# #                         visited[x+dx[k]][y+dy[k]] = True
# #             q.pop(0)
# #
# #         if min_distance:
# #             break
# #     if min_distance == 0:
# #         print('IMPOSSIBLE')
# #     else:
# #         print(min_distance+1)

def fire_spread(my_q, fire_q):
    global distance
    # print('my_q : ', my_q)
    if len(my_q) == 0:
        return
    if len(fire_q) == 0:
        return

    my_new_q = []
    fire_new_q = []
    if fire_q:
        for i in range(len(fire_q)):
            x, y = fire_q[i][0], fire_q[i][1]
            for k in range(len(dx)):
                if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
                    if maps[x+dx[k]][y+dy[k]] != '#' and maps[x+dx[k]][y+dy[k]] != '*' and fire_visited[x+dx[k]][y+dy[k]] == False:
                        fire_visited[x+dx[k]][y+dy[k]] = True
                        maps[x+dx[k]][y+dy[k]] = '*'
                        fire_new_q.append([x+dx[k], y+dy[k]])
    # print('fire_new_q : ', fire_new_q)
    if my_q:
        for i in range(len(my_q)):
            x, y, z  = my_q[i][0], my_q[i][1], my_q[i][2]
            if x == 0 or y == 0 or x == h-1 or y == w-1:
                distance = min(distance, z+1)
                return
            for k in range(len(dx)):
                if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
                    if maps[x+dx[k]][y+dy[k]] == '.' and fire_visited[x+dx[k]][y+dy[k]] == False and my_visited[x+dx[k]][y+dy[k]] == False:
                        my_visited[x+dx[k]][y+dy[k]] = True
                        maps[x+dx[k]][y+dy[k]] = '@'
                        my_new_q.append([x+dx[k], y+dy[k], z+1])

    fire_spread(my_new_q, fire_new_q)



dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]
for l in range(int(input())):
    w, h = map(int, input().split())
    me, fire, maps, fire_visited, my_visited = [], [], [], [], []
    for j in range(h):
        temp = list(input())
        f_temp, m_temp = [False] * w, [False] * w
        fire_visited.append(f_temp)
        my_visited.append(m_temp)
        for k in range(w):
            if temp[k] == '@':
                me = [[j, k, 0]]
                my_visited[j][k] = True
            elif temp[k] == '*':
                fire.append([j, k])
                fire_visited[j][k] = True
        maps.append(temp)
    distance = 1000000
    fire_spread(me, fire)
    if distance == 1000000:
        print('IMPOSSIBLE')
    else:
        print(distance)


