import sys
sys.stdin = open('1232_input.txt', 'r')


# def pre_order(v):
#     print(nodes[v], end = ' ')
#     for k in range(len(child[v])):
#         if child[v][k]:
#             pre_order(child[v][k])
def post_order(v):
    if not child[v]:
        return nodes[v]

    left = post_order(child[v][0])
    right = post_order(child[v][1])


    if nodes[v] == '+':
        return left + right
    if nodes[v] == '-':
        return left - right
    if nodes[v] == '*':
        return left * right
    if nodes[v] == '/':
        return left / right

for i in range(1, 11):
    n = int(input())
    nodes = [0] * (n+1)
    child = []
    for j in range(n+1):
        temp = []
        child.append(temp)
    for j in range(n):
        ope = list(input().split())
        if len(ope) >= 3:
            nodes[int(ope[0])] = ope[1]
            for k in range(2, len(ope)):
                child[int(ope[0])].append(int(ope[k]))
        else:
            nodes[int(ope[0])] = int(ope[1])
    # print('n : ', n)
    print('#{} {}'.format(i, round(post_order(1))))
    # # print()
    # print(nodes)
    # # print()
    # print(child)