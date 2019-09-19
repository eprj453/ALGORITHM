def robot(x, y, count, percent):
    global per

    if visited[x][y] == True:
        per += percent
        return

    if count == n:
        return

    if east:
        visited[x][y] = True
        robot(x, y+1, count+1, percent*east)
        visited[x][y] = False
    if west:
        visited[x][y] = True
        robot(x, y-1, count+1, percent*west)
        visited[x][y] = False
    if south:
        visited[x][y] = True
        robot(x+1, y, count+1, percent*south)
        visited[x][y] = False
    if north:
        visited[x][y] = True
        robot(x-1, y, count+1, percent*north)
        visited[x][y] = False


    # for i in range(len(dx)):
    #     if dx[i] == 0 and dy[i] == 1:
    #         if east == 0:
    #             continue
    #         elif visited[x][y+1] == True:
    #             per += percent
    #             return
    #         else:
    #             visited[x][y] = True
    #             robot(x, y+1, count+1, percent * east, visited)
    #
    #     elif dx[i] == 0 and dy[i] == -1:
    #         if west == 0:
    #             continue
    #         elif visited[x][y-1] == True:
    #             per += percent
    #             return
    #         else:
    #             visited[x][y] = True
    #             robot(x, y-1, count+1, percent * west, visited)
    #
    #     elif dx[i] == 1 and dy[i] == 0:
    #         if south == 0:
    #             continue
    #         elif visited[x+1][y] == True:
    #             per += percent
    #             return
    #         else:
    #             visited[x][y] = True
    #             robot(x+1, y, count+1, percent * south, visited)
    #
    #
    #     elif dx[i] == -1 and dy[i] == 0:
    #
    #         if north == 0:
    #
    #             continue
    #
    #         elif visited[x -1][y] == True:
    #
    #             per += percent
    #
    #             return
    #
    #         else:
    #
    #             visited[x][y] = True
    #
    #             robot(x -1, y, count + 1, percent * north, visited)

    # for i in range(len(dx)):
    #     if dx[i] == 0 and dy[i] == 1 and east != 0:
    #         visited[x][y] = True
    #         robot(x, y+1, count+1, percent * east)
    #
    #     elif dx[i] == 0 and dy[i] == -1 and west != 0:
    #         visited[x][y] = True
    #         robot(x, y-1, count+1, percent * west)
    #
    #     elif dx[i] == 1 and dy[i] == 0 and south != 0:
    #         visited[x][y] = True
    #         robot(x+1, y, count+1, percent * south)
    #
    #     elif dx[i] == -1 and dy[i] == 0 and north != 0:
    #         visited[x][y] = True
    #         robot(x-1 , y, count+1, percent * north)



n, east, west, south, north = map(int, input().split())
east /= 100
west /= 100
south /= 100
north /= 100
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = []
for i in range(30):
    temp = [False] * 30
    visited.append(temp)
count = 0
per = 0
robot(14, 14, 0, 1)
print('%0.10f'%(1-per))

'''
10
1
25 25 25 25
2
25 25 25 25
7
50 0 0 50
14
50 50 0 0
14
25 25 25 25
6
0 46 16 38
1
10 36 35 19
14
36 30 21 13
3
25 19 20 36
14
35 15 37 13

'''

'''
#1 1.0000000000
#2 0.7500000000
#3 1.0000000000
#4 0.0001220703
#5 0.0088454932
#6 0.5705340928
#7 1.0000000000
#8 0.0089999035
#9 0.5832200000
#10 0.0506629797

'''