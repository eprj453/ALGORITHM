def spread_virus():
    global answer
    spreadVirus = 0
    virusMap = [[False] * n for _ in range(n)]
    q = []
    for v in comb:
        virusMap[v[0]][v[1]] = True
        q.append([v[0], v[1]])

    count = 0
    while q:
        print('ehsek')
        x, y = q[0][0], q[0][1]
        for k in range(4):
            kx, ky = x + dx[k], y + dy[k]
            if 0 <= kx < n and 0 <= ky < n:
                if virusMap[kx][ky] == False and maps[kx][ky] != '-':
                    virusMap[kx][ky] == True
                    q.append([kx, ky])
                    spreadVirus += 1
        q.pop(0)
        count += 1

    if maxVirus - spreadVirus == 0:
        answer = min(count, answer)
    return




def makeComb(k, start):
    if k == m:
        spread_virus()
        return

    for i in range(start, len(viruses)):
        comb.append(viruses[i])
        makeComb(k+1, i+1)
        comb.pop()



n, m = map(int, input().split())
maps = []
viruses = []
walls = 0
dx, dy = [0, 1, 0 ,-1], [1, 0, -1, 0]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            viruses.append((i, j))
    walls += temp.count(1)
    maps.append(temp)
comb_visited = [False] * len(viruses)
comb = []
answer = 0xffffff
mapSize = n * n
maxVirus = (n*n) - walls # 바이러스가 다 퍼졌을 때
makeComb(0, 0)

print(answer if answer != 0xffffff else -1)
