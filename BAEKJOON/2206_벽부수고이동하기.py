def BFS(c, q):
    x, y = q[0][0], q[0][1]
    global min_length
    # print('x ,y : ',x ,y)
    if x == n-1 and y == m-1:
<<<<<<< HEAD
        print('도착')
        min_length = min(min_length, q[0][2])
        # return
    if x > n-1 or y > m-1:
        min_length = -1
        return
    for i in range(len(dx)):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
            # print(dx[i], dy[i])
            if maps[x+dx[i]][y+dy[i]] == '1' and c == 1 and visited[x+dx[i]][y+dy[i]] == False:
                visited[x + dx[i]][y + dy[i]] = True
                q.append([x+dx[i], y+dy[i], q[0][2]+1])
                print('간다. : ', x+dx[i], y+dy[i])
                q.pop(0)
                BFS(c - 1, q)
                print(x, y)
                print()
            elif maps[x+dx[i]][y+dy[i]] == '0' and visited[x+dx[i]][y+dy[i]] == False:
                visited[x + dx[i]][y + dy[i]] = True
                q.append([x + dx[i], y + dy[i], q[0][2] + 1])
                print('간다. : ', x + dx[i], y + dy[i])
                q.pop(0)
                BFS(c, q)
                print(x, y)
                print()
=======
        return length
<<<<<<< HEAD
    print(x, y)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # for i in range(len(dx)):
    if 0 <= x+dx[0] < n and 0 <= y+dy[0] < m and maps[x+dx[0]][y+dy[0]] == '1' and c == 1 and visited[x+dx[0]][y+dy[0]] == False:
        visited[x + dx[0]][y + dy[0]] == True
        BFS(x + dx[0], y + dy[0], c - 1, length + 1)
    if 0 <= x+dx[0] < n and 0 <= y+dy[0] < m and maps[x+dx[0]][y+dy[0]] == '0':
        BFS(x + dx[0], y + dy[0], c, length + 1)
=======

    for i in range(len(dx)):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
            if maps[x+dx[i]][y+dy[i]] == '1' and c == 1:
                BFS(x + dx[i], y + dy[i], c - 1, length + 1)
            elif maps[x+dx[i]][y+dy[i]] == '1' and c == 0:
                return -1
            elif maps[x+dx[i]][y+dy[i]] == '0':
                # result = True
                BFS(x+dx[i], y+dy[i], c, length+1)
>>>>>>> 813cf371b0e0eb7d9d7a3a5b093105a6e52b7511

    if 0 <= x + dx[1] < n and 0 <= y + dy[1] < m and maps[x + dx[1]][y + dy[1]] == '1' and c == 1:
        BFS(x + dx[1], y + dy[1], c - 1, length + 1)
    if 0 <= x + dx[1] < n and 0 <= y + dy[1] < m and maps[x + dx[1]][y + dy[1]] == '0':
        BFS(x + dx[1], y + dy[1], c, length + 1)

    if 0 <= x + dx[2] < n and 0 <= y + dy[2] < m and maps[x + dx[2]][y + dy[2]] == '1' and c == 1:
        BFS(x + dx[2], y + dy[2], c - 1, length + 1)
    if 0 <= x + dx[2] < n and 0 <= 2 + dy[2] < m and maps[x + dx[2]][y + dy[2]] == '0':
        BFS(x + dx[2], y + dy[2], c, length + 1)

    if 0 <= x + dx[3] < n and 0 <= y + dy[3] < m and maps[x + dx[3]][y + dy[3]] == '1' and c == 1:
        BFS(x + dx[3], y + dy[3], c - 1, length + 1)
    if 0 <= x + dx[3] < n and 0 <= y + dy[3] < m and maps[x + dx[3]][y + dy[3]] == '0':
        BFS(x + dx[3], y + dy[3], c, length + 1)
        # elif maps[x+dx[i]][y+dy[i]] == '1' and c == 0:
        #     return -1
        # elif maps[x+dx[i]][y+dy[i]] == '0':
        #     # result = True
        #     BFS(x+dx[i], y+dy[i], c, length+1)


    return -1


>>>>>>> 2d8f9494f57c801305c7d70bb23f88cc38a97567
n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visited = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(False)
    visited.append(temp)
visited[0][0] = True
q = [[0, 0, 0]]
min_length = 1000000
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
<<<<<<< HEAD
BFS(1, q)
print(min_length)
=======
visited = []
for i in range(n):
    visited.append([False] * m)
print(BFS(0, 0, 1, 1))
>>>>>>> 2d8f9494f57c801305c7d70bb23f88cc38a97567
