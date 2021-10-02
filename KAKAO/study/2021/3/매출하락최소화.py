children = [[] for _ in range(300_001)]
dp = [[0, 0] for _ in range(300_001)]


def recursive_tree(node, sales):
    idx = node - 1

    if not children[node]: # leaf node
        dp[node] = [sales[idx], 0]
        return

    for child_node in children[node]:
        recursive_tree(child_node, sales)

    present = sales[idx] # 현재 node가 참석하는 경우
    absent = 0 # 현재 node가 불참하는 경우

    # 현재 Node가 참석하는 경우 자식 node는 참석하든 안하든 상관없음. 최소가 되도록 합을 맞춘다.
    present += sum([min(dp[child_node]) for child_node in children[node]])

    # 현재 node가 불참할 경우 자식 node 중 하나는 참석해야 한다. 원소 1개는 반드시 present가 들어가도록 한다.

    min_absent = 300_000 * 10_000
    for child_node in children[node]:
        node_present = dp[child_node][0]
        others = sum([min(dp[other_node]) for other_node in children[node] if other_node != child_node])
        min_absent = min(min_absent, node_present + others)
    print(min_absent)

    # 자식 node를 순회하며 이 node가 참석 + 이 node 외에 모든 node가 불참한 경우를 구해 최소값 구함.
    # min_absent = 300_000 * 10_000
    # for child_node in children[node]:
    #     child_node_present, child_node_absent = dp[child_node]
    #     min_value = min(child_node_absent, child_node_absent)
    #     other_node_absent = child_absent_sum - child_node_absent
    #     min_absent = min(min_absent, child_node_present + other_node_absent)

    dp[node] = [present, min_absent]
    return


def solution(sales, links):
    answer = 0
    for link in links:
        parent, child = link
        children[parent].append(child)

    recursive_tree(1, sales)
    answer = min(dp[1])
    # print(dp[:len(sales)+1])
    return answer

a = solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])

# a = solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]])
print(dp[:5])