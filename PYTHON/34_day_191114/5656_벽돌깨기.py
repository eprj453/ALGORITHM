from collections import deque
import copy
import sys
sys.stdin = open('5656_input.txt', 'r')

# def copy(arr):
#     temp = []
#     for i in range(len(arr)):
#         temp.append(arr[i])
#     return temp


# def drop(s, remain, maps):
#     global min_remain
#
#     if s == n or remain == 0:
#         min_remain = min(min_remain, remain)
#         return
#
#     for i in range(w):
#         cnt = 0
#         # cnt = 0
#         x, y = 0, i
#         is_block = False
#         while x < h:
#             if maps[x][y] != 0:
#                 is_block = True
#                 break
#             else:
#                 x += 1
#         # copy = copy()
#
#         temp_map = copy.deepcopy(maps)
#         temp_map = [maps[j][:] ]
#
#         if is_block: # 부술수 있는 벽돌 존재
#             #
#             # print('부술 벽돌 : ', x, y)
#             # print('부순 횟수 : ', s)
#             # for j in range(w):
#             #     print(maps[j])
#             # print()
#             block_visited = []
#             for _ in range(h):
#                 temp = [False] * w
#                 block_visited.append(temp)
#             haveToBreak = [[x, y]]
#             q = []
#             q.append([x, y])
#             block_visited[x][y] = True
#
#             while q:
#                 b = q.pop(0)
#                 x2, y2 = b[0], b[1]
#
#                 if maps[x2][y2] == 1:
#                     if block_visited[x2][y2] == False:
#                         block_visited[x2][y2] = True
#                         haveToBreak.append([x2, y2])
#                 else:
#                     for k in range(len(dx)):
#                         d_x, d_y = dx[k], dy[k]
#                         start, end = 0, maps[x2][y2]-1
#                         while start < end:
#                             if 0 <= x2 + d_x < h and 0 <= y2 + d_y < w:
#                                 if maps[x2+d_x][y2+d_y] >= 1 and block_visited[x2+d_x][y2+d_y] == False:
#                                     if maps[x2+d_x][y2+d_y] >= 2:
#                                         q.append([x2 + d_x, y2 + d_y])
#                                     block_visited[x2+d_x][y2+d_y] = True
#                                     haveToBreak.append([x2 + d_x, y2 + d_y])
#                             else:
#                                 break
#                             d_x += dx[k]
#                             d_y += dy[k]
#                             start += 1
#
#             for b in haveToBreak:
#                 if temp_map[b[0]][b[1]] != 0:
#                     temp_map[b[0]][b[1]] = 0
#             cnt = len(haveToBreak)
#
#             for j in range(w):
#                 for k in range(h-2, -1, -1):
#                     if temp_map[k][j] != 0 and temp_map[k+1][j] == 0:
#                         x, y = k, j
#                         while x < h-1:
#                             if x == h-2 and temp_map[x+1][y] == 0:
#                                 temp_map[x+1][y] = temp_map[k][j]
#                                 temp_map[k][j] = 0
#                             if temp_map[x+1][y] != 0:
#                                 temp_map[x][y] = temp_map[k][j]
#                                 temp_map[k][j] = 0
#                                 break
#                             else:
#                                 x += 1
#             # print([x, y])
#             # print('부서지는 벽돌들 : ',haveToBreak)
#             # for j in range(w):
#             #     print(temp_map[j])
#             # print()
#             drop(s+1, remain-cnt, temp_map)
#
#
#
#
#
#
#
#
# #
# # arr = list(range(12))
# # temp = []
# # n = 4
# # cnt = 0
# # func(0)
# # print(cnt)
#
#
# dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# for i in range(1, int(input())+1):
#     n, w, h = map(int, input().split())
#     b = 0
#     blocks = []
#     for _ in range(h):
#         temp = list(map(int, input().split()))
#         b += (w - temp.count(0))
#         blocks.append(temp)
#     min_remain = b
#     drop(0, b, blocks)
#     print('#{} {}'.format(i, min_remain))

    # print(b)



def drop(s):
    if s == n:
        print(temp)
        return
    for k in range(len(breaks)):
        temp.append(breaks[k])
        drop(s+1)
        temp.pop()


for i in range(1, int(input())+1):
    n, w, h = map(int, input().split())
    b = 0
    blocks = []
    for _ in range(h):
        temp = list(map(int, input().split()))
        b += (w - temp.count(0))
        blocks.append(temp)
    min_remain = b
    breaks = []
    for j in range(w):
        count = 0
        while count < h:
            result = False
            if blocks[count][j] != 0: # 칠 수 있는 벽돌이 존재
                c = count
                for k in range(c, c+n):
                    if k + 1 == h:
                        break
                    if blocks[k][j] > 1:
                        breaks.append(j)
                        result = True
                        break
            if result:
                break
            count += 1
    print(breaks)
    temp = []
    drop(0)
    print()





































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
