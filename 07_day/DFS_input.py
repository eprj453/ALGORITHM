v, e = map(int, input().split())
visit = [False] * (v+1)

def DFS(v):
    visit[v] = True; print(v, end=' ')
    for w in graph_list[v]:
        if not visit[w]:
            DFS(w)


graph_list = [[] for _ in range(v+1)] # 사용하는 정점의 번호 1 ~ v+1

for _ in range(e): # 간선 개수만큼 읽기 시작
    u, v = map(int, input().split())
    graph_list[u].append(v)
    graph_list[v].append(u)


for i in range(1, v+1):
    print(i, '--->', graph_list[i])


