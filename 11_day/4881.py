# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     list1 = list(range(n))
#     check = []
#     for j in range(1 << n):
#         for k in list1:
#             if j & (1 << k):
#                 check.append(1)
#             else:
#                 check.append(0)
#         print(check)
#     # n = int(input())
#     # nums = [list(map(int, input().split())) for _ in range(n)]
#     # visited = [[False]*n for _ in range(n)]
#     # # print(nums)
#     # for j in range(n):
#     #     for k in range(n):

t = int(input())
for i in range(1, t+1):
    n = int(input())
    list1 = list(range(n))
    nums = [list(map(int, input().split())) for _ in range(n)]

    R = n

    N = len(a)

    visited = False * N

    T = [0] * R

    perm(0)

    def perm(k):
        if k == R:
            return t
        else:
            for i in range(N):
                if visited[i] == True:
                    continue
                else:
                    t[k] = a[i]
                    visited[i] = True
                    perm(k + 1)
                    visited[i] = False


    perm(0)