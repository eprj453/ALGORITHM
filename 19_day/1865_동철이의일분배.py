import sys
sys.stdin = open('1865_input.txt', 'r')


# def search(s, n, max_sum):
#     global max_per
#     if s == n:
#         print(temp)
#         # max_per = max(max_sum, max_per)
#     else:
#         for i in range(n):
#             if visited[i] or nums[s][i] == 0: continue
#             else:
#                 visited[i] = True
#                 search(s+1, n, max_sum*(nums[s][i] / 100))
#                 visited[i] = False

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

# def perm(arr, start, end):
#     global ans
#     if start == end:
#         max_sum = 1
#         for i in range(len(arr)):
#             max_sum *= (nums[i][arr[i]])/100
#         ans = max(ans, max_sum)
#         return
#     else:
#         for i in range(start, end):
#
#             # swap(arr, i, start)
#             # perm(arr, start+1, end)
#             # swap(arr, i, start)

def search(s, n, t_sum):
    global max_per
    if s == n:
        max_per = max(t_sum*100, max_per)
        # print(temp)
        # max_per = max(max_sum, max_per)
    else:
        for i in range(n):
            if visited[i]: continue
            else:
                if (t_sum * (nums[s][i]/100))*100 <= max_per:
                    continue
                # if t_sum * (nums[s][i] / 100) < max_per:
                #     continue
                # temp[s] = list1[s][i]
                # print('s : ', s, end=' ')
                # print('i :', i)
                visited[i] = True
                search(s+1, n, t_sum * (nums[s][i] / 100))
                visited[i] = False
            # else:
            #     visited[i] = True
            #     search(s+1, n, max_sum*(nums[s][i] / 100))
            #     visited[i] = False
            #
# list1 = [[0,-1,-2,-3], [-4,-5,-6,-7], [-8,-9,-10,-11], [-12,-13,-14,-15]]
# n = len(list1)
# visited = [False] * n
# temp = [0] * n
# max_per = -100
# search(0, n, 0)
# print(max_per)
for i in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    max_per = 0
    search(0, n, 1)
    # max_per = round(max_per, 6)
    # if len(str(max_per))
    print('#{}'.format(i), end = ' ')
    print('%.6f'%max_per)
