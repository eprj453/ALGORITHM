import sys
sys.stdin = open('5643_input.txt', 'r')

from collections import deque


for i in range(1, int(input())+1):
    n = int(input())
    m = int(input())
    node_c = [[] for _ in range(n+1)]
    node_p = [[] for _ in range(n+1)]
    ans = 0
    for _ in range(m):
        short, tall = map(int, input().split())
        node_c[short].append(tall)
        node_p[tall].append(short)
    for j in range(1, n+1):
        visited = [False] * (n+1)
        can_ordered = {j}
        child_q, parent_q = deque(), deque()
        child_q.append(j)
        parent_q.append(j)

        visited[j] = True
        while child_q:
            node = child_q.popleft()
            if node_c[node]:
                for k in node_c[node]:
                    if visited[k] == False:
                        child_q.append(k)
                        can_ordered.add(k)
                        visited[k] = True

        while parent_q:
            node = parent_q.popleft()
            if node_p[node]:
                for k in node_p[node]:
                    if visited[k] == False:
                        parent_q.append(k)
                        can_ordered.add(k)
                        visited[k] = True

        if len(can_ordered) == n:
            ans += 1

    print('#{} {}'.format(i, ans))
    # print(node_parent)
