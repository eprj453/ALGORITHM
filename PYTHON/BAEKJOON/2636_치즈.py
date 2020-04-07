n, m = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
maps = []
cheeses, time, ans, last_cheese = 0, 0, 0, 0
for _ in range(n):
    temp = list(map(int, input().split()))
    cheeses += temp.count(1)
    maps.append(temp)

while True:
    last_cheese = cheeses
    melt_cheeses = []
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                q = [[i,j]]
                while q:
                    x, y = q[0][0], q[0][1]
                    for k in range(4):
                        kx, ky = x + dx[k], y + dy[k]
                        if 0 <= kx < n and 0 <= ky < m:
                            if maps[kx][ky] == 1 and visited[kx][ky] == False:
                                visited[kx][ky] = True
                                melt_cheeses.append((kx, ky))
                            else:
                                if maps[kx][ky] == 0 and visited[kx][ky] == False:
                                    visited[kx][ky] = True
                                    q.append([kx, ky])
                    q.pop(0)

                for x, y in melt_cheeses:
                    if maps[x][y] == 1:
                        maps[x][y] = 0
                        cheeses -= 1
                break

    time += 1

    if cheeses == 0:
        break

print(time)
print(last_cheese)


