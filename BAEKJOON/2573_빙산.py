n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
melt = [[0] * (m-2) for _ in range(n-2)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0
count = 0
while True:

    if result:
        break

    z_count = 0

    for i in range(1, n-1):
        for j in range(1, m-1):
            for k in range(len(dx)):
                if ice[i+dx[k]][j+dy[k]] == 0 and ice[i][j] != 0:
                    melt[i-1][j-1] += 1

    for i in range(1, n-1):
        for j in range(1, m-1):
            ice[i][j] -= melt[i-1][j-1]
            if ice[i][j] < 0:
                ice[i][j] = 0

    count += 1

    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice[i][j] == 0:
                z_count += 1

    if (n-2) * (m-2) == z_count:
        result = '0'

    for i in range(1, n-1):
        if result:
            break
        for j in range(1, m-1):
            if ice[i+dx[0]][j+dy[0]] == 0 and ice[i+dx[1]][j+dy[1]] == 0 and ice[i+dx[2]][j+dy[2]] == 0 and ice[i+dx[3]][j+dy[3]] == 0:
                result = count
                break
            if ice[i][j] == 0:
                z_count += 1


print(result)
