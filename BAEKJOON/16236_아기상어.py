def bfs(x, y, d):
    print(x, y)
    global min_distance
    global shark
    global can_eat

    if d > min_distance:
        return

    if d <= min_distance and maps[x][y] < shark and 0 < maps[x][y] < 7:
        if [d, x, y] not in can_eat:
            can_eat.append([d, x, y])
            print('append : ', d, x, y)
            min_distance = min(min_distance, d)
        return


    for k in range(len(dx)):
        if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n and 0 <= maps[x+dx[k]][y+dy[k]] < 7:
            if maps[x+dx[k]][y+dy[k]] <= shark and visited[x+dx[k]][y+dy[k]] == False:
                visited[x+dx[k]][y+dy[k]] = True
                bfs(x+dx[k], y+dy[k], d+1)
                visited[x+dx[k]][y+dy[k]] = False



n = int(input())
maps = []
fishes = []
visited = []
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
        if temp[j] != 0 and temp[j] != 9:
            fishes[temp[j]].append([i, j])
        if temp[j] == 9:
            shark_d = [i, j]
    maps.append(temp)
    visited.append([False] * n)
q = [shark_d]
visited[shark_d[0]][shark_d[1]] = True

# print(shark_d)

while True:
    can_eat = []
    min_distance = 20*20


    bfs(shark_d[0], shark_d[1], 0)

    if not can_eat:
        break
    move += min_distance
    can_eat.sort()
    print(can_eat)
    shark_d = [can_eat[0][1], can_eat[0][2]]
    print('shark_d : ', shark_d)
    visited[can_eat[0][1]][can_eat[0][2]] = True
    shark += can_eat[0][0]

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
