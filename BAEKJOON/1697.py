<<<<<<< HEAD
n, k = map(int, input().split())

q = []
q.append([n, 0])
visited = [False] * 100001
print(visited)

while len(q) > 0:
    # print(q)
=======
from collections import deque

n, k = map(int, input().split())

start = n
count = 0
if start != 0:
    while start < k:
        if start == k:
            print(count)
            break
        start *= 2
        count += 1
    print(start)
    if k - start < (2*start)-k:
        start /= 2
        count -= 1
    q = []
    q.append([start, count])
    print(q)

while len(q) > 0:
>>>>>>> 2e9aa022a685454e981f12ab60b977f0a21e9d98
    if q[0][0]+1 == k or q[0][0]-1 == k or q[0][0]*2 == k:
        print(q[0][1] + 1)
        break
    else:
<<<<<<< HEAD
        if 0 <= q[0][0]+1 and visited[q[0][0]+1] == False:
            q.append([q[0][0]+1, q[0][1]+1])
            visited[q[0][0]+1] = True
        if 0 <= q[0][0]-1 and visited[q[0][0]-1] == False:
            q.append([q[0][0]-1, q[0][1] + 1])
            visited[q[0][0]-1] = True
        if 0 <= q[0][0]*2 and visited[q[0][0]*2] == False:
            q.append([q[0][0]*2, q[0][1] + 1])
            visited[q[0][0]*2] = True

=======
        q.append([q[0][0]+1, q[0][1]+1])
        q.append([q[0][0]-1, q[0][1] + 1])
        q.append([q[0][0]*2, q[0][1] + 1])
>>>>>>> 2e9aa022a685454e981f12ab60b977f0a21e9d98
    q.pop(0)