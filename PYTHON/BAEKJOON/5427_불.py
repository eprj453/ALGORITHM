import sys
sys.stdin = open('5427_input.txt', 'r')

# for i in range(1, int(input())+1):
# #     w, h = map(int, input().split())
# #     start_x, start_y = 0, 0
# #     maps = []
# #     fires = []
# #     visited = []
# #     q = []
# #     dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# #     c = 0
# #     while c < h:
# #         temp = list(input())
# #         temp2 = [False] * w
# #         maps.append(temp)
# #         visited.append(temp2)
# #         for j in range(len(temp)):
# #             if temp[j] == '@':
# #                 start_x, start_y = c, j
# #                 visited[start_x][start_y] = True
# #             if temp[j] == '*':
# #                 q.append([c, j, 1, 0])
# #                 visited[c][j] = True
# #         c += 1
# #     q.append([start_x, start_y, 0, 0])
# #     min_distance = 0
# #     # 0 > 나, 1 > 불
# #     while q:
# #         x, y, which, count = q[0][0], q[0][1], q[0][2], q[0][3]
# #         if (x == 0 or y == 0 or x == h-1 or y == w-1) and which == 0:
# #             min_distance = count
# #             break
# #
# #         if which == 1:
# #             for k in range(len(dx)):
# #                 if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
# #                     if maps[x+dx[k]][y+dy[k]] == '.' and visited[x+dx[k]][y+dy[k]] == False:
# #                         q.append([x+dx[k], y+dy[k], which, count+1])
# #                         visited[x+dx[k]][y+dy[k]] = True
# #
# #             q.pop(0)
# #
# #
# #         elif which == 0:
# #             for k in range(len(dx)):
# #                 if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
# #                     if (x == 0 or y == 0 or x == h or y == w) and which == 0:
# #                         min_distance = count
# #                         break
# #                     if maps[x+dx[k]][y+dy[k]] != '#' and visited[x+dx[k]][y+dy[k]] == False:
# #                         q.append([x+dx[k], y+dy[k], which, count+1])
# #                         visited[x+dx[k]][y+dy[k]] = True
# #             q.pop(0)
# #
# #         if min_distance:
# #             break
# #     if min_distance == 0:
# #         print('IMPOSSIBLE')
# #     else:
# #         print(min_distance+1)

