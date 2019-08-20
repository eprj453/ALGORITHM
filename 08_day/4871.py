import sys
sys.stdin = open('4871_input.txt', 'r')

def find(start, end, line_list):
    global count
    if start == end:
        count += 1
    for i in range(len(line_list)):
        if line_list[i][0] == start:
            find(line_list[i][1], end, line_list)
    return count


t = int(input())
for i in range(1, t+1):
    count = 0
    v, e = map(int, input().split())
    line_list = []
    for j in range(e):
        temp = list(map(int, input().split()))
        line_list.append(temp)
    start, end = map(int, input().split())

    print('#{} {}'.format(i, 1 if find(start, end, line_list) > 0 else 0))

