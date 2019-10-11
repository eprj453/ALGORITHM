import sys
sys.stdin = open('5174_input.txt', 'r')

def search(v):
    global count

    if len(nodes[v]) == 0:
        return
    else:
        for i in range(len(nodes[v])):
            count += 1
            search(nodes[v][i])



for i in range(1, int(input())+1):
    e, n = map(int, input().split())
    node_temp = list(map(int, input().split()))
    nodes = []
    for j in range(e+2):
        temp = []
        nodes.append(temp)
    for j in range(0, len(node_temp), 2):
        nodes[node_temp[j]].append(node_temp[j+1])
    count = 1
    search(n)
    print('#{} {}'.format(i, count))