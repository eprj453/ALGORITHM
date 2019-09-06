from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 1, 1, 0
maps = [list((input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
f_count = 0
# print(maps)
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
s = deque()
s.append([r,c,d])
f_count += 1
visited[r][c] = True
while len(s) > 0:
    result = False
    x, y, d2 = s[-1][0], s[-1][1], s[-1][2] # 스택 맨 뒤의 좌표, (1, 1)에서 북쪽 보고 있는 상태(0)
    for i in range(len(dx)): # 먼저 자신의 4방향중에서 청소가 가능한 곳이 있는지 체크.
        if maps[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == False:
            result = True
            break
    if result == False:  # 청소가 가능한 곳이 없다면
        if maps[x-dy[d2]][y-dx[d2]] == '1':
            break
        else:
            s.append([x-dy[d2], y-dx[d2], d2]) # 방향은 같은채로 후진
            s.popleft()
            
    for i in range(len(dx)):
        if maps[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == False: # 왼쪽이 0이면서 아직 방문 전일때
            s.append([x+dx[i], y+dy[i], (d2+1)%4])
            s.popleft()
            visited[x + dx[i]][y + dy[i]] = True
            f_count += 1
            result = True
            break

        elif maps[x+dx[i]][y+dy[i]] != 0 or visited[x+dx[i]][y+dy[i]] == True: # 왼쪽이 0이 아니거나 이미 방문했을때(왼쪽에 청소할 공간이 없을때)
            s.append([x, y, (d2+3)%4]) # 현재 위치에서 왼쪽으로 회전만 시킨 뒤 break
            s.pop()
            result = True
            break

    # if result == False: # 4방향 모두



'''
     0
  3     1
     2

'''


    # while True:
    #     if maps[x+dx[d2]][y+dy[d2]] == '0' and visited[x+dx[d2]][y+dy[d2]] == False: # 왼쪽이 0이고 아직 청소하지 않았다면
    #         s.append([x+dx[d2], y+dy[d2], (d2+1)%4]) # 청소할 곳을 서쪽을 보는 상태로 stack에 append
    #         visited[x+dx[d2]][y+dy[d2]] = True
    #         f_count += 1
    #         break
    #     elif visited[x+dx[d2]][y+dy[d2]] == True:
    #         s.pop()
    #         s.append([x, y, (d2+1)%4])
    #         break
    #     elif







'''
r, c >> 청소기 위치 [r,c]

d = 0 > 북쪽 (-1, 0)
d = 1 > 동쪽 (0, +1)
d = 2 > 남쪽 (+1, 0)
d = 3 > 서쪽 (0, -1)
'''