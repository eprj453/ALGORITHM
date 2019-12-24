import sys
sys.stdin = open('6485_input.txt', 'r')

for i in range(1,  int(input())+1):
    n = int(input())
    stations = [0] * 5001
    for _ in range(n):
        start, end = map(int, input().split())
        for num in range(start, end+1):
            stations[num] += 1
    p = int(input())
    print('#{} '.format(i), end="")
    for j in range(p):
        if j == p-1:
            print('{}'.format(stations[int(input())]))
        else:
            print('{}'.format(stations[int(input())]), end=" ")
