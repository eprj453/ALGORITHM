def BFS(x, y, c, length):
    if x == n-1 and y == m-1:
        return length
    print(x, y)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # for i in range(len(dx)):
    if 0 <= x+dx[0] < n and 0 <= y+dy[0] < m and maps[x+dx[0]][y+dy[0]] == '1' and c == 1 and visited[x+dx[0]][y+dy[0]] == False:
        visited[x + dx[0]][y + dy[0]] == True
        BFS(x + dx[0], y + dy[0], c - 1, length + 1)
    if 0 <= x+dx[0] < n and 0 <= y+dy[0] < m and maps[x+dx[0]][y+dy[0]] == '0':
        BFS(x + dx[0], y + dy[0], c, length + 1)

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


n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = []
for i in range(n):
    visited.append([False] * m)
print(BFS(0, 0, 1, 1))