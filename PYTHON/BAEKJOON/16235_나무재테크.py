# import copy
# import heapq
# n, m, k = map(int, input().split())
# nutrients = [list(map(int, input().split())) for _ in range(n)]
# maps = [[5]* n for _ in range(n)]
# tree_dict = {}
# for _ in range(m):
#     heap = []
#     x, y, year = map(int, input().split())
#     heapq.heappush(heap, year)
#     tree_dict[(x-1, y-1)] = heap
# trees = m
# answer = 0
# dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
# for _ in range(k):
#     # print(maps)
#     # print(tree_dict)
#     for key, value in tree_dict.items():# 봄 - 나무가 양분 먹음, 나이 1 증가,
#         x, y = key[0], key[1]
#         pop_idx = len(tree_dict[key])
#         for i in range(len(tree_dict[key])):
#             # nutrient = maps[x][y]
#             if tree_dict[key][i] <= maps[x][y]: # 영양소를 따져보자.
#                 maps[x][y] -= tree_dict[key][i]
#                 tree_dict[key][i] += 1
#             else:
#                 pop_idx = i # 영양소가 없는 경우 즉시 파괴
#                 break
#         if pop_idx != len(tree_dict[key]): # 자라지 못한 나무들은 양분이 된다.
#             for nut in tree_dict[key][pop_idx:]:
#                 maps[x][y] += (nut // 2)
#             tree_dict[key] = tree_dict[key][:pop_idx]
#             # end = len(tree_dict[key])
#             # while pop_idx < end:
#             #     # print('h')
#             #     dead_tree_year = tree_dict[key].pop()
#             #     maps[x][y] += (dead_tree_year // 2)
#             #     pop_idx+=1
#
#     copy_tree_dict = copy.deepcopy(tree_dict)
#     for key, value in tree_dict.items():
#         # print(key)
#         x, y = key[0], key[1]
#         for tree_year in tree_dict[key]:
#             if not tree_year % 5: # 5의 배수일 경우 번식
#                 for d in dirs:
#                     dx, dy = x + d[0], y + d[1]
#                     if 0 <= dx < n and 0 <= dy < n:
#                         # print(dx, dy)
#                         if copy_tree_dict.get((dx, dy)): # 이미 기존에 나무가 있는 경우
#                             heapq.heappush(copy_tree_dict[(dx, dy)], 1)
#                         else:
#                             heap = []
#                             heapq.heappush(heap, 1)
#                             copy_tree_dict[(dx, dy)] = heap
#     tree_dict = copy_tree_dict
#     for i in range(n):
#         for j in range(n):
#             maps[i][j] += nutrients[i][j]
#     # print(tree_dict)
#     # print(maps)
# for value in tree_dict.values():
#     answer += len(value)
#
# # print(tree_dict)
# print(answer)


n, m, k = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
soils = [[5] * n for _ in range(n)]
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

answer = 0

for _ in range(m):
    x, y, year = map(int, input().split())
    trees[x-1][y-1].append(year)

for _ in range(k):
    for i in range(n): # 봄, 나무가 있을 경우
        for j in range(n):
            if trees[i][j]:
                x, dead = 0, -1
                dead_trees = []
                for x in range(len(trees[i][j])):
                    tree = trees[i][j][x]
                    if tree <= soils[i][j]: # 아직 자랄 수 있음.
                        soils[i][j] -= tree # 영양분 빨아들이고
                        trees[i][j][x] += 1 # 나무는 1살 추가
                    else:  #더 이상 자랄 수 없음.
                        dead = x
                        break
                if dead >= 0: #여름, 죽는 나무가 있다면
                    dead_trees = trees[i][j][dead:]
                    trees[i][j] = trees[i][j][:dead]
                    for tree in dead_trees:
                        soils[i][j] += (tree//2) # 죽은 나무는 양분으로

    for i in range(n):
        for j in range(n):
            if trees[i][j]: # 나무가 있는 경우
                for tree in trees[i][j]:
                    if tree % 5 == 0: # 나이가 5의 배수라면
                        for d in dirs:
                            x, y = i + d[0], j + d[1]
                            # print(x, y)
                            if 0 <= x < n and 0 <= y < n:
                                trees[x][y].insert(0, 1) # 나무를 심자

    for i in range(n):
        for j in range(n):
            soils[i][j] += nutrients[i][j]

for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)


