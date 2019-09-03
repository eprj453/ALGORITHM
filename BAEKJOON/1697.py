n, k = map(int, input().split())

q = []
q.append([n, 0])
visited = [False] * 100001
print(visited)

while len(q) > 0:
    # print(q)
    if q[0][0]+1 == k or q[0][0]-1 == k or q[0][0]*2 == k:
        print(q[0][1] + 1)
        break
    else:
        if 0 <= q[0][0]+1 and visited[q[0][0]+1] == False:
            q.append([q[0][0]+1, q[0][1]+1])
            visited[q[0][0]+1] = True
        if 0 <= q[0][0]-1 and visited[q[0][0]-1] == False:
            q.append([q[0][0]-1, q[0][1] + 1])
            visited[q[0][0]-1] = True
        if 0 <= q[0][0]*2 and visited[q[0][0]*2] == False:
            q.append([q[0][0]*2, q[0][1] + 1])
            visited[q[0][0]*2] = True

    q.pop(0)