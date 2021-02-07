graph = [
    [],
    [2], # 1
    [3], # 2
    [5], # 3
    [2],
    [6, 7],
    [8],
    [],
    [],
    [10],
    [11], # 10
    [12], # 11
    [13], # 12
    [14, 15],
    [11],
    [],
    [17],
    [18],
    []
]

n = 15

cycle_size = [0] * (n+1)



for node, connects in graph:
    graph_count = 1
    if cycle_size[node] != 0: continue

    node_stk = [node]
    cycle_visited = [False] * (n + 1)
    cycle_visited[node] = True

    while node_stk:
        current = node_stk.pop()
        for next_node in graph[current]:
            if cycle_visited[next_node]: # 이미 방문한적 있는 노드
                cycle_visited = [idx for idx, node in enumerate(cycle_visited) if node]
                for c in cycle_visited:
                    cycle_size[c] = len(cycle_visited)

                break










