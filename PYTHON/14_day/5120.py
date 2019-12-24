import sys
sys.stdin = open('5120_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    idx = 0
    count = 1
    for j in range(k):
        idx += m
        if idx > len(nums):
            idx = idx % len(nums)
        # if idx % len(nums) == 0:
        #     nums.insert(0, nums[len(nums)-1] + nums[0])
        if idx % len(nums) == 0:
            nums.insert(len(nums)+1, nums[len(nums)-1] + nums[0])
        else:
            nums.insert(idx % len(nums), nums[(idx % len(nums))] + nums[(idx % len(nums))-1])
    # for j in range(len(nums)-1, len(nums)- 11, -1):
    #     print(nums[j], end = ' ')
    count = -1
    n = 0
    print('#{} '.format(i), end = '')
    while count < len(nums)-1:
        print(nums[count], end = ' ')
        if count < -9:
            break
        n += 1
        count -= 1
    print()


