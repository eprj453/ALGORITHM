import sys
sys.stdin = open('5176_input.txt', 'r')

def tree(k):
    global idx
    global n

    if k <= n:
        tree(k * 2)
        nums[k] = idx
        idx += 1
        tree((k*2)+1)



for i in range(1, int(input())+1):
    n = int(input())
    nums = [0] * (n+1)
    idx = 1
    tree(1)
    print('#{} {} {}'.format(i, nums[1], nums[n//2]))
    print(nums)
    # tree = []




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.l_child = None
#         self.r_child = None
#
#
#
# class Tree:
#     def __init__(self):
#         self.head = None
#         self.l_child = None
#         self.r_child = None
#         self.NodeCount = 0
#
#     def getNode(self, pos):
#         if pos < 1 or pos > self.NodeCount:
#             return False
#
#         else:
#             i = 1
#             now = self.head
#








for i in range(1, int(input())+1):
    n = int(input())
    nodes = list(range(1, n+1))
    print(nodes)