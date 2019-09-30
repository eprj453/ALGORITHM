def bfs(q):
    global cnt
    if len(q) == 0:
        cnt += 1
        return
    x, y = q[0][0], q[0][1]
    result = False
    for i in range(len(dx)):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
            if land[x+dx[i]][y+dy[i]] == 1 and visited[x+dx[i]][y+dy[i]] == False:
                visited[x + dx[i]][y + dy[i]] = True
                q.append([x + dx[i], y+dy[i]])
    q.pop(0)
    bfs(q)



dx, dy = [-1, 1, 0, 0], [0 ,0, -1, 1]
for i in range(1, int(input())+1):
    m, n, k = map(int, input().split())
    land = []
    visited = []
    q = []
    cnt = 0
    for j in range(n):
        v_temp = [False] * m
        temp = [0] * m
        land.append(temp)
        visited.append(v_temp)
    for j in range(k):
        x, y = map(int, input().split())
        land[y][x] = 1

    # for j in range(n):
    #     print(land[j])
    # for j in range(n):
    #     print(visited[j])
    for j in range(n):
        for k in range(m):
            if land[j][k] == 1 and visited[j][k] == False:
                visited[j][k] = True
                q.append([j, k])
                bfs(q)
    print(cnt)