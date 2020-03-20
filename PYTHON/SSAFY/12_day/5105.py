import sys
sys.stdin = open('5105_input.txt', 'r')


t = int(input())
for i in range(1, t+1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    start, end, q = [], [], []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for j in range(n):
        for k in range(n):
            if maze[j][k] == '2':
                start = [j, k]
            if maze[j][k] == '3':
                end = [j, k]

    q.append(start)
    visited[start[0]][start[1]] = 0

    ans = 0
    while len(q) > 0:
        if ans != 0 : break
        for j in range(len(dx)):
            # print(q[0][0] + dx[j], q[0][1] + dy[j])
            if q[0][0] + dx[j] >= 0 and q[0][1] + dy[j] >= 0 and q[0][0] + dx[j] < n and q[0][1] + dy[j] < n:
                if maze[q[0][0] + dx[j]][q[0][1] + dy[j]] == '0' and visited[q[0][0] + dx[j]][q[0][1] + dy[j]] == 0:
                    q.append([q[0][0] + dx[j], q[0][1] + dy[j]])
                    visited[q[0][0] + dx[j]][q[0][1]+dy[j]] = visited[q[0][0]][q[0][1]] + 1
            if q[0][0] + dx[j] == end[0] and q[0][1] + dy[j] == end[1]:
                ans = visited[q[0][0]][q[0][1]]
                break
        q.pop(0)

    print('#{} {}'.format(i, ans))
