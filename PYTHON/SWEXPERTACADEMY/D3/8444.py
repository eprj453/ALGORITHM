import sys
sys.stdin = open('8444_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    room_l = int(input())
    room = list(input().split())
    temp = ['0']*room_l
    count = 0
    for j in range(len(room)):
        if room == temp:
            break
        if room[j] == temp[j]:
            continue
        else:
            count += 1
            for k in range(j, len(room), j+1):
                if temp[k] == '1':
                    temp[k] = '0'
                else:
                    temp[k] = '1'
    print('#{} {}'.format(i, count))