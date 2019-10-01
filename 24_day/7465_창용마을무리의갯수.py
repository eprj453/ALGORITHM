import sys
from collections import deque
sys.stdin = open('7465_input.txt', 'r')

def bfs(q):
    global count
    if not q:
        count += 1
        return
    else:
        for ele in matrix[q[0]]:
            if visited[ele] == False:
                visited[ele] = True
                q.append(ele)
        q.pop(0)
        bfs(q)



for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [False] * (n+1)
    matrix = []
    count = 0
    for j in range(n+1):
        temp = []
        matrix.append(temp)

    for j in range(m):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)

    q = []

    for e in range(1, n+1):
        if visited[e] == False:
            visited[e] = True
            q.append(e)
            while q:
                visited[q[0]] = True
                for t in matrix[q[0]]:
                    if visited[t] == False:
                        q.append(t)
                q.pop(0)
            count += 1


    print('#{} {}'.format(i, count))


