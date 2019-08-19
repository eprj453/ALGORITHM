import sys
sys.stdin = open('4408_input.txt', 'r')


t = int(input())
for i in range(1, t+1):
    corridor_list = [0] * 200
    # print(room_list)
    n = int(input())
    for j in range(n):
        here_goal = list(map(int, input().split()))
        here, goal = here_goal[0], here_goal[1]
        if here < goal: # 정주행 학생
            if here % 2 == 0: # 짝수 2, 7?
                for k in range(here, goal, 2):
                    corridor_list[(k//2)-1] += 1
                if goal % 2: # 목적지 짝수라면
                    corridor_list[(goal//2)-1] += 1
                else:
                    corridor_list[goal//2] += 1

            else: # 홀수
                for k in range(here, goal, 2):
                    corridor_list[k//2] += 1
                if goal % 2: # 목적지 홀수면
                    corridor_list[goal//2] += 1

        else: # 거꾸로 질주하는 학생
            if here % 2 == 0: # 현재 위치 짝수? 6 , 2?
                for k in range(here, goal, -2):
                    corridor_list[(k//2)-1] += 1
                if goal % 2 == 0:
                    corridor_list[(goal//2)-1] += 1
            else: # 현재 위치 홀수? 5, 2
                for k in range(here, goal, -2):
                    corridor_list[k//2] += 1
                if goal % 2: # 목적지 홀수라면
                    corridor_list[goal//2] += 1
                else:
                    corridor_list[(goal//2)-1] += 1

    print('#{} {}'.format(i, max(corridor_list)))
