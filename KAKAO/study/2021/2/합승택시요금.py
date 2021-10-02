from queue import PriorityQueue


def dijk(s, n, graph):
    dist = [20000000] * (n+1) # 가능한 최소비용을 최대로 설정
    visited = [False] * (n+1) # 방문 체크

    dist[s] = 0 # 시작점부터 시작점까지의 거리는 0
    pq = PriorityQueue()
    pq.put((0, s)) # 구하고자 하는 시작점부터 시작

    while not pq.empty():
        d, u = pq.get() # 현재 위치
        if d > dist[u]: continue # 시작점 위치보다 가능한 최소비용이 클 경우 굳이 볼 필요 없음
        visited[u] = True # 현재 위치는 방문했다고 표시
        for v, w in graph[u]: # 현재 위치와 연결되어 있는 노드(v)와 그 거리(w)
            if not visited[v] and dist[v] > dist[u] + w: # 방문한적 없고(방문한 곳은 이미 최소비용임) 연결되어 있는 노드의 최소비용이 갱신할 최소비용보다 더 클경우
                dist[v] = dist[u] + w # 갱신
                pq.put((dist[v], v)) #  queue에 삽입.

    return dist

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        u, v, w = fare
        graph[u].append((v, w))
        graph[v].append((u, w))



    from_start = dijk(s, n, graph) # 시작점에서부터 모든 노드까지의 거리
    from_a = dijk(a, n, graph) # a에서부터 모든 노드까지의 거리
    from_b = dijk(b, n, graph) # b에서부터 모든 노드까지의 거리

    no_carfull = from_start[a] + from_start[b] # 카풀하지 않았을때의 비용은 a 따로, b 따로 비용의 합
    carfull = 20000000 # 카풀했을때 비용을 최대로 잡음
    for i in range(1, n+1):
        carfull = min(from_start[i] + from_a[i] + from_b[i], carfull)

    return min(carfull, no_carfull)