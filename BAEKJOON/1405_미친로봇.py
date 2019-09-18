def perm(s, e):
    global count
    global count2
    if s == e:
        result = []
        count2 += 1
        x, y = 0, 0
        result.append([0, 0])
        for i in temp:
            if i == 'E':
                y += 1
            elif i == 'W':
                y -= 1
            elif i == 'S':
                x += 1
            else:
                x -= 1
            if [x, y] in result:
                count += 1
                break
            else:
                result.append([x, y])
    else:
        for i in range(len(location)):
            if visited[i] == False:
                temp[s] = location[i]
                visited[i] = True
                perm(s+1, e)
                visited[i] = False



n, east, west, south, north = map(int, input().split())
location = []
temp = ['']*n
visited = [False] * 100
count = 0
count2 = 0
for i in range(east):
    location.append('E')
for i in range(west):
    location.append('W')
for i in range(south):
    location.append('S')
for i in range(north):
    location.append('N')
perm(0, n)
print(round(((count2- count)/count2), 2))