# arr = [[9, 20, 2, 18, 11],[19, 1, 25, 3, 21],[8, 24, 10, 17, 7], [15, 4, 16, 5, 6],[12, 13, 22, 23, 14]]
#
# '''
# 09 20 02 18 11
# 19 01 25 03 21
# 08 24 10 17 07
# 15 04 16 05 06
# 12 13 22 23 14
# '''
#
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# sum = 0
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         for k in range(len(dx)):
#             tx, ty = i + (dx[k]), j + (dy[k])
#             print(tx, ty)
#



arr = [[ 1,  2,  4,  7, 11],
    [ 3,  5,  8, 12, 15],
    [ 6,  9, 13, 16, 18],
    [10, 14, 17, 19, 20]]


N, M = len(arr), len(arr[0])
for diag in range(0, N + M - 1):    # diag: 사선의 수
                                    # x, y: 시작 좌표
    x = 0 if diag < M else (diag - M + 1)
    y = diag if diag < M else M - 1

    while x < N and y >= 0:
        print('%2d ' % arr[x][y], end='')
        x += 1
        y -= 1
    print()


#
# a = 20
# b = a >> 1
# print(b)