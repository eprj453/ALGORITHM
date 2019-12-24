def binary_search(v):
    if v > n-m:
        return

    if (v*2)+1 > n:
        nodes[v] = nodes[v*2]
        return

    binary_search(v * 2)
    binary_search((v * 2) + 1)

    if nodes[v*2] != 0 and nodes[v*2+1] != 0:
        nodes[v] = nodes[v*2] + nodes[v*2+1]
        return

for i in range(1, int(input())+1):
    ans = 0
    n, m, l = map(int, input().split())
    nodes = [0] * (n+1)
    for j in range(m):
        x, y = map(int, input().split())
        nodes[x] = y
    # print(ans)
    binary_search(l)
    print(nodes[l])


    # print(ans)