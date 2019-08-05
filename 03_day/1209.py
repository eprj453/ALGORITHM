import sys
sys.stdin = open('input_1209.txt', 'r')

# while True:
#     n = int(input())
#     array_list = []
#     for j in range(100):
#         array_list += [list(map(int, input().split()))]
#
#     max = 0
#     for j in range(0, 100):
#         sum = 0
#         for k in range(0, 100):
#             sum += array_list[j][k]
#         print('sum은 {}'.format(sum))
#         if sum > max:
#             max = sum
#
#     for j in range(0, 100):
#         sum = 0
#         for k in range(0, 100):
#             sum += array_list[k][j]
#         if sum > max:
#             max = sum
#
#     sum = 0
#     for j in range(0, 100):
#         sum += array_list[j][j]
#     if sum > max:
#         max = sum
#
#     sum = 0
#     for j in range(0, 100):
#         sum += array_list[j][99-j]
#     if sum > max:
#        max = sum
#
#     print('#{} {}'.format(n, max))
#
#     if n == 10:
#         break


while True:
    n = int(input())
    array_list = []
    for j in range(100):
        array_list += [list(map(int, input().split()))]

    cols_max, rows_max, cross_sum, cross_sum2, total_max = 0, 0, 0, 0, 0

    for j in range(0, 100):
        cols_sum, rows_sum = 0, 0
        for k in range(0, 100):
            cols_sum += array_list[j][k]
        if cols_sum > cols_max:
            cols_max = cols_sum
        if rows_sum > cols_max:
            rows_max = rows_sum

    for j in range(0, 100):
        cross_sum += array_list[j][j]
        cross_sum2 += array_list[j][99-j]

    print(cross_sum, cross_sum2, cols_max, rows_max)
    total_max = max(cols_max, rows_max, cross_sum, cross_sum2)

    print('#{} {}'.format(n, total_max))

    if n == 10:
        break
