nm = list(map(int,input().split()))
n, m = nm[0], nm[1]
chess_list = []

for i in range(n):
    chess_list.append(input())

compare = 100000
chess_compare1, chess_compare2 = 'BWBWBWBW', 'WBWBWBWB'
for i in range(n-8+1): # 0~3
    for j in range(m-8+1): # 0~6
        w_count, b_count = 0, 0
        for k in range(i, i + 8):
            chess_compare1, chess_compare2 = chess_compare2, chess_compare1
            for l in range(j, j + 8):
                # print(k, l)
                if chess_list[k][l] == chess_compare1[l-j]:
                    w_count += 1
                else:
                    b_count += 1
        compare = min(compare, w_count, b_count)
print(compare)


# compare_count1, compare_count2 = 0, 0
# for i in range(coop[0], coop[0]+8):# 2, 5 2번째부터 9번째까지의 행
#     chess_compare1, chess_compare2 = 'BWBWBWBW', 'WBWBWBWB'
#     if i % 2 == 1:
#         chess_compare1, chess_compare2 = chess_compare2, chess_compare1
#
#         # print(chess_compare2)
#     for j in range(coop[1], coop[1]+8): # 5번째부터 12번째까지 칸
#         print(chess_list[i][j], end = ' ')
#         print(chess_compare1[j-coop[1]], end = ' ')
#         print(chess_compare2[j - coop[1]])
#         print('--------------------')
#         if chess_list[i][j] != chess_compare1[j-coop[1]]:
#             compare_count2 += 1
#         else:
#             compare_count1 += 1
#     print()
#
# print(compare_count1, compare_count2)
# print(min(compare_count1, compare_count2))
