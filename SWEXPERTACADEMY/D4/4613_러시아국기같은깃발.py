import sys
sys.stdin = open('4613_input.txt', 'r')

def color(w, b, r, start, end, count):
    global max_count
    if w + b + r > n-2:
        max_count = max(count, max_count)
        return

    else:
        temp = 0
        for i in range(flag[start]):




for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    count = 0

    for i in range(m):
        if flag[0][i] != 'W':
            flag[0][i] = 'W'
            count += 1
        if flag[len(flag)-1][i] != 'R':
            flag[len(flag) - 1][i] = 'R'
            count += 1
    max_count = count
    start, end = 1, n-2
    print()
    print(flag)
    print(count)