# t = int(input())
# for i in range(1, t+1):
#     list2 = []
#     nm = input()
#     nm2 = nm.split(' ')
#     for j in range(0, int(nm2[0])):
#         nn_list = input()
#         nn_list2 = nn_list.split(' ')
#         list = []
#         for k in range(0, len(nn_list2)):
#             list.append(int(nn_list2[k]))
#         list2.append(list)
#     for l in range(0,int(nm2[0])-int(nm2[1])+1):
#       for m in range(0,int(nm2[0])-int(nm2[1])+1):
#         for n in range(l,int(nm2[1])+l):
#           for o in range(m,int(nm2[1])+m):
#

# t = int(input())
# for i in range(1, t+1):
#     nm = list(map(input().split()))

# list1 = list(map(int, input().split()))

# list1 = []
# list2 = []
# cnt = 0
# # for line in t:
# #     list1.append(line)
# t = input()
# while True:
#     if t == ' ':
#         break
#     else:
#         for i in t:
#             if cnt > 4:
#                 list2.append(list1)
#                 list1 = []
#                 cnt = 0
#             elif i != ' ':
#                 print('i는 {}'.format(i))
#                 list1.append(i)
#                 print(list1)
#                 cnt += 1
#                 print(cnt)
# print(list2)


t = int(input())
for i in range(1, t+1):
    nk = list(map(int, input().split()))
    # print(f'{nk[0]}, {nk[1]}')
    puzzle_list = []
    for j in range(0, nk[0]):
        puzzle_list += [list(input().split())]
    #print(puzzle_list)

    compare_list = []

    for k in range(0, nk[0]):
        compare = 0
        for l in range(0, nk[0]):
            if l == nk[0] - 1:
                if puzzle_list[l][k] == 1 or puzzle_list[k][l]:
                    compare += 1
                    compare_list.append(compare)
                    break
                else:
                    compare_list.append(compare)
                    break
            elif puzzle_list[k][l] or puzzle_list[l][k] == '1':
                compare += 1
            elif puzzle_list[k][l] or puzzle_list[l][k] == '0':
                compare_list.append(compare)
                compare = 0
    #print(compare_list)

    # for k in range(0, nk[0]):
    #     compare = 0
    #     for l in range(0, nk[0]):
    #         if l == nk[0]-1:
    #             if puzzle_list[l][k] == 1:
    #                 compare += 1
    #                 compare_list.append(compare)
    #                 break
    #             else:
    #                 compare_list.append(compare)
    #                 break
    #         elif puzzle_list[l][k] == '1':
    #             compare += 1
    #         elif puzzle_list[l][k] == '0':
    #             compare_list.append(compare)
    #             compare = 0
    answer = compare_list.count(nk[1])
    print('#{} {}'.format(i, answer))







    # compare = ''
    # compare_list = []
    # for l in range(0, nk[0]):
    #     for m in range(0, nk[0]):
    #         if puzzle_list[l][m] == '1':
    #             compare += puzzle_list[l][m]
    #             count += 1
    #         elif puzzle_list[l][m] == '':
    #             count == 0
    #     compare_list.append([compare])
    #     compare = ''
    # for l in compare_list:
    #     if len(l) == nk[1]:
    #         count += 1
    # print(f'compare list {compare_list}')
    # compare = ''
    # compare_list = []
    # for l in range(0, nk[0]-nk[1]+1):
    #     for m in range(0, nk[0]):
    #         if puzzle_list[n][o] == 1 and puzzle_list[n+1][o] == 1 and puzzle_list[n+2][o] == 1:
    #             count += 1

    # print('#{} {}'.format(i, count))

# string = []
# list1 = []
#
# while True:
#     t = input()
#     if t == '':
#         break
#     else:
#         string.append(t)
# for i in string:
#     list1.append(list(i.split()))
#
# print(list1)

# t = int(input())
# for i in range(1, t+1):
#     nk = list(map(int, input().split()))
#     puzzle_list = []
#     puzzle_list2 = []
#     while True:
#         puzzle = input()
#         if puzzle == '':
#             break
#         else:
#             puzzle_list.append(puzzle)
#     for j in puzzle_list:
#         puzzle_list2.append(list(map(int, j.split())))
#     print(puzzle_list2)
