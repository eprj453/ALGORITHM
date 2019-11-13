from collections import deque
# import copy
import sys
# sys.stdin = open('5656_input.txt', 'r')

def comb(k, start):
    global cnt
    if k == n:
        print(temp)
        cnt += 1
        return

    for i in range(start, len(arr)):
        temp.append(arr[i])
        comb(k+1, i+1)
        temp.pop()


n = 4
arr = list(range(12))
temp = []
print(temp)
cnt = 0
visited = [False] * len(arr)
comb(0, 0)
print(cnt)
# def drop(s, remain_block, maps):
#     global min_remain
#     if s == n:
#         min_remain = min(min_remain, remain_block)
#         return
#
#     for k in range(h):
#         cnt = 0
#         x, y = 0, k
#         is_block = False
#         while x < h:
#             if maps[x][y] != 0:
#                 is_block = True
#                 break
#             else:
#                 x += 1
#
#         if is_block:
#             visited = [[False] * w for _ in range(h)]
#             visited[x][y] = True
#             haveToBreak = [[x, y]]
#             q = deque()
#             q.append([x, y])
#             while q:
#                 x2, y2 = q[0][0], q[0][1]
#                 if maps[x2][y2] == 1:
#                     q.popleft()
#                 else:
#                     for l in range(len(dx)):
#                         d_x, d_y = dx[l], dy[l]
#                         start, end = 0, maps[x2][y2]
#                         while start < end:
#                             if not 0 <= x2 + d_x < h or not 0 <= y2 + d_y < w:
#                                 break
#                             if maps[x2+d_x][y2+d_y] != 0 and visited[x2+d_x][y2+d_y] == False:
#                                 haveToBreak.append([x2+d_x, y2+d_y])
#                                 q.append([x2+d_x, y2+d_y])
#                                 visited[x2+d_x][y2+d_y] = True
#                             d_x += d_x
#                             d_y += d_y
#                             start += 1
#                     q.popleft()
#             print(haveToBreak)
#             cnt = len(haveToBreak)
#             for b in haveToBreak:
#                 maps[b[0]][b[1]] = 0
#
#             for b in range(w):
#                 for c in range(h-2, -1, -1):
#                     if maps[c][b] != 0 and maps[c+1][b] == 0:
#                         t_x = c
#                         while t_x < h-1:
#                             if maps[t_x][b] == 0:
#                                 t_x += 1
#                             else:
# #                                 break
# #                         maps[t_x][b] = maps[c][b]
# #                         maps[c][b] = 0
# #
# #         drop(s+1, remain_block - cnt, maps)
#
#
#



#
#
#
# dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# for i in range(1, int(input())+1):
#     n, w, h = map(int, input().split())
#     maps = []
#     blocks = 0
#     for _ in range(w):
#         temp = list(map(int, input().split()))
#         blocks += (w - temp.count(0))
#         maps.append(temp)
#     # temp_maps = copy.deepcopy(maps)
#     min_remain = blocks
#     drop(0, blocks, maps)
#     print(min_remain)
#
