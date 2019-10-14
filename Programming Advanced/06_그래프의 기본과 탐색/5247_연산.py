from collections import deque

for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [False] * 1000001
    q = deque()
    q.append([n, 0])
    visited[n] = True
    ans = 0
    while q:
        p_q = q.popleft()
        x, y = p_q[0], p_q[1]
        if x - 1 == m or x + 1 == m or x *2 == m or x - 10 == m:
            ans = y+1
            break
        if 0 <= x - 1 <= 1000000 and visited[x-1] == False:
            q.append([x-1, y+1])
            visited[x-1] = True
        if 0 <= x + 1 <= 1000000 and visited[x+1] == False:
            q.append([x+1, y+1])
            visited[x+1] = True
        if 0 <= x * 2 <= 1000000 and visited[x*2] == False:
            q.append([x*2, y+1])
            visited[x*2] = True
        if 0 <= x - 10 <= 1000000 and visited[x-10] == False:
            q.append([x-10, y+1])
            visited[x-10] = True

    ans = 0 if ans == 0 else ans
    print('#{} {}'.format(i, ans))