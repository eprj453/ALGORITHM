# def bishop(s, e, count):
#     global max_count
#     t = 0
#     for i in range(s, b_len):
#         result2 = True
#         x, y = b_list[i][0], b_list[i][1]
#         for k in range(len(dx)):
#             if result2 == False: break
#             d_x, d_y = dx[k], dy[k]
#             while 0 <= x + d_x < n and 0 <= y + d_y < n:
#                 if chess[x + d_x][y + d_y] == 'B':
#                     result2 = False
#                     break
#                 d_x += dx[k]
#                 d_y += dy[k]
#         if result2 == True:
#             t += 1
#     # print(t)
#     # t : 앞으로 둘 수 있는 최대 bishop
#     if t + count <= max_count:
#         return
#
#     # if count + (b_len - s) <= max_count:
#     #     # print('return', count + (b_len - s + 1))
#     #     return
#
#     if s == e:
#         # print('max_count : ', max_count)
#         # print('count + (b_len - s+1)', count + (b_len - s+1))
#         # for i in range(n):
#         #     print(chess[i])
#         # print()
#         max_count = max(max_count, count)
#         return
#     # if s == e:
#     #     count = 0
#     #     for i in range(n):
#     #         print(chess[i])
#     #     print()
#     #     result = True
#     #     for i in range(n):
#     #         if result == False: break
#     #         for j in range(n):
#     #             if chess[i][j] == 'B':
#     #                 count += 1
#     #                 x, y = i, j
#     #                 for k in range(len(dx)):
#     #                     if result == False: break
#     #                     delta_x, delta_y = dx[k], dy[k]
#     #                     while 0 <= x + delta_x < n and 0 <= y + delta_y < n:
#     #                         if chess[x+delta_x][y+delta_y] == 'B':
#     #                             result = False
#     #                             break
#     #                         delta_x += dx[k]
#     #                         delta_y += dy[k]
#     #     if count <= max_count:
#     #         return
#     #     if result == True:
#     #         max_count = max(max_count, count)
#     #         print('max : ', max_count)
#     #         return
#     #     else:
#     #         return
#
#
#     # x, y = b_list[s][0], b_list[s][1]
#     result = True
#     for k in range(len(dx)):
#         x, y = b_list[s][0], b_list[s][1]
#         if result == False: break
#         d_x, d_y = dx[k], dy[k]
#         while 0 <= x + d_x < n and  0 <= y + d_y < n:
#             if chess[x+d_x][y+d_y] == 'B':
#                 result = False
#                 break
#             d_x += dx[k]
#             d_y += dy[k]
#     if result:
#         # print('x, y : , count : , ',x, y, count+1)
#         chess[x][y] = 'B'
#         # for i in range(n):
#         #     print(chess[i])
#         # print()
#         bishop(s+1, e, count+1)
#         chess[x][y] = 1
#         # for i in range(n):
#         #     print(chess[i])
#         # print()
#         bishop(s+1, e, count)
#                 # visited[i] = False
#     else:
#         bishop(s+1, e, count)
#
#         # if chess[b_list[i][0]][b_list[1][1]] == 'B': continue
#         # else:
#         #     chess[b_list[i][0]][b_list[i][1]] = 'B'
#         #     bishop(s+1 , e, count+1)
#         #     chess[b_list[i][0]][b_list[i][1]] = 1
#         #     bishop(s+1, e, count)
#
#
#
#
# n = int(input())
# chess = [list(map(int, input().split())) for _ in range(n)]
# b_list = []
# visited = []
# for i in range(n):
#     for j in range(n):
#         if chess[i][j] == 1:
#             b_list.append([i, j])
#             visited.append(False)
# # print(b_list)
# b_len = len(b_list)
# dx, dy = [-1, 1, -1, 1], [1, -1, -1, 1]
# max_count = 0
# bishop(0, b_len, 0)
# print(max_count)


def bishop(s, e, count):
    global max_count
    # t = 0
    # for i in range(s, b_len):
    #     result2 = True
    #     x, y = b_list[i][0], b_list[i][1]
    #     for k in range(len(dx)):
    #         if result2 == False: break
    #         d_x, d_y = dx[k], dy[k]
    #         while 0 <= x + d_x < n and 0 <= y + d_y < n:
    #             if chess[x + d_x][y + d_y] == 'B':
    #                 result2 = False
    #                 break
    #             d_x += dx[k]
    #             d_y += dy[k]
    #     if result2 == True:
    #         t += 1
    # # print(t)
    # # t : 앞으로 둘 수 있는 최대 bishop
    # if t + count <= max_count:
    #     return

    if s == e:
        max_count = max(max_count, count)
        return

    x, y  = b_list[s][0], b_list[s][1]
    if visited[x][y] == False: # 둘 수 있고 1인 곳
        print('s, e : ',s, e)
        print('visited : ', x, y)
        visited[x][y] = False
        bishop(s+1, e, count)
        visited[x][y] = True # 더 이상 둘 수 없도록
        for i in range(len(dx)):
            d_x, d_y = dx[i], dy[i]
            while 0 <= x + d_x < n and 0 <= y + d_y < n:
                if chess[x+d_x][y+d_y] == 1 and visited[x+d_x][y+d_y] == False:
                    visited[x+d_x][y+d_y] = True
                d_x += dx[i]
                d_y += dy[i]
        for i in range(n):
            print(visited[i])
        print()
        bishop(s+1, e, count+1)
    else:
        bishop(s+1, e, count)


n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
b_list = []
visited = []
for i in range(n):
    temp = [False] * n
    for j in range(n):
        if chess[i][j] == 1:
            b_list.append([i, j])
    visited.append(temp)
print('visited start')
print('b_list : ',b_list)
for i in range(n):
    print(visited[i])
b_len = len(b_list)
dx, dy = [-1, 1, -1, 1], [1, -1, -1, 1]
max_count = 0
bishop(0, b_len, 0)
print(max_count)