import sys
sys.stdin = open('5208_input.txt', 'r')


def station(start, end, charge, change):
    global min_count
    if change >= min_count:
        return
    if start == end:
        min_count = min(min_count, change)
        return
    if start > end:
        return
    if charge == 0:
        if start == end:
            min_count = min(min_count, change)
            return
        else:
            return

    station(start+1, end, m[start+1], change+1)
    station(start+1, end, charge-1, change)

for i in range(1, int(input())+1):
    n, m = 0 , []
    temp = list(map(int, input().split()))
    for j in range(len(temp)+1):
        if j == 0:
            n = temp[j]
        elif j == len(temp):
            m.append('0')
        else:
            m.append(temp[j])
    min_count = 100
    station(0, len(temp)-1, m[0], 0)

    print('#{} {}'.format(i, min_count))