import time

def spread_virus(temp):
    global min_spread

    v_visited = []
    for i in range(n):
        v_temp = [False] * m
        v_visited.append(v_temp)

    for i in range(3):
        maps[temp[i][0]][temp[i][1]] = 1
    # print(maps)
    v_count = 0
    for vi in range(len(virus)):
        # if v_count >= min_spread:
        #     return
        v_x, v_y = virus[vi][0], virus[vi][1]
        v_visited[v_x][v_y] = True
        q = [[v_x, v_y]]
        while q:
            x, y = q[0][0], q[0][1]
            for k in range(len(dx)):
                if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
                    if maps[x+dx[k]][y+dy[k]] != 1 and v_visited[x+dx[k]][y+dy[k]] == False:
                        v_visited[x+dx[k]][y+dy[k]] = True
                        q.append([x+dx[k], y+dy[k]])
                        v_count += 1
            q.pop(0)
    # print(v_count)
    min_spread = min(min_spread, v_count)

    for i in range(3):
        maps[temp[i][0]][temp[i][1]] = 0

    return



def comb(k, start):
    if k == r:
        # print(temp)
        spread_virus(temp)
        return

    for i in range(start, len(walls)):
        temp.append(walls[i])
        comb(k+1, i+1)
        temp.pop()


start = time.time()
n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
maps = [list(map(int, input().split())) for _ in range(n)]
walls = []
virus = []
safes = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            walls.append([i, j])
            safes += 1
            # walls.append([i, j])
        if maps[i][j] == 2:
            virus.append([i, j])

# print(virus)
virus_spread = len(virus)
min_spread = 64
temp = []
r = 3
comb(0, 0)
print(safes)
print('virus_spread : ', virus_spread)
print('min_spread : ', min_spread)

# print(min_spread+virus_spread)
print(safes - (min_spread + 3))
# print(len(walls))
# for i in range(1 << len(walls)):
#     wall_temp = []
#     for j in range(i+1):
#         if i & (1 << j):
#             wall_temp.append(walls[j])
#     if len(wall_temp) == 3:
#         print(wall_temp)
print('time : {}'.format(time.time()-start))



'''
7 7
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0


'''