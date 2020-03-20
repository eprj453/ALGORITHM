import sys
sys.stdin = open('4875_input.txt', 'r')

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    maze, visited = [list(input()) for _ in range(n)], []
    for j in range(n + 2):
        if j == 0 or j == n + 1:
            maze.insert(j, (['1'] * (n + 2)))
        else:
            maze[j].insert(0, '1')
            maze[j].insert(n + 1, '1')
        visited.append([False] * (n + 2))

    q = []
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for j in range(n + 2):
        for k in range(n + 2):
            if maze[j][k] == '2':
                visited[j][k] == True
                q.append([j, k])

    ans = '0'
    while len(q) > 0:
        if ans != '0':
            break
        for c in range(len(dx)):
            if maze[q[0][0] + dx[c]][q[0][1] + dy[c]] == '3':
                ans = '1'
                break
            if visited[q[0][0] + dx[c]][q[0][1] + dy[c]] == False and maze[q[0][0] + dx[c]][q[0][1] + dy[c]] == '0':
                visited[q[0][0] + dx[c]][q[0][1] + dy[c]] = True
                q.append([q[0][0] + dx[c], q[0][1] + dy[c]])
        q.pop(0)

    print('#{} {}'.format(i, ans))