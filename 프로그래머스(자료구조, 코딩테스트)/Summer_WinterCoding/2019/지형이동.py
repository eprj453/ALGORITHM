def solution(land, height):
    w, h = len(land), len(land[0])
    answer = 0
    visited = [[0] * h for _ in range(w)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    num = 0
    for i in range(w):
        for j in range(h):
            if not visited[i][j]:
                q = [[i, j]]
                visited[i][j] = num + 1
                while q:
                    x, y = q[0][0], q[0][1]
                    for k in range(4):
                        kx, ky = x + dx[k], y + dy[k]
                        if 0 <= kx < h and 0 <= ky < w:
                            if abs(land[x][y] - land[kx][ky]) <= height:
                                if visited[kx][ky] == 0:
                                    visited[kx][ky] = num + 1
                                    q.append([kx, ky])

                    q.pop(0)
                num += 1

    print(visited)
    tmp = 10000
    weight_dict = {}
    for i in range(w):
        for j in range(h):
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < h and 0 <= y < w:
                    if visited[i][j] != visited[x][y]:
                        l1, l2 = min(visited[i][j], visited[x][y]), max(visited[i][j], visited[x][y])
                        weight_dict[(min(l1, l2), max(l1, l2))] = min(weight_dict.get((l1, l2), 10000), abs(land[i][j] - land[x][y]))

    # answer = sum(list(weight_dict.values)[:(height-1)])
    bridge_num = num - 1
    weight_list = [(value, (key[0], key[1])) for key, value in weight_dict.items()]
    weight_list.sort()
    print(weight_list)
    # answer = sum(sorted(list(weight_dict.values()))[:bridge_num])
    land_sets = [[x] for x in range(1, num+1)]
    print(land_sets)
    # print(land_sets)
    for weight in weight_list:
        w, l1, l2 = weight[0], weight[1][0], weight[1][1]

        l1_set, l2_set = 0, 0
        for l in range(len(land_sets)):
            if l1 in land_sets[l] and l2 in land_sets[l]:
                break

            if l1 in land_sets[l]: l1_set = l
            if l2 in land_sets[l]: l2_set = l


        else:
            add_set = set(land_sets[l1_set]).union(land_sets[l2_set])
            # temp_set = set(land_sets) - land_sets[l1_set]
            temp_set = list(set(land_sets) - set(land_sets[l2_set]))
            answer += w
            bridge_num -= 1

        if not bridge_num: break

    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
# print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