# def fire_spread(my_q, fire_q):
#     global distance
#     # print('my_q : ', my_q)
#     if len(my_q) == 0:
#         return
#
#     my_new_q = []
#     fire_new_q = []
#     if fire_q:
#         for i in range(len(fire_q)):
#             x, y = fire_q[i][0], fire_q[i][1]
#             print(x, y)
#             for k in range(len(dx)):
#                 if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
#                     if maps[x+dx[k]][y+dy[k]] != '#' and maps[x+dx[k]][y+dy[k]] != '*' and fire_visited[x+dx[k]][y+dy[k]] == False:
#                         fire_visited[x+dx[k]][y+dy[k]] = True
#                         maps[x+dx[k]][y+dy[k]] = '*'
#                         fire_new_q.append([x+dx[k], y+dy[k]])
#     # print('fire_new_q : ', fire_new_q)
#     if my_q:
#         for i in range(len(my_q)):
#
#             x, y, z  = my_q[i][0], my_q[i][1], my_q[i][2]
#             # print(x, y, z)
#             # if x == 0 or y == 0 or x == h-1 or y == w-1:
#             #     distance = min(distance, z+1)
#             #     return
#             for k in range(len(dx)):
#                 if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
#                     if maps[x+dx[k]][y+dy[k]] == '.' and fire_visited[x+dx[k]][y+dy[k]] == False and my_visited[x+dx[k]][y+dy[k]] == False:
#                         if (x+dx[k] == 0 or y+dy[k] == 0 or x+dx[k] == h-1 or y+dy[k] == w-1) and maps[x+dx[k]][y+dy[k]] == '.':
#                             distance = min(distance, z+2)
#                             return
#                         my_visited[x+dx[k]][y+dy[k]] = True
#                         maps[x+dx[k]][y+dy[k]] = '@'
#                         my_new_q.append([x+dx[k], y+dy[k], z+1])
#
#     # for i in range(h):
#     #     print(maps[i])
#     # print()
#
#
#     fire_spread(my_new_q, fire_new_q)
#
#
#
# dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]
# for l in range(int(input())):
#     w, h = map(int, input().split())
#     me, fire, maps, fire_visited, my_visited = [], [], [], [], []
#     for j in range(h):
#         temp = list(input())
#         f_temp, m_temp = [False] * w, [False] * w
#         fire_visited.append(f_temp)
#         my_visited.append(m_temp)
#         for k in range(w):
#             if temp[k] == '@':
#                 me = [[j, k, 0]]
#                 my_visited[j][k] = True
#             elif temp[k] == '*':
#                 fire.append([j, k])
#                 fire_visited[j][k] = True
#         maps.append(temp)
#     distance = 1000000
#     fire_spread(me, fire)
#     if distance == 1000000:
#         print('IMPOSSIBLE')
#     else:
#         print(distance)


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(int(input())):
    w, h = map(int, input().split())
    fires, me = [], []
    visited = []
    maps = []
    min_d = 1000 * 1000
    for _ in range(h):
        temp = [False] * w
        visited.append(temp)

    for i in range(h):
        temp = list(input())
        for j in range(len(temp)):
            if temp[j] == '*':
                fires.append([i, j])
                visited[i][j] = True
            elif temp[j] == '@':
                me.append([i, j, 0])
        maps.append(temp)


    while me:

        x, y, z = me[0][0], me[0][1], me[0][2]

        if fires:
            new_fire = []
            for fire in fires:
                x, y = fire[0], fire[1]
                for k in range(len(dx)):
                    if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w:
                        if visited[x+dx[k]][y+dy[k]] == False and maps[x+dx[k]][y+dy[k]] != '#':
                            maps[x+dx[k]][y+dy[k]] = '*'
                            visited[x+dx[k]][y+dy[k]] = True
                            new_fire.append([x+dx[k], y+dy[k]])
            fires = new_fire

        for m in me:
            if x == 0 or y == 0 or x == h - 1 or y == w - 1:
                min_d = min(min_d, z + 1)


        new_me = []
        # print(me)
        for m in me:
            # print(m)
            x, y, z = m[0], m[1], m[2]
            for k in range(len(dx)):
                if 0 <= x + dx[k] < h and 0 <= y + dy[k] < w:
                    if maps[x + dx[k]][y + dy[k]] == '.':
                        maps[x+dx[k]][y+dy[k]] = '@'
                        new_me.append([x+dx[k], y+dy[k], z+1])


        me = new_me
        #
        # for i in range(h):
        #     print(maps[i])
        #
        # print()
    min_d = 'IMPOSSIBLE' if min_d == 1000*1000 else min_d
    print(min_d)







'''

21
1 1
@
3 3
.#.
#@#
.#.
3 3
...
.@.
...
3 3
.#.
#@#
.#*
8 3
########
#*@.....
########
5 6
##.##
#...#
#.#.#
#.#@#
#*#.#
#####
5 6
##.##
#...#
#.#.#
#*#@#
#.#.#
#####
5 6
##.##
#...#
#*#.#
#.#@#
#.#.#
#####
8 9
########
#......#
#.####.#
#.#@.#.#
#.##.#.#
#....#.#
######.#
.......#
########
5 3
##.##
#*.@#
#####
7 7
.......
.*#.##.
.##.##.
...@...
.##.##.
.##.#*.
.......
7 7
......*
.##.##.
.##.##.
...@...
.##.##.
.##.##.
*......
7 7
.*....*
.##.##.
.##.##.
...@...
.##.##.
.##.##.
.*....*
7 7
.......
*##.##*
.##.##.
...@...
.##.##.
.##.##.
*.....*
7 7
*....*.
.##.##.
.##.##.
...@...
.##.##.
.##.##.
*....*.
7 7
*.....*
.##.##.
.##.##.
...@...
.##.##.
*##.##*
.......
7 7
..#.#..
.*#.#*.
.##.##.
...@...
.##.##.
.*#.#*.
.......
7 7
.......
.*#.#*.
.##.###
...@...
.##.###
.*#.#*.
.......
7 7
.......
.*#.#*.
###.##.
...@...
###.##.
.*#.#*.
.......
7 7
.......
.*#.#*.
.##.##.
...@...
.##.##.
.*#.#*.
..#.#..
5 3
..#..
.@#*.
..#..
'''

'''
1
5 7
...#*
..##.
##.#.
#@...
##.#.
..##.
...#*

'''

