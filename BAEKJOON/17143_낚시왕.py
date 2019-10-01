# # def fishing(s, e, maps):
# #     if s == e:
# #         return
# #
# #     else:
# #         shark_temp = []
#
#
r, c, m = map(int, input().split())
sharks = []
for i in range(r):
    temp = [0] * c
    sharks.append(temp)
# print(sharks)
for i in range(m):
    x, y, s, d, z = map(int, input().split())
    sharks[x-1][y-1] = [z,s,d]  # z : 상어 크기, s : 이동횟수, d : 방향
hunt_sum = 0
n = 0
# print('초기상태')
# for k in range(r):
#     print(sharks[k])
# print()
while n < c:
    shark_temp = []
    for i in range(r): # 가장 가까운 상어 잡기
        if sharks[i][n] != 0:
            hunt_sum += sharks[i][n][0]
            sharks[i][n] = 0
            break

    for i in range(r):
        temp = [0] * c
        shark_temp.append(temp)

    for i in range(r):
        for j in range(c):
            if sharks[i][j] != 0: # 상어 발견
                z_temp = sharks[i][j][0]
                move = sharks[i][j][1]
                dir = sharks[i][j][2]
                x, y = i, j
                if sharks[i][j][1] == 0:
                    if shark_temp[i][j] == 0:
                        shark_temp[i][j] = [z_temp, move, dir]
                    else:
                        if shark_temp[i][j][0] < z_temp:
                            shark_temp[i][j] = [z_temp, move, dir]
                    continue
                else:
                    if sharks[i][j][2] == 1:
                        x = i
                        quo = (((r - 1) + (move - x)) // (r - 1))
                        remainder = (((r - 1) + (move - x)) % (r - 1))
                        # print('quo : ', quo)
                        # print('remainer : ', remainder)
                        if quo % 2 == 1 and remainder == 0:
                            dir = 1
                            x = remainder
                        elif quo % 2 == 1 and remainder > 0:
                            dir = 2
                            x = remainder
                        elif quo % 2 == 0 and remainder == 0:
                            dir = 2
                            x = (r - 1) - remainder
                        else:
                            dir = 1
                            x = (r - 1) - remainder

                    elif sharks[i][j][2] == 2:
                        quo = (move + x) // (r - 1)  # 몫
                        remainder = (move + x) % (r - 1)  # 나머지
                        if quo % 2 == 1 and remainder == 0:
                            dir = 2
                            x = (r - 1) - remainder
                        elif quo % 2 == 1 and remainder > 0:  # 홀수라면
                            dir = 1
                            x = (r - 1) - remainder
                        elif quo % 2 == 0 and remainder == 0:
                            dir = 1
                            x = remainder
                        else:
                            dir = 2
                            x = remainder

                    elif sharks[i][j][2] == 3:
                        y = j
                        quo = (move + y) // (c - 1)  # 몫
                        remainder = (move + y) % (c - 1)  # 나머지
                        if quo % 2 == 1 and remainder == 0:  # 홀수라면
                            dir = 3
                            y = (c - 1) - remainder
                        elif quo % 2 == 1 and remainder > 0:
                            dir = 4
                            y = (c - 1) - remainder
                        elif quo % 2 == 0 and remainder == 0:
                            dir = 4
                            y = remainder
                        else:
                            dir = 3
                            y = remainder

                    elif sharks[i][j][2] == 4:  # 오른쪽 상어(증가)
                        y = j
                        quo = (move + y) // (c - 1)  # 몫
                        remainder = (move + y) % (c - 1)  # 나머지
                        if quo % 2 == 1 and remainder == 0:  # 홀수라면
                            dir = 3
                            y = (c - 1) - remainder
                        elif quo % 2 == 1 and remainder > 0:
                            dir = 4
                            y = (c-1) - remainder
                        elif quo % 2 == 0 and remainder == 0:
                            dir = 4
                            y = remainder
                        else:
                            dir = 3
                            y = remainder

                if shark_temp[i][y] == 0:
                    shark_temp[i][y] = [z_temp, move, dir]
                else:
                    if shark_temp[i][y][0] < z_temp:
                        shark_temp[i][y] = [z_temp, move, dir]

        else:
            continue



    sharks = shark_temp

    # for k in range(r):
    #     print(sharks[k])
    # print()

    # for i in range(r):
    #     for j in range(c):
    #         if sharks[i][j] != 0:
    #             sharks[i][j][3] = False
    #         else:
    #             continue
    n += 1
    # print('{}초 후'.format(n))
    # for k in range(r):
    #     print(sharks[k])
    # print()

print(hunt_sum)

