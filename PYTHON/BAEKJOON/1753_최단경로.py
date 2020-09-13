from queue import PriorityQueue
import heapq

def dijk(start, v, graph):
    dist = [0xffffff] * (v+1)
    pos = [i for i in range(v+1)]
    visited = [False] * (v+1)
    dist[start] = 0
    # print(len(dist))
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        d, u = pq.get() # 거리, NODE
        if d > dist[u]: continue

        visited[u] = True
        for v, w in graph[u]: # NODE에 연결되어 있는 다른 node 체크
            if not visited[v] and dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                pos[v] = u
                pq.put((dist[v], v))

    return dist

def dijk_heapq(start, v, graph):
    dist = [0xffffff] * (v+1)
    visited = [False] * (v+1)

    hq = []
    heapq.heappush(hq, (0, start))

    dist[start] = 0

    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            # print(v, w)
            cost = d + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(hq, (cost, v))



    return dist



v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    u, v_2, w = map(int, input().split())
    graph[u].append((v_2, w))

result = dijk(start, v, graph)

for i in range(1, v+1):
    answer = result[i]
    answer = 'INF' if answer == 0xffffff else answer
    print(answer)




'''
6 7
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
4 6 7
'''