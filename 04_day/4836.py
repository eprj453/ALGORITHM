import sys
sys.stdin = open('4836_input.txt', 'r')
t = int(input())
for t in range(1, t + 1):
    blank_list = []

    for i in range(10):
        blank_list.append([0] * 10)

    n = int(input())
    count = 0
    color_list = []

    

    for j in range(n):
        color_list += [list(map(int, input().split()))]

    for j in range(0, len(color_list)):
        color = 1 if color_list[j][4] == 1 else 2
        for k in range(color_list[j][0], (color_list[j][2]) + 1):
            for l in range(color_list[j][1], (color_list[j][3]) + 1):
                if blank_list[k][l] != color and blank_list[k][l] != 0:
                    blank_list[k][l] = 3
                    count += 1
                else:
                    blank_list[k][l] = color
    print('#{} {}'.format(t, count))

# t = int(input())
# for i in range(1, t+1):
#
#     blank_list = []
#
#     for i in range(10):
#         blank_list.append([0]*10)
#
#
#     print(blank_list)
#     print(len(blank_list))
#     print(len(blank_list[0]))
#
#     n = int(input())
#     count = 0
#     color_list = []
#     for j in range(n):
#         color_list += [list(map(int, input().split()))]
#
#     for j in range(0, len(color_list)):
#         color = 1 if color_list[j][4]==1 else 2
#        # print('color : {}'.format(color))
#
#         for k in range(color_list[j][0], (color_list[j][2])+1):
#             #print('k: {}'.format(k))
#             for l in range(color_list[j][1], (color_list[j][3])+1):
#                 if blank_list[k][l] != color and blank_list[k][l] != 0:
#                     blank_list[k][l] = 3
#                     count += 1
#                 else:
#                     blank_list[k][l] = color
#         print('count : {}'.format(count))



    #     if color_list[j][4] == 1:
    #         for k in range(color_list[j][0], (color_list[j][2])+1):
    #             print('k: {}'.format(k))
    #             for l in range(color_list[j][1], (color_list[j][3])+1):
    #                 print('{},{}'.format(k,l))
    #                 if blank_list[k][l] == 0:
    #                     blank_list[k][l] = 1
    #                 else:
    #                     blank_list[k][l] = 3
    #                     count += 1
    #
    #
    #     elif color_list[j][4] == 2:
    #         for k in range(color_list[j][0], (color_list[j][2])+1):
    #             print('k: {}'.format(k))
    #             for l in range(color_list[j][1], (color_list[j][3])+1):
    #                 print('{},{}'.format(k,l))
    #                 if blank_list[k][l] == 0:
    #                     blank_list[k][l] = 2
    #                 else:
    #                     blank_list[k][l] = 3
    #                     count += 1
    #     print(blank_list)
    # print('count : {}'.format(count))

        # if color_list[j][4] == 1:
        #     for k in range(color_list[j][0], (color_list[j][2])+1):
        #         print('k: {}'.format(k))
        #         for l in range(color_list[j][1], (color_list[j][3])+1):
        #             print('{},{}'.format(k,l))
        #             blank_list[l][k] = 1
        #
        #
        # elif color_list[j][4] == 2:
        #     for m in range(color_list[j][0], (color_list[j][2])+1):
        #         print('m: {}'.format(m))
        #         for n in range(color_list[j][1], (color_list[j][3])+1):
        #             print('{},{}'.format(m, n))
        #             blank_list[m][n] = 2

        # for k in range(2, 5):
        #     print('k: {}'.format(k))
        #     for l in range(2, 5):
        #         if blank_list[k][l] != color and blank_list[k][l] != 0:
        #             blank_list[k][l] = 3
        #         else:
        #             print('{},{}'.format(k,l))
        #             blank_list[k][l] = color
'''
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 1, 0, 0, 1, 1], 
[0, 0, 0, 0, 1, 1, 0, 0, 1, 1], 
[0, 0, 2, 2, 3, 3, 2, 2, 3, 1], 
[0, 0, 2, 2, 3, 3, 2, 2, 2, 0], 
[0, 0, 2, 2, 3, 3, 2, 2, 2, 0], 
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''