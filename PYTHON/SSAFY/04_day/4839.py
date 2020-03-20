import sys
sys.stdin = open('4839_input.txt', 'r')
# 400 300 350
# 전체쪽수 400 중 a는 300쪽, b는 350쪽 탐색
# t = int(input())
# for i in range(1, t+1):
#     tab = list(map(int, input().split()))
#     t, a, b = tab[0], tab[1], tab[2]
#     # print(t, a, b)
#     mid = int(tab[0] / 2)
#     a_loc, b_loc = mid, mid
#     a_range = [0, t]
#     b_range = [0, t]
#     a_win = 0
#     b_win = 0
#
#     while True:
#
#         while True:
#             if a > a_loc:
#                 a_range[0] = a_loc
#                 a_loc = (a_range[0] + a_range[1]) // 2
#                 break
#             elif a < a_loc:
#                 a_range[1] = a_loc
#                 a_loc = (a_range[0] + a_range[1]) // 2
#                 break
#
#         while True:
#             if b > b_loc:  # 250 > 200
#                 b_range[0] = b_loc
#                 b_loc = (b_range[0] + b_range[1]) // 2
#                 break
#             elif b < b_loc:  # 150 <  200
#                 b_range[1] = b_loc
#                 b_loc = (b_range[0] + b_range[1]) // 2
#                 break
#
#         if a_loc == a:
#             a_win += 1
#
#         if b_loc == b:
#             b_win += 1
#
#         if a_win != 0 or b_win != 0:
#             # print(a_win, b_win)
#             if a_win > b_win:
#                 winner = 'A'
#             elif a_win < b_win:
#                 winner = 'B'
#             else:
#                 winner = 0
#             break
#     print('#{} {}'.format(i, winner))

