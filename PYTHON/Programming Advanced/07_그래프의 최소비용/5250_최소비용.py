import sys
sys.stdin = open('5250_input.txt', 'r')

def min_fare(x, y, z, d):
    global min_distance

    # if z >= min_distance:
    #     print('return, ', z)
    #     return

    if d == (n-1) * 2:
        print('x, y :', x, y)
        print('z : ', z)
        print()
        min_distance = min(min_distance, z)
        return

    p_val = maps[x][y]
    min_val = 1000
    for k in range(len(dx)):
        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
            if maps[x+dx[k]][y+dy[k]] - p_val < min_val:
                min_val = maps[x+dx[k]][y+dy[k]] - p_val

    for k in range(len(dx)):
        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
            if maps[x+dx[k]][y+dy[k]] - p_val <= min_val:
                if maps[x+dx[k]][y+dy[k]] == p_val:
                    min_fare(x+dx[k], y+dy[k], z+1, d+1)
                else:
                    min_fare(x + dx[k], y + dy[k], z + 1 + min_val, d + 1)
            #     visited[x + dx[k]][y + dy[k]] = True
            #     min_fare(x+dx[k], y+dy[k], z+1+min_val, d+1)
            #
            # if p_val > maps[x+dx[k]][y+dy[k]] and visited[x+dx[k]][y+dy[k]] == False:
            #     visited[x + dx[k]][y + dy[k]] = True
            #     min_fare(x+dx[k], y+dy[k], z+1, d+1)
            # elif p_val > maps[x+dx[k]][y+dy[k]]:
            #     min_fare(x+dx[k], y+dy[k], z+1, d+1)


dx, dy = [0, 1], [1, 0]
for i in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    min_distance = 100 * 100 * 1000
    # memo = [0] * (((n-1)*2)+1)
    # visited = []
    # for j in range(n):
    #     temp = [False] * n
    #     visited.append(temp)
    # print(memo)
    min_fare(0, 0, 0, 0)
    # print('#{} {}'.format(i, min_distance))
    # print(memo)
    print('#{} {}'.format(i, min_distance))


# def min_fare(q):
#     if not q:
#         return
#     global min_distance
#     new_q = []
#     min_val = 1000
#
#     for k in range(len(q)):
#         x, y, z = q[k][0], q[k][1], q[k][2]
#         if x == n - 1 and y == n - 1:
#             min_distance = min(min_distance, z)
#             return
#         for l in range(len(dx)):
#             if 0 <= x + dx[l] < n and 0 <= y + dy[l] < n:
#                 if abs(maps[x + dx[l]][y + dy[l]] - maps[x][y]) <= min_val:
#                     min_val = abs(maps[x + dx[l]][y + dy[l]] - maps[x][y])
#
#     for k in range(len(q)):
#         x, y, z = q[k][0], q[k][1], q[k][2]
#         for l in range(len(dx)):
#             if 0 <= x + dx[l] < n and 0 <= y + dy[l] < n:
#                 if abs(maps[x + dx[l]][y + dy[l]] - maps[x][y]) == min_val and visited[x + dx[l]][y + dy[l]] == False:
#                     new_q.append([x + dx[l], y + dy[l], z + 1 + abs(maps[x + dx[l]][y + dy[l]] - maps[x][y])])
#                     visited[x + dx[l]][y + dy[l]] = True
#
#     min_fare(new_q)
#
#
# dx, dy = [0, 1], [1, 0]
# for i in range(1, int(input()) + 1):
#     n = int(input())
#     maps = [list(map(int, input().split())) for _ in range(n)]
#     visited = []
#     for j in range(n):
#         temp = [False] * n
#         visited.append(temp)
#     min_distance = 100 * 100 * 1000
#     visited[0][0] = True
#     qq = [[0, 0, 0]]
#     min_fare(qq)
#     print('#{} {}'.format(i, min_distance))