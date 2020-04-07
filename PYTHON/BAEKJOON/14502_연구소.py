# import time
#
# def spread_virus(temp):
#     # print('active')
#     global min_spread
#
#     v_visited = []
#     for i in range(n):
#         v_temp = [False] * m
#         v_visited.append(v_temp)
#
#     v_count = 0
#     for vi in range(len(virus)):
#         v_x, v_y = virus[vi][0], virus[vi][1]
#         v_visited[v_x][v_y] = True
#         q = [[v_x, v_y]]
#         if v_count == -1:
#             break
#         while q:
#             if v_count >= min_spread:
#                 v_count = -1
#                 break
#             x, y = q[0][0], q[0][1]
#             for k in range(len(dx)):
#                 if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
#                     if maps[x+dx[k]][y+dy[k]] == 0 and v_visited[x+dx[k]][y+dy[k]] == False and [x+dx[k], y+dy[k]] not in temp:
#                         v_visited[x+dx[k]][y+dy[k]] = True
#                         q.append([x+dx[k], y+dy[k]])
#                         v_count += 1
#             q.pop(0)
#
#
#     if v_count == -1:
#         return
#     else:
#         min_spread = min(min_spread, v_count)
#         return
#
#
#
#
# def comb(k, start):
#     if k == r:
#         spread_virus(temp)
#         return
#
#     for i in range(start, len(safe_zone)):
#         temp.append(safe_zone[i])
#         comb(k+1, i+1)
#         temp.pop()
#
#
# start = time.time()
# n, m = map(int, input().split())
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# maps = [list(map(int, input().split())) for _ in range(n)]
# virus = []
# safe_zone = []
# for i in range(n):
#     for j in range(m):
#         if maps[i][j] == 0:
#             safe_zone.append([i, j])
#         elif maps[i][j] == 2:
#             virus.append([i, j])
# min_spread = 64
# temp = []
# r = 3
# comb(0, 0)
# print(len(safe_zone) - min_spread - 3)
#
# print('time : {}'.format(time.time()-start))
#
#
#
# '''
#
#
# '''


def spread_virus(temp):
    global min_virus

    v_visited = [[False] * m for _ in range(n)]

    virus_count = 0
    for vi in range(len(viruses)):
        v_x, v_y = viruses[vi][0], viruses[vi][1]
        v_visited[v_x][v_y] = True
        q = [[v_x, v_y]]
        while q:
            x, y = q[0][0], q[0][1]
            for k in range(len(dx)):
                if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
                    if maps[x+dx[k]][y+dy[k]] == 0 and v_visited[x+dx[k]][y+dy[k]] == False and [x+dx[k], y+dy[k]] not in temp:
                        v_visited[x+dx[k]][y+dy[k]] = True
                        q.append([x+dx[k], y+dy[k]])
                        virus_count += 1
            q.pop(0)


    min_virus = min(min_virus, virus_count)
    return

def comb(k, start):
    if k == 3:
        spread_virus(temp)
        return

    for i in range(start, len(safe_zones)):
        temp.append(safe_zones[i])
        comb(k+1, i+1)
        temp.pop()

n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
maps = [list(map(int, input().split())) for _ in range(n)]
viruses = []
safe_zones = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            safe_zones.append([i, j])
        elif maps[i][j] == 2:
            viruses.append([i, j])
min_virus = 64
temp = []
comb(0, 0)
print(len(safe_zones) - min_virus - 3)