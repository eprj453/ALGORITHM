for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    nodes = list(map(int, input().split()))
    linked = []
    for j in range(n+1):
        temp = []
        linked.append(temp)
    for j in range(0, len(nodes), 2):
        linked[nodes[j]].append(nodes[j+1])
        linked[nodes[j+1]].append(nodes[j])
    visited = [False] * (n+1)
    ans = 0
    for j in range(1, n+1):
        if visited[j] == False:
            visited[j] = True
            q = [j]
            while q:
                x = q.pop(0)
                for node in linked[x]:
                    if visited[node] == False:
                        q.append(node)
                        visited[node] = True
            ans += 1

    print('#{} {}'.format(i, ans))