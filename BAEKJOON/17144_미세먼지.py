# def clean(direction, r):
#     if direction == 1: # 시계방향

def dust_diffsion(c):
    dust_temp = []
    for h in range(r):
        temp = [0] * c
        dust_temp.append(temp)
    for i in range(len(dusts)):
        for j in range(len(dusts[i])):
            if dusts[i][j] == 0: continue
            if dusts[i][j] != 0 and dusts[i][j] != -1:
                x, y = i, j
                count = []
                for k in range(len(dx)):
                    if 0 <= x+dx[k] < len(dusts) and 0 <= y+dy[k] < len(dusts[i]) and dusts[x+dx[k]][y+dy[k]] != -1:
                        count.append([x+dx[k], y+dy[k]]) # 갯수 세기
                        dust_temp[x+dx[k]][y+dy[k]] += dusts[x][y]//5
                dust_temp[x][y] -= (dusts[x][y]//5) * len(count)
    for k in range(len(dusts)):
        for c in range(len(dusts[i])):
            dusts[k][c] += dust_temp[k][c]

def clean_air(x, y, direction):
    if direction == 0:
        while x != 0:
            # print('돈다')
            if x == machine:
                x -= 1
                continue
            else:
                dusts[x][0] = dusts[x-1][0]
            x -= 1
        # print('x : ',x)
        while y < c-1:
            # print(x, y)
            dusts[0][y] = dusts[0][y+1]
            y += 1
        while x < machine: # machine : 2
            dusts[x][y] = dusts[x+1][y]
            x += 1
        while y != 0:
            if y == 1:
                dusts[x][y] = 0
            else:
                dusts[x][y] = dusts[x][y-1]
            y -= 1
    else:
        while x < r-1:
            # print('x : ',x)
            if dusts[x][0] == -1:
                x += 1
                continue
            else:
                dusts[x][0] = dusts[x+1][0]
            x += 1
        while y < c-1:
            dusts[x][y] = dusts[x][y+1]
            y += 1
        while x > machine+1:
            dusts[x][y] = dusts[x-1][y]
            x -= 1
        while y != 0:
            if dusts[x][y-1] == -1:
                dusts[x][y] = 0
            else:
                dusts[x][y] = dusts[x][y-1]
            y -= 1





r, c, t = map(int, input().split())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
dusts = []
machine = 0
for i in range(r):
    tmp = list(map(int, input().split()))
    if tmp[0] == -1 and machine == 0:
        machine = i
    dusts.append(tmp)
dust_sum = 0
n = 0
while n < t:
    dust_diffsion(c)
    clean_air(machine, 0, 0)
    clean_air(machine+1, 0, 1)

    # for i in range(r):
    #     print(dusts[i])
    # print()
    n += 1


for i in range(r):
    for j in range(len(dusts[i])):
        if dusts[i][j] != -1:
            dust_sum += dusts[i][j]

print(dust_sum)
