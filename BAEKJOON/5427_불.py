for i in range(1, int(input())+1):
    w, h = map(int, input().split())
    start_x, start_y = 0, 0
    maps = []
    fires = []
    visited = []
    q = []
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    c = 0
    while c < h:
        temp = list(input())
        temp2 = [False] * w
        maps.append(temp)
        visited.append(temp2)
        for j in range(len(temp)):
            if temp[j] == '@':
                start_x, start_y = c, j
                visited[start_x][start_y] = True
            if temp[j] == '*':
                q.append([c, j, 1, 0])
                visited[c][j] = True
        c += 1
    q.append([start_x, start_y, 0, 0])
    min_distance = 0
    # 0 > 나, 1 > 불
    while q:
        x, y, which, count = q[0][0], q[0][1], q[0][2], q[0][3]
        if (x == 0 or y == 0 or x == h-1 or y == w-1) and which == 0:
            min_distance = count
            break

        if which == 1:
            for k in range(len(dx)):
                if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
                    if maps[x+dx[k]][y+dy[k]] == '.' and visited[x+dx[k]][y+dy[k]] == False:
                        q.append([x+dx[k], y+dy[k], which, count+1])
                        visited[x+dx[k]][y+dy[k]] = True

            q.pop(0)


        elif which == 0:
            for k in range(len(dx)):
                if 0 <= x+dx[k] < h and 0 <= y+dy[k] < w:
                    if (x == 0 or y == 0 or x == h or y == w) and which == 0:
                        min_distance = count
                        break
                    if maps[x+dx[k]][y+dy[k]] != '#' and visited[x+dx[k]][y+dy[k]] == False:
                        q.append([x+dx[k], y+dy[k], which, count+1])
                        visited[x+dx[k]][y+dy[k]] = True
            q.pop(0)

        if min_distance:
            break
    if min_distance == 0:
        print('IMPOSSIBLE')
    else:
        print(min_distance+1)