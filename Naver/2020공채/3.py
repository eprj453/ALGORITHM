cnt = 0
def get_child_count(num, graph):
    cnt = 0
    for i in graph[num]:
        cnt += 1
        if graph[i]:
            get_child_count(i, graph)

def solution(n, edges):
    global cnt
    answer = 0
    network = [[] for _ in range(n+1)]
    for edge in edges:
        p, c = edge
        network[p].append(c)
    print(network)
    get_child_count(1, network)
    print(cnt)

print(solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))