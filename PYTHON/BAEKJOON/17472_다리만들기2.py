def mst(node, parent):
    if node == parent[node]:
        return node

    root = mst(parent[node], parent)
    return root

answer = 0
n, m = map(int, input().split())
islands = [list(input().split()) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

num = 1
for i in range(n): # 번호 매기기
    for j in range(m):
        if islands[i][j] == '1' and not check[i][j]:
            check[i][j] = num
            q = []
            q.append([i, j])
            while q:
                x, y = q.pop(0)
                for dir in dirs:
                    dx, dy = x + dir[0], y + dir[1]
                    if 0 <= dx < n and 0 <= dy < m:
                        if islands[dx][dy] == '1' and not check[dx][dy]:
                            check[dx][dy] = num
                            q.append([dx, dy])
            num += 1


tree_dict = dict()
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if check[i][j] and not visited[i][j]:
            bridge_dict = dict()
            visited[i][j] = True
            q = [[i, j]]
            while q:
                flag = False
                x, y = q.pop(0)
                for dir in dirs:
                    dx, dy = x + dir[0], y + dir[1]
                    if 0 <= dx < n and 0 <= dy < m:
                        if not check[dx][dy]:
                            flag = True
                if flag: # 다리 있음
                    for dir in dirs:
                        dx, dy = x + dir[0], y + dir[1]
                        if 0 <= dx < n and 0 <= dy < m:
                            if not visited[dx][dy]:
                                if not check[dx][dy]:
                                    bridge_dict[(x, y)] = bridge_dict.get((x, y), []) + [[dx-x, dy-y]]
                                else:
                                    visited[dx][dy] = True
                                    q.append([dx, dy])

                visited[x][y] = True
            # print(bridge_dict)
            q = []
            for key, value in bridge_dict.items():
                for v in value:
                    q.append([(key[0], key[1]), (v[0], v[1]), 0])
            # print(check[i][j])
            while q:
                info = q.pop(0)
                x, y, dirx, diry, distance = info[0][0], info[0][1], info[1][0], info[1][1], info[2]
                dx, dy = x + dirx, y + diry
                if 0 <= dx < n and 0 <= dy < m:
                    if not check[dx][dy]:
                        q.append([(dx, dy), (dirx, diry), distance+1])
                    else:
                        i1, i2 = check[i][j], check[dx][dy]
                        i1, i2 = min(i1, i2), max(i1, i2)
                        if i1 != i2 and distance > 1:
                            # print('print(i1, i2 = {}, {}, distance : {} )'.format(i1, i2, distance))
                            tree_dict[(i1, i2)] = min((tree_dict.get(i1, i2), 10), distance)
                            # print(tree_dict[(min(i1, i2), max(i1, i2))] )
# for i in range(n):
#     print(check[i])

# print(tree_dict)
tree_list = [(key,value) for key, value in tree_dict.items()]
tree_list.sort(key=lambda x : x[1])
# print(tree_list)

size = [1 for _ in range(num+1)]
parent = [x for x in range(num+1)]

count = 0
for node, edge in tree_list:
    if count == num-2: break
    n1, n2 = node[0], node[1]
    p1, p2 = mst(n1, parent), mst(n2, parent)

    if p1 != p2:
        # print(n1, n2)
        s1, s2 = size[n1], size[n2]
        if s1 > s2:
            parent[p1] = p2
            size[n2] += size[n1]
        else:
            parent[p2] = p1
            size[n1] += size[n2]
        count += 1
        answer += edge

if answer == 0 or count != num-2:
    answer = -1

print(answer)

'''
10 6
0 0 0 1 0 0
0 0 0 1 0 0
0 1 0 0 0 1
0 0 0 0 0 0
1 1 0 1 1 0
1 0 0 0 1 0
1 1 0 0 1 0
0 0 0 0 1 1
0 0 0 0 0 0
0 1 0 0 0 0



14



9 5
0 1 1 1 1
1 0 0 1 0
0 0 0 1 0
1 1 0 0 1
1 1 0 1 1
1 0 0 0 1
1 0 1 1 0
0 0 1 0 0
0 0 0 0 0


13
'''




                    
            

