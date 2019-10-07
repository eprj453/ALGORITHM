import time

def spread_virus(temp):
    # print('active')
    global min_spread

    v_visited = []
    for i in range(n):
        v_temp = [False] * m
        v_visited.append(v_temp)

    # for i in range(3):
    #     maps[temp[i][0]][temp[i][1]] = 1

    v_count = 0
    result = True
    for vi in range(len(virus)):
        v_x, v_y = virus[vi][0], virus[vi][1]
        v_visited[v_x][v_y] = True
        q = [[v_x, v_y]]
        if v_count == -1:
            break
        while q:
            if v_count >= min_spread:
                v_count = -1
                break
            x, y = q[0][0], q[0][1]
            for k in range(len(dx)):
                if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
                    if maps[x+dx[k]][y+dy[k]] == 0 and v_visited[x+dx[k]][y+dy[k]] == False and [x+dx[k], y+dy[k]] not in temp:
                        v_visited[x+dx[k]][y+dy[k]] = True
                        q.append([x+dx[k], y+dy[k]])
                        v_count += 1
            q.pop(0)


    if v_count == -1:
        return
    else:
        min_spread = min(min_spread, v_count)
        return




def comb(k, start):
    global min_ans
    if k == r:
        spread_virus(temp)
        return

    for i in range(start, len(safe_zone)):
        temp.append(safe_zone[i])
        comb(k+1, i+1)
        temp.pop()


start = time.time()
n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
maps = [list(map(int, input().split())) for _ in range(n)]
virus = []
safe_zone = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            safe_zone.append([i, j])
        elif maps[i][j] == 2:
            virus.append([i, j])
min_spread = 64
temp = []
r = 3
comb(0, 0)
# print(safes)
# print('virus_spread : ', virus_spread)
# print('min_spread : ', min_spread)
# print('safe : ', safe)
# # print(min_spread+virus_spread)
# print('wall : ', wall+3)
# print('min_ans : ',min_ans)
print(len(safe_zone) - min_spread - 3)
# print(safes - (min_spread))
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