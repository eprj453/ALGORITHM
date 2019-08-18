import sys
sys.stdin = open('4408_input.txt', 'r')


t = int(input())
for i in range(1, t+1):
    room_list = [0] * 400
    # print(room_list)
    n = int(input())
    for j in range(n):
        here_goal = list(map(int, input().split()))
        here, goal = here_goal[0], here_goal[1]
        for k in range(here-1, goal-1):
            room_list[k] += 1

    print('#{} {}'.format(i, max(room_list)))