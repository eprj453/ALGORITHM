import sys
sys.stdin = open('s_input.txt', 'r')


def perm(k, start):
    global max_val
    if k == r:
        temp = ans[0] * ans[1]
        temp2 = str(temp)
        result = True
        for j in range(len(temp2) - 1):
            if temp2[j] > temp2[j + 1]:
                result = False
                break
        if temp > max_val and result == True:
            max_val = temp
    else:
        for i in range(start, l):
            ans[k] = nums[i]
            perm(k+1, i+1)

    return max_val

t = int(input())
for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    l = len(nums)
    ans = [True] * 2
    r = 2
    max_val = 0
    # if perm(0, 0) == 0:
    print('#{} {}'.format(i, perm(0,0) if perm(0,0) != 0 else -1))
    # else:
    #     print('#{} {}'.format(i, perm(0, 0)))