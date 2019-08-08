# 원래는
# bit = [0, 0, 0, 0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)


subset_list = [3, 6, 7, 1, 5, 4]

n = len(subset_list)

for i in range(1<<n):
    print('i : {}'.format(i))
    for j in range(n+1):
        if i & (1<<j):
            print(subset_list[j], end=', ')
        # print('----')
    print()