from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 1, 1, 0
maps = [list((input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
f_count = 0
# print(maps)
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0] # 가리키는 방향을 기준으로 왼쪽을 가리키도록 반시계 방향으로 벡터 설정
dx2, dy2 = [1, 0, -1, 0],[0, -1, 0, 1] # 가리키는 방향을 기준으로 반대 방향을 가리키도록 벡터 설정
idx_list = [0, 3, 2, 1]
s = deque()
s.append([r,c,d])
f_count += 1
visited[r][c] = True
while len(s) > 0:
    print(s)
    x, y, d2 = s[-1][0], s[-1][1], s[-1][2] # 스택 맨 끝 좌표와 현재 방향
    result = False
    result2 = False
    # if visited[x+dx[(d2+i)%3]][y+dy[(d2+i)%3]] == False and maps[x+dx[d2]][y+dy[d2]] == '1':
    for i in range(len(dx)):
        x, y, d2 = s[-1][0], s[-1][1], s[-1][2]
        print('s-1', s[-1])
        # 왼쪽 먼저 본 뒤 갈 수 있으면 break, 왼쪽으로 못가면 4방향 전부 순회, 이 반복문이 다 돌았는데도 break를 못한다면 4방향 전부 갈수 없는 상태
        # (d2) % 3은 본인이 갖고 있는 좌표를 시작으로 왼쪽을 제일 먼저 본 뒤 동서남북을 순회함.
        if visited[x+dx[(d2-i)%4]][y+dy[(d2-i)%4]] == False and maps[x+dx[(d2-i)%4]][y+dy[(d2-i)%4]] == '0': # 왼쪽으로 갈 수 있고 벽이 아니면서 청소하지 않았다면
            print(x+dx[(d2-i)%4], y+dy[(d2-i)%4])
            print(x + dx[(d2 + 3) % 4], y + dy[(d2 + 3) % 4])
            idx = idx_list.index(d2)
            s.append([x+dx[(d2-i)%4], y+dy[(d2-i)%4], idx_list[(idx-i+1)%4]]) # 좌표 옮기기
            print('s.append : ',x+dx[(d2+i)%3], y+dy[(d2+i)%3], idx_list[idx-i] % 4)
            print('visited : ', x+dx[(d2-i)%4], y+dy[(d2-i)%4])
            visited[x+dx[(d2-i)%4]][y+dy[(d2-i)%4]] = True  # 방문표시
            result = True
            result2 = True
            f_count += 1
            break

    if result == False: # 만약 갈 수 있는 곳이 없다면 본인이 갖고 있는 방향을 기준으로 뒤로(반대방향으로) 1칸
        if maps[x + dx2[d2]][y + dy2[d2]] != '1':  # 가리키고 있는 반대 방향이 1이라면
            result2 = True
            temp = s.pop()  # 기존 좌표 out
            s.append([temp[0]+dx2[d2], temp[1]+dy2[d2], temp[2]]) # 방향을 그대로 유지한채로 1칸 후진한 좌표를 s에 append

    if result2 == False:
        break

print(f_count)

    # result = False
    # x, y, d2 = s[-1][0], s[-1][1], s[-1][2] # 스택 맨 뒤의 좌표, (1, 1)에서 북쪽 보고 있는 상태(0)
    # for i in range(len(dx)): # 먼저 자신의 4방향중에서 청소가 가능한 곳이 있는지 체크.
    #     if maps[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == False:
    #         result = True
    #         break
    # if result == False:  # 청소가 가능한 곳이 없다면
    #     if maps[x-dy[d2]][y-dx[d2]] == '1':
    #         break
    #     else:
    #         s.append([x-dy[d2], y-dx[d2], d2]) # 방향은 같은채로 후진
    #         s.popleft()
    #
    # for i in range(len(dx)):
    #     if maps[x+dx[i]][y+dy[i]] == 0 and visited[x+dx[i]][y+dy[i]] == False: # 왼쪽이 0이면서 아직 방문 전일때
    #         s.append([x+dx[i], y+dy[i], (d2+1)%4])
    #         s.popleft()
    #         visited[x + dx[i]][y + dy[i]] = True
    #         f_count += 1
    #         result = True
    #         break
    #
    #     elif maps[x+dx[i]][y+dy[i]] != 0 or visited[x+dx[i]][y+dy[i]] == True: # 왼쪽이 0이 아니거나 이미 방문했을때(왼쪽에 청소할 공간이 없을때)
    #         s.append([x, y, (d2+3)%4]) # 현재 위치에서 왼쪽으로 회전만 시킨 뒤 break
    #         s.popleft()
    #         result = True
    #         break
    #
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