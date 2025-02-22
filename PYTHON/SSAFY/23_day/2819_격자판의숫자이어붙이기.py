import sys
sys.stdin = open('2819_input.txt', 'r')


def my_func(x, y, num, length):

    if length == 7:
        ans_list.add(num)
        return
    for l in range(len(dx)):
        if 0 <= x + dx[l] < 4 and 0 <= y + dy[l] < 4:
            my_func(x + dx[l], y + dy[l], num + nums[x+dx[l]][y+dy[l]], length+1)


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(1, int(input()) + 1):
    visited = []
    for j in range(4):
        temp = [False] * 4
        visited.append(temp)
    nums = [list(input().split()) for _ in range(4)]
    ans_list = set()
    for j in range(4):
        for k in range(4):
            my_func(j , k, nums[j][k], 1)
    # print(ans_list)
    print('#{} {}'.format(i, len(ans_list)))
    print(ans_list)
