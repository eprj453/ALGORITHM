def BFS(c, q):
    x, y = q[0][0], q[0][1]
    global min_length
    # print('x ,y : ',x ,y)
    if x == n-1 and y == m-1:
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
BFS(1, q)
print(min_length)