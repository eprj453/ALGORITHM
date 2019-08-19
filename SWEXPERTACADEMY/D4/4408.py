import sys
sys.stdin = open('4408_input.txt', 'r')


# t = int(input())
# for i in range(1, t+1):
#     odd_list = [0] * 200
#     even_list = [0] * 200
#     # print(room_list)
#     n = int(input())
#     for j in range(n):
#         here_goal = list(map(int, input().split())) # 1, 3 / 2, 200
#         here, goal = here_goal[0], here_goal[1]
#         if here % 2: # 홀수에서 시작한다면
#             for k in range(here-1, goal-1):
#                 if k % 2:
#                     odd_list[k//2] += 1
#             if (goal-1) % 2: # 목적지가 홀수라면
#                 odd_list[goal-1//2] += 1
#             elif (goal-1) % 2 == 0: # 목적지가 짝수라면
#                 if goal-1 < here-1: # 거꾸로 질주하는 학생이라면
#                     even_list[((goal-1)//2)-1] += 1
#                 else:
#                     odd_list[((goal-1)//2)-1] -= 1
#                     even_list[((goal-1)//2)-1] += 1
#
#         else: # 짝수에서 시작한다면
#             for k in range(here-1, goal-1):
#                 if k % 2 == 0: # 짝수 리스트 훑기
#                     even_list[(k//2)-1] += 1
#             if (goal-1) % 2 == 0: # 목적지가 짝수라면
#                 even_list[((goal-1)//2)-1] += 1
#             elif (goal-1) % 2 == 1: # 목적지가 홀수라면
#                 if goal-1 < here-1: # 거꾸로 질주하는 학생이라면
#                     even_list[(goal-1)//2] -= 1
#                     odd_list[(goal-1)//2] += 1
#                 else:
#                     odd_list[(goal-1)//2] += 1
#
#
#     count_max = 0
#     for j in range(len(odd_list)):
#         if odd_list[j] + even_list[j] > count_max:
#             count_max = odd_list[j] + even_list[j]
#
#     print('#{} {}'.format(i, count_max))



t = int(input())
for i in range(1, t+1):
    odd_list = [0] * 200
    even_list = [0] * 200
    n = int(input())
    for j in range(n):
        here_goal = list(map(int, input().split()))
        here, goal = here_goal[0], here_goal[1]
        if here % 2:
            for k in range(here, goal):
                if k % 2:
                    odd_list[(k//2)] += 1
            if goal % 2 == 1:
                odd_list[goal//2] += 1
            elif goal % 2 == 0:
                if goal < here:
                    even_list[(goal//2)-1] += 1
                else:
                    odd_list[(goal//2)-1] -= 1
                    even_list[(goal//2)-1] += 1

        else:
            for k in range(here, goal):
                if k % 2 == 0:
                    even_list[(k//2)-1] += 1
            if goal % 2 == 0:
                even_list[(goal//2)-1] += 1
            elif goal % 2 == 1:
                if goal < here:
                    even_list[goal//2] -= 1
                    odd_list[(goal//2)] += 1
                else:
                    odd_list[goal//2] += 1
                    
    count_max = 0
    for j in range(len(odd_list)):
        if odd_list[j] + even_list[j] > count_max:
            count_max = odd_list[j] + even_list[j]

    print('#{} {}'.format(i, count_max))
