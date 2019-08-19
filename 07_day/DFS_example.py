v, e = map(int, input().split())
visit = [False] * (v+1)
graph_list = [[] for _ in range(v+1)] # 사용하는 정점의 번호 1 ~ v+1

for _ in range(e): # 간선 개수만큼 읽기 시작
    u, v = map(int, input().split())
    graph_list[u].append(v)
    graph_list[v].append(u)


for i in range(1, v+1):
    print(i, '--->', graph_list[i])


def DFS(v): # v : 시작점
    stack = []

    visit[v] = True # 시작점 방문
    stack.append(v) # 시작점을 스택에 push하고 시작.
    while stack:
        #v에 방문하지 않은 인점정점을 찾는다 --> w
        for w in graph_list[v]:
            if not visit[w]: # visit[w]가 false라면
                visit[w] = True # w 방문
                stack.append(True)
                v = w # w를 현재 방문하는 접점 설정
                break
        else: # 이전에 방문한 정점으로 되돌아간다.
            v = stack.pop()




