import sys
sys.stdin = open('2805_input.txt', 'r')

# t = int(input())
# for i in range(1, t+1):
#     n = int(input()) # 5
#     farm_list = []
#
#     for j in range(n):
#         farm_list.append(list(map(int, input())))
#
#     farm_sum = 0
#
#     for j in range(0, (n//2)+1):
#         farm_sum += farm_list[n // 2 - j][n // 2]
#         farm_sum += farm_list[n // 2 + j][n // 2]
#         for k in range(1, (n//2)-j+1):
#             if j == 0:
#                 # print(n // 2, (n // 2) - k)
#                 # print(n // 2, (n // 2) + k)
#                 # print('-----------------')
#                 farm_sum += farm_list[n // 2][(n // 2) - k]
#                 farm_sum += farm_list[n // 2][(n // 2) + k]
#
#             else:
#                 # print((n // 2) - j, (n // 2) + k)
#                 # print((n // 2) - j, (n // 2) - k)
#                 # print((n // 2) + j, (n // 2) + k)
#                 # print((n // 2) + j, (n // 2) - k)
#                 farm_sum += farm_list[(n // 2) - j][(n // 2) + k]
#                 farm_sum += farm_list[(n // 2) - j][(n // 2) - k]
#                 farm_sum += farm_list[(n // 2) + j][(n // 2) + k]
#                 farm_sum += farm_list[(n // 2) + j][(n // 2) - k]
#
#         # print('------------------')
#     farm_sum -= farm_list[n//2][n//2]
#     print('#{} {}'.format(i, farm_sum))

for i in range(1, int(input())+1):
    n = int(input())
    f = [list(map(int, input())) for _ in range(n)]
    f_sum = 0
    x, y, = n//2, 0
    for j in range(n):
        x2, y2 = x, y
        while x2 >= y:
            f_sum += f[x2][y2]
            x2 -= 1
            y2 += 1
        if j % 2:
            x += 1
        else:
            y += 1
    print('#{} {}'.format(i, f_sum))





