from collections import deque
com = int(input())
edge = int(input())
virus = []
visited = [False] * (com+1)
count = 0
q = []
for i in range(com+1):
    temp = []
    virus.append(temp)
for i in range(edge):
    n, m = map(int, input().split())
    virus[n].append(m)
    virus[m].append(n)
q.append(1)
visited[1] = True
while q:
    x = q[0]
    for v in virus[x]:
        # print(virus[x][v])
        if visited[v] == False:
            visited[v] = True
            q.append(v)
            count += 1
    q.pop(0)
print(count)