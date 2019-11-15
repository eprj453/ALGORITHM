import sys
sys.stdin = open('2105_input.txt', 'r')

def find(x, y, path, is_back, d1, d2, d3, d4):
    global max_d
    if x == j and y == k and is_back == True and d1 and d2 and d3 and d4:
        max_d = max(path, max_d)
        return



    if d1 == 0:
        if 0 <= x + 1 < n and 0 <= y - 1 < n:
            f_des = maps[x+1][y-1]
            if d_visited[f_des] == False:
            #     d_visited[f_des] = True
            #     w_visited[x+1][y-1] = True
                find(x+1, y-1, path+1, False, d1+1, d2, d3, d4)

    if d1 != 0 and d2 == 0:
        for d in range(0, 2):
            d_x, d_y = dx[d], dy[d]
            if 0 <= x + d_x < n and 0 <= y + d_y < n:
                f_des = maps[x+d_x][y+d_y]
                if d_visited[f_des] == False:
                    # d_visited[f_des] = True
                    # w_visited[x + d_x][y + d_y] = True
                    if d == 0:
                        find(x+d_x, y+d_y, path+1, False, d1+1, d2, d3, d4)
                    else:
                        find(x + d_x, y + d_y, path + 1, False, d1, d2+1, d3, d4)
                    # d_visited[f_des] = False
                    # w_visited[x + d_x][y + d_y] = False

    if d2 != 0 and d3 == 0:
        for d in range(1, 3):
            d_x, d_y = dx[d], dy[d]
            if 0 <= x + d_x < n and 0 <= y + d_y < n:
                f_des = maps[x+d_x][y+d_y]
                if d_visited[f_des] == False:
                    # d_visited[f_des] = True
                    # w_visited[x + d_x][y + d_y] = True
                    if d == 1:
                        find(x + d_x, y + d_y, path + 1, False, d1, d2+1, d3, d4)
                    else:
                        find(x + d_x, y + d_y, path + 1, False, d1, d2, d3+1, d4)
                    # d_visited[f_des] = False
                    # w_visited[x + d_x][y + d_y] = False

    if d3:
        if d3 < d1:
            d_x, d_y = -1, 1
            if 0 <= x + d_x < n and 0 <= y + d_y < n:
                f_des = maps[x + d_x][y + d_y]
                if d_visited[f_des] == False:
                    # d_visited[f_des] = True
                    # w_visited[x + d_x][y + d_y] = True
                    find(x + d_x, y + d_y, path + 1, False, d1, d2, d3+1, d4)
                    # d_visited[f_des] = False
                    # w_visited[x + d_x][y + d_y] = False

        elif d3 == d1:
            d_x, d_y = -1, -1
            if x + d_x == j and y + d_y == k:
                find(x+d_x, y+d_y, path + 1, True, d1, d2, d3, d4+1)
            else:
                if 0 <= x + d_x < n and 0 <= y + d_y < n:
                    f_des = maps[x + d_x][y + d_y]
                    if d_visited[f_des] == False:
                        # d_visited[f_des] = True
                        # w_visited[x + d_x][y + d_y] = True
                        find(x + d_x, y + d_y, path + 1, False, d1, d2, d3, d4+1)
                        # d_visited[f_des] = False
                        # w_visited[x + d_x][y + d_y] = False

    # if my_dir != 0 and
    # start = 0
    # for i in range(4, 0, -1):
    #     # print(can_go)
    #     if can_go[i-1] != 0:
    #         start = i
    #         break
    #
    # d_list = [d1, d2, d3, d4]
    # if d1 == 0:
    #     for d in range(0, 2):
    #         d_x, d_y = dx[d], dy[d]
    #         if 0 <= x + d_x < n and 0 <= y + d_y < n:
    #             f_des = maps[x + d_x][y + d_y]
    #             if d_visited[f_des] == False and w_visited[x+d_x][y+d_y] == False:
    #                 d_visited[f_des] = True
    #                 w_visited[x+d_x][y+d_y] = True
    #                 if d == 0:
    #                     find(x+d_x, y+d_y, path+1, False, d1+1, d2, d3, d4)
    #                 else:
    #                     find(x + d_x, y + d_y, path + 1, False, d1, d2+1, d3, d4)
    #                 d_visited[f_des] = False
    #                 w_visited[x + d_x][y + d_y] = False
    #
    #
    # if d2:
    #     for d in range(1, 3):
    #         d_x, d_y = dx[d], dy[d]
    #         if 0 <= x + d_x < n and 0 <= y + d_y < n:
    #             f_des = maps[x + d_x][y + d_y]
    #             if d_visited[f_des] == False and w_visited[x + d_x][y + d_y] == False:
    #                 d_visited[f_des] = True
    #                 w_visited[x + d_x][y + d_y] = True
    #                 if d == 1:
    #                     find(x + d_x, y + d_y, path + 1, False, d1, d2+1, d3, d4)
    #                 if d == 2 and d3 < d1:
    #                     find(x + d_x, y + d_y, path + 1, False, d1, d2, d3+1, d4)
    #                 d_visited[f_des] = False
    #                 w_visited[x + d_x][y + d_y] = False
    #
    # if d3:
    #     for d in range()



    # if d3:
    #     for d in range(2, 4):
    #         d_x, d_y = dx[d], dy[d]
    #         if 0 <= x + d_x < n and 0 <= y + d_y < n:
    #             f_des = maps[x + d_x][y + d_y]
    #             if d == 3 and x+d_x == j and y+d_y == k:
    #                 find(x+d_x, y+d_y, path+1, True, d1, d2, d3, d4+1)
    #             if d_visited[f_des] == False and w_visited[x + d_x][y + d_y] == False:
    #                 d_visited[f_des] = True
    #                 w_visited[x + d_x][y + d_y] = True
    #                 if d == 2 and d3 < d1:
    #                     find(x + d_x, y + d_y, path + 1, False, d1, d2, d3+1, d4)
    #                 if d == 3 and d3 == d1:
    #                     find(x + d_x, y + d_y, path + 1, False, d1, d2, d3, d4+1)
    #                 d_visited[f_des] = False
    #                 w_visited[x + d_x][y + d_y] = False


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
                find(j, k, 0, False, 0, 0, 0, 0)
    max_d = -1 if max_d == 0 else max_d
    print('#{} {}'.format(a, max_d))

