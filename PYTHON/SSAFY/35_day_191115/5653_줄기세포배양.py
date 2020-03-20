import copy
import sys
sys.stdin = open('5653_input.txt', 'r')



# 0 : 비활성, 1 : 활성, 2 : 사멸
# 대기 크기, 현상태, 원래크기
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# di = {1 : 123, 2: 234}
# di.pop(2)
# print(di)
# print(di.keys())
# print(di.get(2))
for i in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(n)]
    living_cells = {}
    dead_cells = {}
    living_count = 0
    for j in range(n):
        for l in range(m):
            if cells[j][l] != 0:
                living_cells[(j, l)] = [0, cells[j][l], cells[j][l]]
                living_count += 1
    for _ in range(k):
        # print(living_cells)
        new_cells = {}
        for key, value in living_cells.items():
            st, va, ce  = value[0], value[1], value[2]
            if st == 0: # 아직 비활성일 경우
                if va == 1:
                    living_cells[key][0] = 1
                else:
                    living_cells[key][1] -= 1
                    # va -= 1
            elif st == 1: # 활성 상태일 경우
                for k in range(4):
                    nx, ny = key[0]+dx[k], key[1]+dy[k]
                    if new_cells.get((nx, ny)) == None:
                        new_cells[(nx, ny)] = [0, ce, ce]
                        living_count += 1
                    else:
                        targetSt = new_cells[(nx, ny)][0]
                        if targetSt == 0 or targetSt == 1: # 비활성일 경우
                            if targetSt < st:
                                new_cells[(nx, ny)] = [0, ce, ce]
                living_count -= 1
                living_cells[key][0] = 2
        living_cells.update(new_cells)
    print(living_count)

            # for k in range(4):
            #     nx, ny = key[0] + dx[k], key[1] + dy[k]
            #     if living_cells[(nx, ny)] == None:


    # cnt = 0
    # living_cells = {
# }
    # n, m, k = map(int, input().split())
    # # cells = [list(map(int, input().split())) for _ in range(n)]
    # for j in range(n):
    #     temp = list(map(int, input().split()))
    #     for l in range(len(temp)):
    #         if temp[l] != 0:
    #             living_cells[(j, l)] = [temp[l], 0, temp[l]]
    #             cnt += 1
    # # print(cell_dict)
    # dead_cells = {}
    # t = 0
    # while t < k:
    #     t_living_cells = copy.deepcopy(living_cells)
    #     for key, info in living_cells.items():
    #         if info[1] == 0: # 비활성
    #             temp_info = t_living_cells.get(key)
    #             if temp_info[0] == 1:
    #                 temp_info[0] = 0
    #                 temp_info[1] = 1
    #             else:
    #                 temp_info[0] -= 1
    #
    #         elif info[1] == 1:
    #             temp_info = t_living_cells.get(key)
    #             for l in range(len(dx)):
    #                 target = (key[0] + dx[l], key[1] + dy[l])
    #                 if dead_cells.get(target) == None: # 죽은 셀이 자리를 차지하고 있을 경우
    #                     if t_living_cells.get(target) == None:
    #                         t_living_cells[target] = [temp_info[2], 0, temp_info[2]]
    #                     else:
    #                         target_info = t_living_cells.get(target)
    #                         if target_info[1] == 0: #
    #                             if target_info[2] < temp_info[2]:
    #                                 target_info[0], target_info[2] = temp_info[0], temp_info[2]
    #                                 # t_living_cells[target] = [temp_info[2], 0, temp_info[2]]
    #             dead_cells[key] = [info[2], 2, info[2]]
    #     living_cells = t_living_cells
    #     t += 1
    #
    # print(len(living_cells))
