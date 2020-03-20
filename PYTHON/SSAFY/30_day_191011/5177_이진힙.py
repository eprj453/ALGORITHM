# class Node:
#     def __init(self, data):
#         self.data = data
#
# class BinaryHeap:
#     def __init__(self):
#         self.parent = None
#         self.l_child = None
#         self.r_child = None
#
#
#     def insertChild(self):

import sys
sys.stdin = open('5177_input.txt', 'r')

# def tree(k):
#     global idx
#     global n
#


for i in range(1, int(input()) + 1):
    n = int(input())
    idx = 1
    nums = list(map(int, input().split()))
    binaryHeap = [0] * (n + 1)
    for num in nums:
        binaryHeap[idx] = num
        if idx // 2 >= 1:
            t_idx = idx
            while binaryHeap[t_idx] < binaryHeap[t_idx // 2]:
                binaryHeap[t_idx], binaryHeap[t_idx // 2] = binaryHeap[t_idx // 2], binaryHeap[t_idx]
                t_idx = t_idx // 2
        idx += 1

    ans, idx = 0, n
    while idx > 1:
        idx //= 2
        ans += binaryHeap[idx]

    print('#{} {}'.format(i, ans))
    # print(3//2)