import sys
sys.stdin = open('5202_input.txt', 'r')


for i in range(1, int(input())+1):
    n = int(input())
    dock = [list(map(int, input().split())) for _ in range(n)]

    for j in range(len(dock)-1, -1, -1):
        for k in range(0, j):
            if dock[k][1] > dock[k+1][1]:
                dock[k], dock[k + 1] = dock[k+1], dock[k]

    tasks = [dock[0]]
    for task in dock:
        if tasks[-1][1] <= task[0]:
            tasks.append(task)

    print('#%d %d'%(i, len(tasks)))