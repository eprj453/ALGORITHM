def pre_order(v):
    print(v, end = ' ')
    for i in range(2):
        if children[v][i] != 0:
            pre_order(children[v][i])

def in_order(v):
    if children[v][0] == 0 and children[v][1] == 0:
        print(v, end = ' ')
        return

    for i in range(len(children[v])):
        if i == 0 and children[v][i] != 0:
            in_order(children[v][0])
            print(v, end =' ')
        if i == 1 and children[v][i] != 0:
            in_order(children[v][1])

def post_order(v):
    if v != 0:
        post_order(children[v][0])
        post_order(children[v][1])
        print(v, end = ' ')
        return

n = 13
nodes = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
children = []
for _ in range(14):
    temp = [0,0]
    children.append(temp)
for i in range(0, len(nodes), 2):
    if children[nodes[i]][0] == 0:
        children[nodes[i]][0] = nodes[i+1]
    else:
        children[nodes[i]][1] = nodes[i+1]
print('전위 순회 결과 : ',end = ' ')
pre_order(1)
print()
print('중위 순회 결과 : ',end = ' ')
in_order(1)
print()
print('후위 순회 결과 : ',end = ' ')
post_order(1)
print()