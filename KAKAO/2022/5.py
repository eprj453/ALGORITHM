from itertools import permutations

'''
cmd : U / L / R
U :
'''
tree_subset = set()
layer_dict = dict()

children, parents = [[] for _ in range(18)], [0] * (18)

def get_layer(cnt, node, curr_node, parents):
    if curr_node == 0:
        layer_dict[cnt] = layer_dict.get(cnt, set())
        layer_dict[cnt].add(node)
        return

    get_layer(cnt+1, node, parents[curr_node], parents)


def get_children_node(parent_nodes):
    children_nodes = []
    for node in parent_nodes:
        if children[node]:
            children_nodes += children[node]

    return children_nodes


def find_all_tree_subset(subset: tuple, layer_nodes):
    tree_subset.add(tuple(subset))

    children_nodes = get_children_node(layer_nodes)

    children_subset = []
    for i in range(1, len(children_nodes)+1):
        children_subset.extend(permutations(children_nodes, i))

    if not children_subset:
        return

    for s in children_subset:
        new_subset = tuple(subset) + s
        find_all_tree_subset(new_subset, s)

    find_all_tree_subset((), [])




def solution(info, edges):
    answer = 0
    n = len(info)

    for edge in edges:
        p, c = edge
        children[p].append(c)
        parents[c] = p

    find_all_tree_subset([], [0])

    # for i in range(n):
    #     get_layer(0, i, i, parents)
    # # print(children)
    # # print(parents)
    # print(tree_subset)
    # print(len(tree_subset))
    for subset in tree_subset:
        cnt = 1
        sheep, wolf = 1, 0
        for s in subset:
            if info[s] == 1:
                cnt -= 1
                wolf += 1
            else:
                cnt += 1
                sheep += 1

        if cnt > 0:
            answer = max(answer, sheep)
    print(answer)
    return answer

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	)