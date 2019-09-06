from collections import deque
n, l, r = map(int, input().split())
countrys = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# print(countrys)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
c_list = []
c_count = 0
while True:
    result = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                q.append([i,j])
                c_list.append([i,j])
                p_sum = countrys[i][j]
                p_count = 1
                visited[i][j] = True
                while len(q) > 0:
                    x, y = q[0][0], q[0][1]
                    for k in range(len(dx)):
                        if x + dx[k] >= 0 and y + dy[k] >= 0 and \
                                x + dx[k] < n and y + dy[k] < n:
                            if visited[x + dx[k]][y + dy[k]] == False and \
                                l <= abs(countrys[x][y] - countrys[x + dx[k]][y + dy[k]]) <= r:
                                result = True
                                q.append([x+dx[k], y+dy[k]])
                                c_list.append([x+dx[k], y+dy[k]])
                                visited[x+dx[k]][y+dy[k]] = True
                                p_sum += countrys[x+dx[k]][y+dy[k]]
                                p_count += 1
                    q.popleft()
                if len(c_list) > 1:
                    for x in c_list:
                        countrys[x[0]][x[1]] = p_sum // p_count
                    c_count += 1
                    c_list = []
                else:
                    c_list = []
    for x in range(n):
        for y in range(n):
            visited[x][y] = False

    if result != True:
        break

print(countrys)
print(c_count)