t = int(input())
for i in range(1, t+1):
    tab = list(map(int, input().split()))
    t, a, b = tab[0], tab[1], tab[2]
    print(t, a, b)
    a_start = 1
    a_end = t # 400
    b_start = 1
    b_end = t # 400
    a_win = 0
    b_win = 0
    # 400 300 350
    # 전체쪽수 400 중 a는 300쪽, b는 350쪽 탐색
    # 전체쪽수 400 중 a는 150쪽, b는 120쪽 탐색

    while True:
        # print('a_start : {}'.format(a_start))
        # print('a_end : {}'.format(a_end))
        a_mid = (a_start + a_end) // 2
       #print('a_mid : {}'.format(a_mid))
        if a_mid > a:
            a_end = a_mid
        elif a_mid < a:
            a_start = a_mid

        # print('b_start : {}'.format(b_start))
        # print('b_end : {}'.format(b_end))
        b_mid = (b_start + b_end) // 2
       #print('b_mid : {}'.format(b_mid))
        if b_mid > b:
            b_end = b_mid
        elif b_mid < b:
            b_start = b_mid

        if (a_start + a_end) // 2 == a:
            a_win += 1

        if (b_start + b_end) // 2 == b:
            b_win += 1

        if a_win != 0 or b_win != 0:
            if a_win > b_win:
                winner = 'A'
            elif a_win < b_win:
                winner = 'B'
            else:
                winner = 0
            break

    print('#{} {}'.format(i, winner))






    # a_range = list(range(1, t+1))
    # b_range = list(range(1, t+1))
    # a_win = 0
    # b_win = 0
    # a_start = 1
    # a_end = len(a_range)-1
    # b_start = 1
    # b_end = len(b_range)-1
    # b_count = 0
    # a_count = 0
    #
    # while a_start <= a_end:
    #     middle = (a_start + a_end) // 2
    #     print(middle)
    #     if a_range[middle] == a:
    #         a_count += 1
    #         break
    #     elif a_range[middle] > a:
    #         end = middle -1
    #         a_count += 1
    #     else:
    #         b_start = middle-1
    #         a_count += 1
    #
    # while b_start <= b_end:
    #     middle = (b_start + b_end) // 2
    #     print(middle)
    #     if b_range[middle] == b:
    #         b_count += 1
    #         break
    #     elif b_range[middle] > b:
    #         end = middle -1
    #         b_count += 1
    #     else:
    #         b_start = middle-1
    #         b_count += 1
    #
    # print(a_count, b_count)

    # while True:
    #
    #     while True:
    #         if a > a_loc:
    #             a_range[0] = a_loc
    #             a_loc = (a_range[0] + a_range[1]) // 2
    #             break
    #         elif a < a_loc:
    #             a_range[1] = a_loc
    #             a_loc = (a_range[0] + a_range[1]) // 2
    #             break
    #
    #     while True:
    #         if b > b_loc:  # 250 > 200
    #             b_range[0] = b_loc
    #             b_loc = (b_range[0] + b_range[1]) // 2
    #             break
    #         elif b < b_loc:  # 150 <  200
    #             b_range[1] = b_loc
    #             b_loc = (b_range[0] + b_range[1]) // 2
    #             break
    #
    #     if a_loc == a:
    #         a_win += 1
    #
    #     if b_loc == b:
    #         b_win += 1
    #
    #     if a_win != 0 or b_win != 0:
    #         # print(a_win, b_win)
    #         if a_win > b_win:
    #             winner = 'A'
    #         elif a_win < b_win:
    #             winner = 'B'
    #         else:
    #             winner = 0
    #         break
    # print('#{} {}'.format(i, winner))


    #     if a > a_loc: # 250 > 200
    #         a_range[0] = a_loc
    #         a_loc = (a_range[0] + a_range[1]) // 2
    #         print('a > a_loc, a_loc : {}'.format(a_loc))
    #
    #
    #     elif a < a_loc: # 150 <  200
    #         a_range[1] = a_loc
    #         a_loc = (a_range[0] + a_range[1]) // 2
    #         print('a < a_loc, a_loc : {}'.format(a_loc))
    #
    #         # print('페이지가 더 앞에 있네요')
    #     if b > b_loc: # 250 > 200
    #         print('b > b_loc, b_loc : {}'.format(b_loc))
    #         b_range[0] = b_loc
    #         b_loc = (b_range[0] + b_range[1]) // 2
    #         # print('페이지가 더 뒤에 있네요')
    #         # a_start = (a_start + a_end) / 2
    #         # if a_start == a:
    #         #     print('a 끝')
    #         # else:
    #         #     pass
    #
    #     elif b < b_loc: # 150 <  200
    #         print('b < b_loc : {}'.format(b_loc))
    #         b_range[1] = b_loc
    #         b_loc = (b_range[0] + b_range[1]) // 2
    #
    #         # print('페이지가 더 앞에 있네요')
    #
    #
    #     if a_loc == a:
    #         print('a 끝')
    #         a_win += 1
    #
    #
    #     if b_loc == b:
    #         print('b_loc : {}'.format(b_loc))
    #         print('b 끝')
    #         b_win += 1
    #
    #     if a_win != 0 or b_win != 0:
    #         print(a_win, b_win)
    #         if a_win > b_win:
    #             winner = 'A'
    #         elif a_win < b_win:
    #             winner = 'B'
    #         else:
    #             winner = 0
    #         break
    #
    # print('#{} {}'.format(i, winner))

# t = int(input())
# for i in range(1, t + 1):
#     tab = list(map(int, input().split()))
#     t, a, b = tab[0], tab[1], tab[2]
#     a_loc, b_loc = int(tab[0] / 2), int(tab[0] / 2)
#     a_range = [0, t]
#     b_range = [0, t]
#     a_win = 0
#     b_win = 0
#
#     while True:
#         if a > a_loc:
#             a_range[0] = a_loc
#             a_loc = (a_range[0] + a_range[1]) // 2
#         elif a < a_loc:
#             a_range[1] = a_loc
#             a_loc = (a_range[0] + a_range[1]) // 2
#
#         if a_loc == a:
#             a_win += 1
#
#         if b > b_loc:
#             b_range[0] = b_loc
#             b_loc = (b_range[0] + b_range[1]) // 2
#         elif b < b_loc:
#             b_range[1] = b_loc
#             b_loc = (b_range[0] + b_range[1]) // 2
#
#         if b_loc == b:
#             b_win += 1
#
#         if a_win != 0 or b_win != 0:
#             if a_win > b_win:
#                 winner = 'A'
#             elif a_win < b_win:
#                 winner = 'B'
#             else:
#                 winner = 0
#             break
#
#     print('#{} {}'.format(i, winner))
#
