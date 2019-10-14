import sys
sys.stdin = open('5249_input.txt', 'r')

def prim_minTree(g, s):
    ans = 0
    wei = [11] * (v+1)
    parent = [None] * (v+1)
    visited = [False] * (v+1)
    wei[s] = 0
    print('wei : ', wei)
    for _ in range(v+1):
        min_idx = -1
        min = 11
        for k in range(v+1):
            if not visited[k] and wei[k] < min:
                min_idx = k
                min = wei[k]
        visited[min_idx] = True
        ans += min
        print('min_idx :', min_idx)
        print('min_weight : ', min)
        for n, val in graph[min_idx]:
            if not visited[n] and val < wei[n]:
                wei[n] = val
                parent[n] = min_idx
    print(parent)
    return ans
for i in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
    ans = 0
    print('graph : ', graph)
    print('#{} {}'.format(i, prim_minTree(graph, 0)))
    # print(ans)
    # print()