import sys
sys.stdin = open('5122_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    for j in range(m):
        ope = list(input().split())
        if ope[0] == 'D':
            nums.pop(int(ope[1]))
        elif ope[0] == 'I':
            nums.insert(int(ope[1]), int(ope[2]))
        else:
            nums[int(ope[1])] = int(ope[2])
    print('#{} '.format(i), end = '')
    if l < len(nums):
        print(nums[l])
    else:
        print(-1)
