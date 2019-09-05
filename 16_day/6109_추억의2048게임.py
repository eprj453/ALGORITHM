import sys
sys.stdin = open('6109_input.txt', 'r')

# from collections import deque
for t in range(1, int(input())+1):
    l, d = input().split()
    l = int(l)
    nums = [list(map(int, input().split())) for _ in range(int(l))]
    temp = []
    temp2 = []
    for i in range(l):
        temp.append([])
        temp2.append([])

    if d == 'up' or d == 'down':
        for j in range(l):
            for k in range(l):
                if d == 'up' or d == 'down':
                    if nums[k][j] != 0:
                        temp[j].append(nums[k][j])

    else:
        for j in range(l):
            for k in range(l):
                if nums[j][k] != 0:
                    temp[j].append(nums[j][k])

    if d == 'up' or d == 'left':
        print(temp)
        for j in range(len(temp)):
            idx = 0
            while True:
                if idx > len(temp[j])-1:
                    break
                if idx == len(temp[j])-1:
                    temp2[j].append(temp[j][idx])
                    break
                elif temp[j][idx] == temp[j][idx+1]:
                    temp2[j].append(temp[j][idx] + temp[j][idx+1])
                    idx += 2
                else:
                    temp2[j].append(temp[j][idx])
                    idx += 1
            for k in range(0, l-len(temp2[j])):
                temp2[j].append(0)

    else:
        for j in range(len(temp)):
            idx = len(temp[j])-1
            while True:
                if idx < 0:
                    break
                if idx == 0:
                    temp2[j].insert(0, temp[j][idx])
                    break
                elif temp[j][idx] == temp[j][idx-1]:
                    temp2[j].insert(0, temp[j][idx] + temp[j][idx-1])
                    idx -= 2
                else:
                    temp2[j].insert(0, temp[j][idx])
                    idx -= 1
            for k in range(0, l-len(temp2[j])):
                temp2[j].insert(0, 0)


    print('#{}'.format(t))
    if d == 'up' or d == 'down':
        for j in range(l):
            for k in range(l):
                print(temp2[k][j], end = ' ')
            print()
    else:
        for j in range(l):
            for k in range(l):
                print(temp2[j][k], end=' ')
            print()


