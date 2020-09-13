from queue import PriorityQueue

def dijk(s, n, graph):
    dist = [20000000] * (n+1)
    visited = [False] * (n+1)

    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        d, u = pq.get()
        if d > dist[u]: continue
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v] and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))

    return dist

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        u, v, w = fare
        graph[u].append((v, w))
        graph[v].append((u, w))



    from_start = dijk(s, n, graph)
    from_a = dijk(a, n, graph)
    from_b = dijk(b, n, graph)

    print(from_start)
    no_carfull = from_start[a] + from_start[b]
    carfull = 20000000
    for i in range(1, n+1):
        carfull = min(from_start[i] + from_a[i] + from_b[i], carfull)

    return min(carfull, no_carfull)

# print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,))
# print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))