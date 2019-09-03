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
    if q[0][0]+1 == k or q[0][0]-1 == k or q[0][0]*2 == k:
        print(q[0][1] + 1)
        break
    else:
        q.append([q[0][0]+1, q[0][1]+1])
        q.append([q[0][0]-1, q[0][1] + 1])
        q.append([q[0][0]*2, q[0][1] + 1])
    q.pop(0)