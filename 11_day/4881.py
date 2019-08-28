import sys
sys.stdin = open('4881_input.txt', 'r')


# def perm(k):
#

# def perm(k, perm_list, n, nums):
#     N = len(perm_list)
#     R = n
#     global min_val
#     visited = [False] * N
#     T = [0] * R
#     if k == R: # ex, [0, 1, 2]
#         temp = 0
#         for j in range(len(nums)):
#             print(T)
#             temp += nums[j][T[j]]
#         if min_val > temp:
#             min_val = temp
#     else:
#         for i in range(N):
#             if visited[i] == True:
#                 continue
#             else:
#                 T[k] = perm_list[i]
#                 visited[i] = True
#                 perm(k+1, perm_list, n, nums)
#                 visited[i] = False
#     return min_val
#
# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     min_val = 10000
#     perm_list = list(range(n))
#     nums = [list(map(int, input().split())) for _ in range(n)]
#     print(perm(0, perm_list, n, nums))
    # R = n
    # N = len(perm_list)
    # visited = False * N
    # T = [0] * R
    # min_val = 10000
    # perm(0)
    # print(min_val)

    # perm(0)