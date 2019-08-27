n, m = map(int,input().split())
maze = []
q = [[1,1,1]] # 1,1 에서 0번째 탐색
visited = []
# x, y = [-1, 1], [-1, 1]
dx, dy = [-1, 1, 0, 0], \
         [0 , 0, -1, 1]

'''
4 6
101111
101010
101011
111011

'''

for i in range(n): # 미로 리스트
    maze.append(list(input()))

for i in range(n+2):
    visited.append([False] * (m+2))
# visited[0][0] = True

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
    # print('q', q)
    for check in q:
        if count != 0:
            break
        # print('check', check)
        if visited[check[0]][check[1]] == False: # check : 좌표
            for num in range(len(dx)):
                # print('check, ', [check[0] + dx[num]], [check[1]+ dy[num]])
                if maze[check[0] + dx[num]][check[1]+ dy[num]] == '1' and visited[check[0] + dx[num]][check[1]+ dy[num]] == False:
                    # 미로가 1이고 아직 방문한적이 없다면
                    q.append([check[0] + dx[num], check[1]+ dy[num], check[2]+1])
                    # print('append, ', [check[0] + dx[num]], [check[1] + dy[num]])
                    if q[-1][0] == n and q[-1][1] == m:
                        count = q[-1][2]
                        break
            visited[check[0]][check[1]] = True
            # print('pop, ',q[0])
            q.pop(0)
            break

print(count)
            # if visited[check[0]+1][check[1]] == False:
            #     q.append([check[0]+1, check[1], check[2]+1])
            # if visited[check[0]-1][check[1]] == False:
            #     q.append([check[0]-1, check[1], check[2]+1])
            # if visited[check[0]][check[1]+1] == False:
            #     q.append([check[0], check[1]+1, check[2]+1])
            # if visited[check[0]][check[1]-1] == False:
            #     q.append([check[0], check[1]-1, check[2]+1])


        # if visited[maze[q[0][0]][maze[q[0][1]]] == False: # 1, 1
        #     if visited[maze[q[0][0]][maze[q[0][1]]+1]: # 1, 2 오른쪽
        #     if visited[maze[q[0][0]][maze[q[0][1]]-1]: # 1, 0 왼쪽
        #     if visited[maze[q[0][0]][maze[q[0][1]]+1]: #
        #     if visited[maze[q[0][0]][maze[q[0][1]]+ 1]:
print(maze)
print(visited)

# while len(q) > 0:
