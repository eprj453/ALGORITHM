import sys
sys.stdin = open('5189_input.txt', 'r')

# def search(s, e):
#     # print('돈다')
#     if s == e:
#         # print(f'--------{temp}---------')
#         back(0, n, temp)
#
#     else:
#         for i in range(n):
#             if visited[i] or s == i: continue
#             else:
#                 temp[s] = arr[i]
#                 visited[i] = True
#                 search(s+1, e)
#                 visited[i] = False
#
# def back(s, e, temp):
#     global ans
#     if s == e:
#         print(temp2)
#         min_sum = 0
#         for i in range(len(temp2)):
#             min_sum += nums[temp2[i]][i]
#         ans = min(ans, min_sum)
#     else:
#         for i in range(n):
#             if visited2[i] or s == i or temp[s] == arr[i]: continue
#             else:
#                 temp2[s] = arr[i]
#                 visited2[i] = True
#                 back(s+1, e, temp)
#                 visited2[i] = False
#
#
#
#
#
# for i in range(1, int(input())+1):
#     n = int(input())
#     nums = [list(map(int, input().split())) for _ in range(n)]
#     visited = [False] * n
#     visited2 = [False] * n
#     arr = list(range(n))
#     temp = [0] * n
#     temp2 = [0] * n
#     ans = 1000
#     search(0, n)
#     print(ans)

def perm(s, e):
    global min_distance
    if s == e:
        temp.insert(0, 1)
        temp.append(1)
        d_sum = 0
        for i in range(len(temp)-1):
            d_sum += nums[temp[i]-1][temp[i+1]-1]
        min_distance = min(min_distance, d_sum)
        temp.pop(0)
        temp.pop()
        return
    else:
        for i in range(0, n-1):
            if visited[i]: continue
            else:
                temp[s] = arr[i]
                visited[i] = True
                perm(s+1, e)
                visited[i] = False






for i in range(1, int(input()) + 1):
    n = int(input()) # 3, 4, 5
    nums = [list(map(int, input().split())) for _ in range(n)]
    arr = list(range(2, n+1))
    temp = [0] * (n-1)
    visited = [False] * (n-1)
    min_distance = 1000
    perm(0, n-1)
    print("#%d %d"%(i, min_distance))