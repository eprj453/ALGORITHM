# import sys
# sys.stdin = open('1865_input.txt', 'r')


# def search(s, n, max_sum):
#     global max_per
#     if s == n:
#         max_per = max(max_sum, max_per)
#     else:
#         for i in range(n):
#             if visited[i] or nums[s][i] == 0: continue
#             else:
#                 visited[i] = True
#                 search(s+1, n, max_sum*(nums[s][i] / 100))
#                 visited[i] = False

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def perm(arr, start, end):
    global ans
    if start == end:
        max_sum = 1
        for i in range(len(arr)):
            max_sum *= (nums[i][arr[i]])/100
        ans = max(ans, max_sum)
        return
    else:
        for i in range(start, end):
            swap(arr, i, start)
            perm(arr, start+1, end)
            swap(arr, i, start)



#
for i in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    arr = list(range(n))
    temp = [0] * n
    ans = 100
    perm(arr, 0, len(arr))
    print('#{} {}'.format(i, max_per))
