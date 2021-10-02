dp = [[0, 0] for _ in range(10001)]
connected = [[] for _ in range(10001)]
visited = [False] * 10001
selected_nodes = []
independent_set = [False] * 10001

def recursive_tree(node: int, weights):
    # print(node)
    # print(visited[:10])
    # print(connected[node])
    # print()
    if not connected[node] or all([visited[x] for x in connected[node]]):
        # print(node)
        dp[node] = [weights[node - 1], 0]
        return

    visited[node] = True
    present = weights[node - 1]
    absent = 0
    # print([visited[x] for x in connected[node]])
    for connected_node in connected[node]:
        if not visited[connected_node]:
            recursive_tree(connected_node, weights)
        absent += max(dp[connected_node])
        present += dp[connected_node][1]

    dp[node] = [present, absent]
    return


def get_independent_set(node):
    visited[node] = True
    if independent_set[node]:
        for connected_node in connected[node]:
            if not visited[connected_node]:
                independent_set[connected_node] = False
                get_independent_set(connected_node)
    else:
        for connected_node in connected[node]:
            if not visited[connected_node]:
                present, absent = dp[connected_node]
                if present > absent:
                    independent_set[connected_node] = True
                else:
                    independent_set[connected_node] = False
                get_independent_set(connected_node)
    # if is_present: # 현재 node가 반드시 있어야 하는 node라면
    #     independent_set[node] = True
    #     for connected_node in connected[node]:
    #         if not visited[connected_node]:
    #             get_independent_set(False, connected_node) # 연결된 node는 전부 독립집합에 속하면 안됨.
    # else: #  현재 node가 있어도 그만 없어도 그민인 node라면
    #     for connected_node in connected[node]:
    #         present, absent = dp[node]
    #         if present > absent: # 현재 node가 있는게 더 이득이라면
    #             independent_set[node] = True
    #             get_independent_set(True, connected_node)
    #         else:
    #             independent_set[node] = False
    #             get_independent_set(False, connected_node)


n = int(input())
weights = [int(x) for x in list(input().split())]

for _ in range(n-1):
    nodes = list(map(int, input().split(' ')))
    # print(nodes)
    # nodes = nodes.replace(' ', '')
    node1, node2 = nodes[0], nodes[-1]
    connected[node1].append(node2)
    connected[node2].append(node1)

start = 1
visited[1] = True
# print(weights)
recursive_tree(1, weights)
# print(dp[:10])

visited = [False] * 10001
visited[1] = True
if dp[1][0] > dp[1][1]:
    independent_set[1] = True

get_independent_set(1)
independent_set = [str(idx) for idx, s in enumerate(independent_set) if s]
# print(connected[:n+1])
# print(dp[:n+1])
print(max(dp[1]))
print(' '.join(independent_set))
