def cheese_melt(cheese, maps):
    ans = cheese
    ans_time = 0
    last_cheese = 0
    while True:
        last_cheese = ans
        visited = [[False] * m for _ in range(n)]
        melt_cheeses = set()
        for k in range(n):
            for l in range(m):
                if maps[k][l] == 0:
                    q = [[k, l]]
                    while q:
                        x, y = q[0][0], q[0][1]
                        result = False
                        for a in range(len(dx)):
                            if 0 <= x + dx[a] < n and 0 <= y + dy[a] < m:
                                if maps[x+dx[a]][y+dy[a]] == 1 and visited[x+dx[a]][y+dy[a]] == False:
                                    visited[x + dx[a]][y + dy[a]] = True
                                    melt_cheeses.add((x+dx[a], y+dy[a]))
                                else:
                                    if maps[x+dx[a]][y+dy[a]] == 0 and visited[x+dx[a]][y+dy[a]] == False:
                                        visited[x+dx[a]][y+dy[a]] = True
                                        q.append([x+dx[a], y+dy[a]])
                        q.pop(0)
                    for x, y in list(melt_cheeses):
                        if maps[x][y] == 1:
                            maps[x][y] = 0
                            ans -= 1
                    break

        ans_time += 1

        if ans == 0:
            break

    return ans_time, last_cheese



n, m = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
maps = []
cheeses, time, ans = 0, 0, 0
for _ in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
           cheeses += 1
    maps.append(temp)

ans_time, last_cheese = cheese_melt(cheeses, maps)
print(ans_time)
print(last_cheese)
    # for i in range(n):
    #     for j in range(m):
    #         for k in range(len(dx)):
    #             if 0 <= i + dx[k] < n and 0 <= j + dy[k] < m:
    #                 if maps[i+dx[k]][j+dy[k]] == 0:
    #                     checked[i+dx[k]][j+dy[k]] = True