import sys
sys.stdin = open('5251_input.txt', 'r')

def DIJKSTRA_ARRAY(s):

    D = [0xfffff] * (n + 1)
    P = [i for i in range(n + 1)]
    visit = [False] * (n + 1)
    D[s] = 0

    cnt = n
    while cnt:                              # 정점의 수 만큼 반복
        u, MIN = 0, 0xfffff                 # D[] 가 최소인 정점 찾기
        for i in range(1, n + 1):           # 무식하게 리스트에서 찾기
            if not visit[i] and D[i] < MIN:
                u, MIN = i, D[i]

        visit[u] = True

        for v, w in nodes[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u

        cnt -= 1

    print(D)
    print('#{} {}'.format(k, D[n]))
    # print(P[1: n + 1])





for k in range(1, int(input())+1):
    n, m = map(int, input().split())
    nodes = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        nodes[s].append((e, w))
        nodes[e].append((s, w))

    DIJKSTRA_ARRAY(0)