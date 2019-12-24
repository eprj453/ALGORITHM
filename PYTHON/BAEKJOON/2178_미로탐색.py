n, m = map(int,input().split())
maze = []
q = [[1,1,1]]
visited = []
dx, dy = [-1, 1, 0, 0], \
         [0 , 0, -1, 1]

for i in range(n):
    maze.append(list(input()))

for i in range(n+2):
    visited.append([False] * (m+2))

for i in range(n+2):
    if i == 0 or i == n+1:
        maze.insert(i, ['0']*(m+2))
    else:
        maze[i].insert(0,'0')
        maze[i].insert(m+2, '0')

count = 0
while len(q) > 0:
    if count != 0:
        break
    for check in q:
        if count != 0:
            break
        if visited[check[0]][check[1]] == False:
            for num in range(len(dx)):
                if maze[check[0] + dx[num]][check[1]+ dy[num]] == '1' and visited[check[0] + dx[num]][check[1]+ dy[num]] == False:
                    q.append([check[0] + dx[num], check[1]+ dy[num], check[2]+1])
                    if q[-1][0] == n and q[-1][1] == m:
                        count = q[-1][2]
                        break
            visited[check[0]][check[1]] = True
            q.pop(0)
            break

print(count)