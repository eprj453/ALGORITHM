def bfs(x, y):
    # print(x, y)
    global min_distance
    global shark
    global can_eat
    d = (abs(shark_d[0] - x) + abs(shark_d[1] - y))
    if d > min_distance:
        return

    if maps[x][y] < shark and 0 < maps[x][y] < 7:
        # print('min_dis : ', min_distance)
        # print('can_eat : ', can_eat)
        # print()
        if not can_eat:
            can_eat = [x, y]
            min_distance = d
            return
        else:
            if d < min_distance:
                can_eat = [x, y]
                min_distance = d

            elif d == min_distance:
                if can_eat[0] > x or (can_eat[0] == x and can_eat[1] > y): # 더 위에 있는 물고기
                    can_eat = [x, y]
            return
            # if d < min_distance:
            #     can_eat = [x, y]
            #     min_distance = d
            #     return
            # elif d == min_distance:
            #     if can_eat[0] > x or (can_eat[0] == x and can_eat[1] > y):
            #         can_eat = [x, y]
            #         # min_distance = min(min_distance, (abs(shark_d[0] - x) + abs(shark_d[1] - y)))
            #     print('can_eat : ', can_eat)
            # return


    for k in range(len(dx)):
        if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n and 0 <= maps[x+dx[k]][y+dy[k]] < 7:
            if maps[x+dx[k]][y+dy[k]] <= shark and visited[x+dx[k]][y+dy[k]] == False:
                visited[x+dx[k]][y+dy[k]] = True
                bfs(x+dx[k], y+dy[k])
                visited[x+dx[k]][y+dy[k]] = False




n = int(input())
maps = []
fishes = []
# visited = []
for _ in range(8):
    temp = []
    fishes.append(temp)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
shark = 2
shark_d = [0, 0]
move = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 9:
            shark_d = [i, j]
    maps.append(temp)
eat_fishes = 0
while True:
    can_eat = []
    min_distance = 20*20
    visited = []
    for _ in range(n):
        visited.append([False] * n)

    visited[shark_d[0]][shark_d[1]] = True

    bfs(shark_d[0], shark_d[1])

    if not can_eat:
        break
    print(can_eat)

    # print('shark_d : ', shark_d)
    # visited[can_eat[0]][can_eat[1]] = True
    move += (abs(can_eat[0] - shark_d[0]) + abs(can_eat[1]-shark_d[1]))
    maps[shark_d[0]][shark_d[1]] = 0
    shark_d = [can_eat[0], can_eat[1]]
    eat_fishes += 1
    if shark == eat_fishes:
        # print('shark += 1!')
        shark += 1
        # print('shark : ',shark)
        eat_fishes = 0
    maps[can_eat[0]][can_eat[1]] = 0
    for i in range(n):
        print(maps[i])
    # print()
    # print('move : ',move)
    # print('shark_d : ',shark_d)
    print('shark : ',shark)
    print('move : ',move)
print(move)
    # print(can_eat)
    # print(min_distance)


# while True:
#     can_eat = []
#     for i in range(n):
#         for j in range(n):
#             if 0 < maps[i][j] < 7 and maps[i][j] <= shark:
#                 can_eat.append([abs(shark_d[0] - i) + abs(shark_d[1] - j), i, j])
#
#     print(sorted(can_eat))

    # min_distance = 20
    # while q:
    #     x, y = q[0][0], q[0][1]
    #     for k in range(len(dx)):
    #         if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n:
    #

    # can_eat = []
    # for fish in fishes:
    #     if fish:
    #         can_eat.append([abs(fish[0], fish[1]]))



# print(fishes)
