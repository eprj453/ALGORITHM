import copy
import sys
sys.stdin = open('2105_input.txt', 'r')

# def find(x, y, distance, d_visited, w_visited, start):
#     # print('호출')
#     global max_distance
#     if [x, y] == start and distance > 1:
#         # print('distance, max_distance : ',distance, max_distance)
#         # print('호출')
#         max_distance = max(distance, max_distance)
#         return
#
#
#     for k in range(len(dx)):
#         # dessert = desserts[x+dx[k]][y+dy[k]]
#         if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n:
#             dessert = desserts[x + dx[k]][y + dy[k]]
#             if [x+dx[k], y+dy[k]] == start and distance > 1:
#                 # print('호출')
#                 find(x+dx[k], y+dy[k], distance+1, d_visited, w_visited, start)
#             else:
#                 if d_visited[dessert] == False and w_visited[x+dx[k]][y+dy[k]] == False:
#                     # copy_d, copy_w = copy.deepcopy(d_visited), copy.deepcopy(w_visited)
#                     # copy_d[dessert] = True
#                     # copy_w[x+dx[k]][y+dy[k]] = True
#                     d_visited[dessert] = True
#                     w_visited[x+dx[k]][y+dy[k]] = True
#                     find(x+dx[k], y+dy[k], distance+1, d_visited, w_visited, start)
#                     d_visited[dessert] = False
#                     w_visited[x + dx[k]][y + dy[k]] = False
#
#
#
#
#
#
# dx, dy = [1, -1, 1, -1], [-1, 1, 1, -1]
# for i in range(1, int(input())+1):
#     n = int(input())
#     # visited = [False] * 101
#     desserts = [list(map(int, input().split())) for _ in range(n)]
#     d_visited = [False] * 101
#     w_visited = [[False] * n for _ in range(n)]
#     max_distance = 0
#     for j in range(n):
#         for k in range(n):
#             d_visited[desserts[j][k]] = True
#             w_visited[j][k] = True
#             find(j, k, 0, d_visited, w_visited, [j, k])
#             d_visited[desserts[j][k]] = False
#             w_visited[j][k] = False
#     print(max_distance)

def find(x, y, path, is_back, can_go):
    global max_d
    if x == j and y == k and is_back == True:
        result = True
        for go in can_go:
            if not go > 0:
                result = False
                break
        if result == True:
            max_d = max(path, max_d)
        return

    start = 0
    for i in range(4, 0, -1):
        # print(can_go)
        if can_go[i-1] != 0:
            start = i
            break

    for i in range(start, 4):
        d_x, d_y = dx[i], dy[i]
        if 0 <= x + d_x < n and 0 <= y + d_y < n:
            f_des = maps[x + d_x][y + d_y]
            if x+d_x == j and y+d_y == k:
                can_go[i] += 1
                find(x+d_x, y+d_y, path+1, True, can_go)
                can_go[i] -= 1
            elif d_visited[f_des] == False and w_visited[x+d_x][y+d_y] == False:
                d_visited[f_des] = True
                w_visited[x+d_x][y+d_y] = True
                can_go[i] += 1
                find(x+d_x, y+d_y, path+1, False, can_go)
                can_go[i] -= 1
                w_visited[x+d_x][y+d_y] = False
                d_visited[f_des] = False


    #     # if len(path) >= 3:
    #     #     max_d = max(len(path), max_d)
    #     #     return
    #     # else:
    #     #     return
    #
    # for l in range(len(dx)):
    #     if 0 <= x+dx[l] < n and 0 <= y+dy[l] < n:
    #         f_des = maps[x+dx[l]][y+dy[l]]
    #         if len(path) >= 3 and x+dx[l] == j and y+dy[l] == k:
    #             find(x+dx[l], y+dy[l], path, True)
    #         elif d_visited[f_des] == False and w_visited[x+dx[l]][y+dy[l]] == False:
    #             d_visited[f_des] = True
    #             w_visited[x+dx[l]][y+dy[l]] = True
    #             path.append(f_des)
    #             find(x+dx[l], y+dy[l], path, False)
    #             path.pop()
    #             # d_visited[f_des] = False
    #             # w_visited[x+dx[l]][y+dy[l]] = False

dx, dy = [1, 1, -1, -1], [-1, 1, 1, -1]
for a in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    max_d = 0
    for j in range(n):
        for k in range(n):
            if (j == 0 and k == 0) or (j == 0 and k == n-1) or (j == n-1 and k == 0) or (j == n-1 and k == n-1):
                continue
            else:
                des = maps[j][k]
                d_visited = [False] * 101
                w_visited = [[False] * n for _ in range(n)]
                d_visited[des] = True
                w_visited[j][k] = True
                find(j, k, 0, False, [0, 0, 0, 0])
    print(max_d)

