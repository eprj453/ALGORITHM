import sys
sys.stdin = open('merge_input.txt', 'r')
from collections import deque


def merge_sort(lo, hi):
    global count
    if lo == hi: return
    mid = (lo + hi) >> 1
    merge_sort(lo, mid)  # 왼쪽
    merge_sort(mid + 1, hi)  # 오른쪽
    i, j, k = lo, mid + 1, lo


    if nums[i] > nums[j]:
        count += 1

    while i <= mid and j <= hi:
        if nums[i] < nums[j]:
            tmp[k] = nums[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = nums[j]
            j, k = j + 1, k + 1

    while i <= mid:
        tmp[k] = nums[i]
        i, k = i + 1, k + 1

    while j <= hi:
        tmp[k] = nums[j]
        j, k = j + 1, k + 1

    for i in range(lo, hi + 1):
        nums[i] = tmp[i]


for i in range(1, int(input())+1):
    n = int(input())
    count = 0
    nums = list(map(int, input().split()))
    tmp = [0] * len(nums)
    merge_sort(0, len(nums)-1)
    print(tmp)
    print('#{} {} {}'.format(i, tmp[n//2],  count))
    # print(count)
