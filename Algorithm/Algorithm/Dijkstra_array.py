import sys
sys.stdin = open('Dijkstra_array.txt', 'r')

def DIJKSTRA_ARRAY(s):

    D = [0xfffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[s] = 0

    cnt = V
    while cnt:                              # 정점의 수 만큼 반복

        u, MIN = 0, 0xfffff                 # D[] 가 최소인 정점 찾기
        for i in range(1, V + 1):           # 무식하게 리스트에서 찾기
            if not visit[i] and D[i] < MIN:
                u, MIN = i, D[i]

        visit[u] = True

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u

        cnt -= 1

    print('#{} 가중치 {}'.format(k, D[1: V + 1]))
    print('#{} 부모 node {}'.format(k, P[1: V + 1]))

for k in range(1, 4):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

    DIJKSTRA_ARRAY(1)
