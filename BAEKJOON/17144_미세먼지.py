# def clean(direction, r):
#     if direction == 1: # 시계방향

def dust_diffsion(c):
    dust_temp = []
    for h in range(r):
        temp = [0] * c
        dust_temp.append(temp)
    for i in range(len(dusts)):
        for j in range(len(dusts[i])):
            if dusts[i][j] != 0 and dusts[i][j] != -1:
                x, y = i, j
                count = []
                for k in range(len(dx)):
                    if 0 <= x+dx[k] < len(dusts) and 0 <= y+dy[k] < len(dusts[i]) and dusts[x+dx[k]][y+dy[k]] != -1:
                        count.append([x+dx[k], y+dy[k]]) # 갯수 세기
                        dust_temp[x+dx[k]][y+dy[k]] += dusts[x][y]//5
                dust_temp[x][y] -= (dusts[x][y]//5) * len(count)
    for k in range(len(dusts)):
        for c in range(len(dusts[i])):
            dusts[k][c] += dust_temp[k][c]

def clean_air(direction, )




r, c, t = map(int, input().split())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
dusts = []
machine = 0
for i in range(r):
    tmp = list(map(int, input().split()))
    if tmp[0] == -1 and machine == 0:
        machine = i
    dusts.append(tmp)

n = 0
while n < t:
    dust_diffsion(c)

    print(dusts)


# dusts = [list(map(int, input().split())) for _ in range(r)]
#
#
# dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
#
# dust_temp = []
# for h in range(r):
#     temp = [0] * c
#     dust_temp.append(temp)
#
# clean = []
#
# n = 0
# while n < t:
#     for i in range(len(dusts)):
#
#         for j in range(len(dusts[i])):
#             if dusts[i][j] == -1: clean.append([i,j])
#             if dusts[i][j] != 0 and dusts[i][j] != -1:
#                 x, y = i, j
#                 count = []
#                 for k in range(len(dx)):
#                     if 0 <= x+dx[k] < len(dusts) and 0 <= y+dy[k] < len(dusts[i]) and dusts[x+dx[k]][y+dy[k]] != -1:
#                         count.append([x+dx[k], y+dy[k]]) # 갯수 세기
#                         dust_temp[x+dx[k]][y+dy[k]] += dusts[x][y]//5
#                 dust_temp[x][y] -= (dusts[x][y]//5) * len(count)
#
#
#     for k in range(len(dusts)):
#         for c in range(len(dusts[i])):
#             dusts[k][c] += dust_temp[k][c]
#
#     clean_1 = clean[0] # 2, 0
#     clean_2 = clean[1] # 3, 0
#     s = 0
#     while clean_1[0] != 0:
#         if dusts[clean_1[0]][0] != -1:
#             dusts[clean_1[0]][0] = dusts[clean_1[0]-1][0]
#         clean_1[0] -= 1
#     while clean_1[1] != len(dusts[i])-1:
#         if dusts[0][clean_1[1]] != -1:
#             dusts[0][clean_1[1]] = dusts[0][clean_1[1]+1]
#         clean_1[1] += 1
#
#     while clean_1[0] <
#




    # for k in range(len(clean)):
    #     if k == 0:
    #         clean_1 = clean[k]
    #         tmp = clean[k][len(dusts[i])-1]
    #         for l in range(len(dusts[i]-2)):
    #             dusts[i][l+1] = dusts[i][l]
    #
    #         tmp2 = clean[0][len(dusts[i]-1)]
    #         for l in range(clean_1[0]-1, -1, -1):
    #
    #
    # print('dust_temp: ', dust_temp)
    # print('dusts : ',dusts)
    # #
    # # for i in range(r):
    # #     print(dusts[i])
    #
    # n += 1
    #
