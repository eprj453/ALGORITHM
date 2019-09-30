def bfs(q):
    global cnt2
    if len(q) == 0:
        cnt2 += 1
        return
    x, y = q[0][0], q[0][1]
    for i in range(len(dx)):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n:
            if maps[x+dx[i]][y+dy[i]] != 0 and visited[x+dx[i]][y+dy[i]] == False:
                q.append([x+dx[i], y+dy[i]])
                visited[x+dx[i]][y+dy[i]] = True
    q.pop(0)
    bfs(q)


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
t = 0
max_val = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt, cnt2, ans = 0, 0, 0
while t < 100:
    q = []
    visited = []
    for i in range(n):
        temp = [False] * n
        visited.append(temp)

    for i in range(n):
        for j in range(n):
            if maps[i][j] <= t: # 기준 이하 지역 전부 침수
                maps[i][j] = 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0 and visited[i][j] == False:
                q.append([i, j])
                visited[i][j] = True
                bfs(q)
    # print(cnt2)
    if cnt > cnt2: # 기존에 구했던 값이 새로 구한 값보다 크다면 : 점점 영역이 줄어든다는 의미, 영역이 더 늘어나지 않는다.
        ans = cnt
        break
    else: # 기존값이 작거나 같으면 아직 여지가 있음.
        cnt = cnt2
        cnt2 = 0

    t += 1

print(ans)



'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7


7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
'''