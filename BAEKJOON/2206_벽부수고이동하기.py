def BFS(x, y, c, length):
    if x == n-1 and y == m-1:
        return length

    for i in range(len(dx)):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
            if maps[x+dx[i]][y+dy[i]] == '1' and c == 1:
                BFS(x + dx[i], y + dy[i], c - 1, length + 1)
            elif maps[x+dx[i]][y+dy[i]] == '1' and c == 0:
                return -1
            elif maps[x+dx[i]][y+dy[i]] == '0':
                # result = True
                BFS(x+dx[i], y+dy[i], c, length+1)





n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
print(BFS(0, 0, 1, 1))