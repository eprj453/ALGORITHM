import sys
sys.stdin = open('merge_input.txt', 'r')

def merge_sort(lo, hi):
    global count
    if lo == hi: return
    mid = (lo + hi - 1) >> 1
    merge_sort(lo, mid)  # 왼쪽
    merge_sort(mid + 1, hi)  # 오른쪽
    i, j, k = lo, mid + 1, lo


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

    if nums[mid] > nums[hi]:
        count += 1

    for i in range(lo, hi + 1):
        nums[i] = tmp[i]


for i in range(1, int(input())+1):
    n = int(input())
    count = 0
    nums = list(map(int, input().split()))
    tmp = [0] * len(nums)
    merge_sort(0, len(nums)-1)

    print('#{} {} {}'.format(i, tmp[n//2],  count))
    # print(count)

# def merge_sort(t_list):
#     global count
#     n = len(t_list)
#
#     if n == 1:  # 길이가 1이 되는 순간. 더 이상 나눌 수 없을때까지 나누면 리스트를 return,
#         return t_list[0]  # 트리의 윗가지부터 연산 시작
#
#     mid = n // 2
#
#     l1 = merge_sort(t_list[0:mid])  # 리스트 계속 나누기(왼쪽)
#     l2 = merge_sort(t_list[mid:n])  # 리스트 계속 나누기(오른쪽)
#
#     # 리스트 길이가 1이면 return이 시작되고 이하 연산 시작.
#
#
#     if l1 > l2:
#         print('l1, l2 :',l1, l2)
#         count += 1
#         return l1
#     else:
#         return l2
#
#
# for i in range(1, int(input()) + 1):
#     n = int(input())
#     count = 0
#     nums = list(map(int, input().split()))
#     ans = merge_sort(nums)
#     nums.sort()
#     print(ans)
#     print('#{} {} {}'.format(i, nums[n//2], count))