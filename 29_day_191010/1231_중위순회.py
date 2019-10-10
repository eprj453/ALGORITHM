import sys
sys.stdin = open('1231_input.txt', 'r')

def in_order(node):
    if len(linked[node]) == 2:
        in_order(linked[node][0])
        print(nodes[node][0], end='')
        in_order(linked[node][1])
    else:
        if len(linked[node]) == 1:
            in_order(linked[node][0])
            print(nodes[node][0], end = '')
        else:
            print(nodes[node][0], end = '')

for i in range(1, 11):
    n = int(input())
    nodes, linked = [], []
    for j in range(n+1):
        temp, temp2 = [], []
        nodes.append(temp)
        linked.append(temp2)
    for j in range(n):
        node_edge = list(input().split())
        for k in range(len(node_edge)):
            if k == 1:
                nodes[int(node_edge[0])].append(node_edge[k])
            elif k >= 2:
                linked[int(node_edge[0])].append(int(node_edge[k]))

    print('#{}'.format(i), end=' ')
    in_order(1)
    print()

    # print(node_edge)

