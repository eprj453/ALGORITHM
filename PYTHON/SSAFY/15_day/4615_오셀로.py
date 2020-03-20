import sys
sys.stdin = open('4615_input.txt', 'r')

# def dfs(x, y, s, board):
#     dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
#     stack = [[x, y]]
#     visited = []
#     for i in range(len(dx)):
#         visited.append([x + dx[i], y + dy[i]])
#     while len(stack) > 0:
#         for i in range(len(dx)):
#             if s == 1 and board[stack[0][0] + dx[i]][stack[0][1] + dy[i]] != 2:
#                 stack.append([stack[0][0] + dx[i], stack[0][1] + dy[i]])
#                 dir_x, dir_y = dx[i], dy[i]
#

# t = int(input())
# dx, dy = [-1, -1, -1 , 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
# for i in range(1, t+1):
#     n, m = map(int, input().split())
#     b_count, w_count = 2, 2
#     board = []
#     for j in range(n):
#         temp = [0] * n
#         board.append(temp)
#     board[(n//2)-1][(n//2)-1] = 2
#     board[(n//2)-1][n//2] = 1
#     board[n//2][(n//2)-1] = 1
#     board[n//2][n//2] = 2
#     for j in range(m):
#         x, y, s = map(int, input().split())
#         if s == 1:
#             # print('둔다 {}, {} {}'.format(s, x-1, y-1))
#             board[x-1][y-1] = 1
#             b_count += 1
#             for k in range(len(dx)):
#                 if (x-1) + dx[k] >=0 and (x-1) + dx[k] < n and (y-1) + dy[k] >= 0 and (y-1) + dy[k] < n:
#                     # print('check, {} {}'.format((x-1) + dx[k], (y-1) + dy[k]))
#                     if board[(x-1)+dx[k]][(y-1)+dy[k]] == 2:
#                         temp = [[(x-1)+dx[k], (y-1)+dy[k]]]
#                         dir_x, dir_y = dx[k], dy[k]
#                         # print('temp 1 : ', temp)
#                         while True:
#                             if (x-1)+dx[k]+dir_x >= n or (x-1)+dx[k]+dir_x < 0 or \
#                                 (y-1) + dy[k] + dir_y >= n or (y-1) + dy[k] + dir_y < 0 or \
#                                 board[(x-1)+dx[k]+dir_x][(y-1) + dy[k] + dir_y] == 0:
#                                 break
#                             if board[(x-1) + dx[k] + dir_x][(y-1) + dy[k] + dir_y] == 2:
#                                 temp.append([(x-1) + dx[k] + dir_x, (y-1) + dy[k] + dir_y])
#
#                             elif board[(x-1) + dx[k] + dir_x][(y-1) + dy[k] + dir_y] == 1:
#                                 for check in temp:
#                                     board[check[0]][check[1]] = 1
#                                     w_count -= 1
#                                     b_count += 1
#                                     # print('검은돌, 흰돌 : {}, {}'.format(b_count, w_count))
#                                     # for m in range(n):
#                                     #     print(board[m])
#                                 break
#                             dir_x += dx[k]
#                             dir_y += dy[k]
#
#
#         elif s == 2:
#             board[x-1][y-1] = 2
#             # print('둔다 {}, {} {}'.format(s, x - 1, y - 1))
#             w_count += 1
#             for k in range(len(dx)):
#                 if (x - 1) + dx[k] >= 0 and (x - 1) + dx[k] < n and (y - 1) + dy[k] >= 0 and (y - 1) + dy[k] < n:
#                     # print('check, {} {}'.format((x - 1) + dx[k], (y - 1) + dy[k]))
#                     if board[(x - 1) + dx[k]][(y - 1) + dy[k]] == 1:
#                         temp = [[(x - 1) + dx[k], (y - 1) + dy[k]]]
#                         dir_x, dir_y = dx[k], dy[k]
#                         while True:
#                             # print('temp 2 : ', temp)
#                             if (x-1) + dx[k] + dir_x >= n or (x-1) + dx[k] + dir_x < 0 or \
#                                 (y-1) + dy[k] + dir_y >= n or (y-1) + dy[k] + dir_y < 0 or \
#                                 board[(x-1)+dx[k]+dir_x][(y-1) + dy[k] + dir_y] == 0:
#                                 break
#                             if board[(x - 1) + dx[k] + dir_x][(y - 1) + dy[k] + dir_y] == 1:
#                                 temp.append([(x - 1) + dx[k] + dir_x, (y - 1) + dy[k] + dir_y])
#
#                             elif board[(x - 1) + dx[k] + dir_x][(y - 1) + dy[k] + dir_y] == 2:
#                                 for check in temp:
#                                     board[check[0]][check[1]] = 2
#                                     w_count += 1
#                                     b_count -= 1
#                                     # print('검은돌, 흰돌 : {}, {}'.format(b_count, w_count))
#                                     # for m in range(n):
#                                     #     print(board[m])
#                                 break
#                             dir_x += dx[k]
#                             dir_y += dy[k]
#
#     print('#{} {} {}'.format(i, b_count, w_count))



t = int(input())
dx, dy = [-1, -1, -1 , 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
for i in range(1, t+1):
    n, m = map(int, input().split())
    b_count, w_count = 2, 2
    board = []
    for j in range(n):
        temp = [0] * n
        board.append(temp)
    board[(n//2)-1][(n//2)-1] = 2
    board[(n//2)-1][n//2] = 1
    board[n//2][(n//2)-1] = 1
    board[n//2][n//2] = 2
    for j in range(m):
        x, y, s = map(int, input().split())
        x ,y = x-1, y-1
        board[x][y] = s
        if s == 1:
            b_count += 1
        else:
            w_count += 1
        for k in range(len(dx)):
            if x + dx[k] >=0 and x + dx[k] < n and y + dy[k] >= 0 and y + dy[k] < n:
                if board[x+dx[k]][y+dy[k]] != s and board[x+dx[k]][y+dy[k]] != 0:
                    temp = [[x+dx[k], y+dy[k]]]
                    dir_x, dir_y = dx[k], dy[k]
                    while True:
                        if x+dx[k]+dir_x >= n or x+dx[k]+dir_x < 0 or \
                            y + dy[k] + dir_y >= n or y + dy[k] + dir_y < 0 or \
                            board[x+dx[k]+dir_x][y + dy[k] + dir_y] == 0:
                            break
                        if board[x + dx[k] + dir_x][y + dy[k] + dir_y] != s:
                            temp.append([x + dx[k] + dir_x, y + dy[k] + dir_y])

                        elif board[x + dx[k] + dir_x][y + dy[k] + dir_y] == s:
                            for check in temp:
                                board[check[0]][check[1]] = s
                                if s == 1:
                                    w_count -= 1
                                    b_count += 1
                                elif s == 2:
                                    w_count += 1
                                    b_count -= 1
                            break
                        dir_x += dx[k]
                        dir_y += dy[k]

    print('#{} {} {}'.format(i, b_count, w_count))