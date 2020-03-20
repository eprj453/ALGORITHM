import sys
sys.stdin = open('1949_input.txt', 'r')


def bfs(x, y, can_dig, distance):

    global max_distance

    for k in range(len(dx)):
        if 0 <= x+dx[k] < n and 0 <= y+dy[k] < n:
            if can_dig == True: # 땅파기 가능
                if maps[x][y] <= maps[x+dx[k]][y+dy[k]] and visited[x+dx[k]][y+dy[k]] == False:
                    for l in range(s+1):
                        if maps[x+dx[k]][y+dy[k]] - l < maps[x][y]:
                            maps[x + dx[k]][y + dy[k]] -= l
                            visited[x+dx[k]][y+dy[k]] = True
                            bfs(x+dx[k], y+dy[k], False, distance+1)
                            maps[x + dx[k]][y + dy[k]] += l
                            visited[x + dx[k]][y + dy[k]] = False


                if maps[x][y] > maps[x+dx[k]][y+dy[k]] and visited[x+dx[k]][y+dy[k]] == False:
                    visited[x + dx[k]][y + dy[k]] = True
                    bfs(x+dx[k], y+dy[k], True, distance+1)
                    visited[x + dx[k]][y + dy[k]] = False

            else:
                if maps[x][y] > maps[x+dx[k]][y+dy[k]] and visited[x+dx[k]][y+dy[k]] == False:
                    visited[x + dx[k]][y + dy[k]] = True
                    bfs(x+dx[k], y+dy[k], False, distance+1)
                    visited[x + dx[k]][y + dy[k]] = False

    if distance >= max_distance:
        max_distance = distance

    return



dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(1, int(input())+1):
    n, s = map(int, input().split())
    maps = []
    visited = []
    max_height, max_distance = 0, 0
    max_areas = []
    for j in range(n):
        temp = list(map(int, input().split()))
        for k in range(n):
            if temp[k] >= max_height:
                if temp[k] > max_height:
                    max_height = temp[k]
                    max_areas = [[j, k]]
                if temp[k] == max_height:
                    max_areas.append([j, k])
        maps.append(temp)
        visited.append([False] * n)

    for area in max_areas:
        visited[area[0]][area[1]] = True
        bfs(area[0], area[1], True, 1)
        visited[area[0]][area[1]] = False

    print('#{} {}'.format(i, max_distance))