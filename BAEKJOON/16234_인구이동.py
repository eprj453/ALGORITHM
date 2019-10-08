from collections import deque
n, l, r = map(int, input().split())
countrys = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
while True:
    result = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                # print('find : ',i ,j)
                c_list = []
                c_sum, c_count = 0, 0
                q.append([i, j]) # 현재 좌표 큐에 추가
                c_list.append([i,j]) # 연결된 모든 노드 저장
                c_sum += countrys[i][j]
                c_count += 1
                visited[i][j] = True
                while len(q) > 0:
                    x, y = q[0][0], q[0][1]
                    # print(q)
                    for k in range(len(dx)):
                        # print(q)
                        if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n: # 범위에 벗어나지 않을때
                            if visited[x+dx[k]][y+dy[k]] == False and l <= abs(countrys[x][y] - countrys[x+dx[k]][y+dy[k]]) <= r:
                                    # print(x + dx[k], y + dy[k])
                                    result = True
                                    q.append([x+dx[k], y+dy[k]]) # 큐에 추가
                                    visited[x+dx[k]][y+dy[k]] = True  # 방문 표시
                                    c_list.append([x+dx[k], y+dy[k]])
                                    c_count += 1
                                    c_sum += countrys[x+dx[k]][y+dy[k]]
                    q.popleft()

                if len(c_list) > 1:
                    # for x in range(n):
                    #     for y in range(n):
                    #         print(countrys[x][y], end = ' ')
                    #     print()
                    #
                    # for x in range(n):
                    #     for y in range(n):
                    #         print(visited[x][y], end = ' ')
                    #     print()
                    for c in c_list:
                        countrys[c[0]][c[1]] = c_sum//c_count
                    # print(c_list)
                    # print(c_sum, c_count)
                    # print(c_sum // c_count)
                    # print('------------------------인구 이동-----------------------------')
                    # for x in range(n):
                    #     for y in range(n):
                    #         print(countrys[x][y], end=' ')
                    #     print()


    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # print('=====================result : {}====================='.format(result))
    if result == False:
        break
    else:
        ans += 1
print(ans)

