import sys
sys.stdin = open('4613_input.txt', 'r')


# def color(w, b, r, start, end, count):
#     global min_count
#     if start == end:
#         if b:
#             min_count = min(count, min_count)
#             return
#         else:
#             return
#     else:
#         if b == 0 and r == 0:
#             temp = 0
#             for i in range(len(flag[start])):
#                 if flag[start][i] != 'W':
#                     temp += 1
#             color(w + 1, b, r, start + 1, end, count+temp)
#
#         if r == 0:
#             temp = 0
#             for i in range(len(flag[start])):
#                 if flag[start][i] != 'B':
#                     temp += 1
#             color(w, b + 1, r, start + 1, end, count+temp)
#
#         if b != 0:
#             temp = 0
#             for i in range(len(flag[start])):
#                 if flag[start][i] != 'R':
#                     temp += 1
#             color(w, b, r + 1, start + 1, end, count+temp)

def dfs(s, e, count):
    if s == e:
        

for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    # c = 0
    # for j in range(m):
    #     if flag[len(flag)-1][j] != 'R':
    #         c += 1
    #     if flag[0][j] != 'W':
    #         c += 1

    min_count = 2501
    start, end = 1, n-1
    # color(0, 0, 0, start, end, 0)
    print('#{} {}'.format(i, c+min_count))
