def search(k, start):
    global min_val
    if k == m:
        min_val = min(min_val, check(temp))
        return
    else:
        for x in range(start, l):
            temp[k] = chicken[x]
            search(k+1, x+1)



def check(temp):
    distance_sum = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == '1':
                min_val2 = 100000000
                for k in temp:
                    if abs(i - k[0]) + abs(j - k[1]) < min_val2:
                        min_val2 = abs(i - k[0]) + abs(j - k[1])
                distance_sum += min_val2
    return distance_sum


n, m = map(int, input().split())
city = [list(input().split()) for _ in range(n)]
chicken = []
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if city[i][j] == '2':
            chicken.append([i, j])

l = len(chicken)
temp = [[]] * m
min_val = 10000000000

if len(chicken) == m:
    min_val = check(chicken)
else:
    search(0, 0)

print(min_val)