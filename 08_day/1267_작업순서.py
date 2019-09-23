import sys
sys.stdin = open('작업순서_input.txt', 'r')

def DFS():
    x = s[-1] # 0
    while s:
        for k in range(len(aim[x])):
            if visited[[x][k]] == False:
                result = False
                for l in range(targeted[aim[x][k]]):
                    if targeted[aim[x][k]][l] == False:
                        result = True
                        break
                if result == True:
                    visited[[x][k]] = True
                    s.append(aim[x][k])
                    print(aim[x][k], end = ' ')
                if result == False:
                    res = s.pop()



n = 0
while n < 10:
    v, e = map(int, input().split())
    targeted = []
    aim = []
    s = []
    node = list(map(int, input().split()))
    for j in range(v + 1):
        temp, temp2 = [], []
        targeted.append(temp)
        aim.append(temp2)
    for j in range(len(node) // 2):
        targeted[node[j*2+1]].append(node[j*2])
        aim[node[j*2]].append(node[j*2+1])
    for j in range(1, len(targeted)):
        if not targeted[j]:
            # s.append(j)
            aim[0].append(j)
            targeted[j].append(0)

    visited = [False] * (v+1)
    visited[0] = True
    s = [0]
    # print('targeted : ', targeted)
    # print('aim : ', aim)
    # print('s : ', s)
    DFS()
    n += 1

# for i in range(1, 11):
#     v, e = map(int, input().split())
#     print(v)
#     line_list = list(map(int, input().split()))
#     matrix = []
#     rev_matrix = []
#     target_list = []
#     for j in range(v+1):
#         temp = []
#         temp2 = []
#         matrix.append(temp)
#         rev_matrix.append(temp2)
#     # print(matrix)
#     for j in range(len(line_list) // 2):
#         matrix[line_list[j*2]].append(line_list[(j*2)+1])
#         rev_matrix[line_list[(j*2)+1]].append(line_list[j*2])
#         target_list.append(line_list[(j*2)+1])
#     for j in range(1, len(rev_matrix)):
#         if len(rev_matrix[j]) == 0:
#             rev_matrix[j].append(0)
#             matrix[0].append(j)
#     # print(matrix)
#     # print(len(target_list))
#     print('matrix', matrix)
#     print('rev_matrix', rev_matrix)
#     # print(target_list)
#
#     stack = [0]
#     visited = [False] * (v+1)
#     visited[0] = True
#     ans_list = []
#
#     # print('rev_matrix', rev_matrix)
#     # print('matrix', matrix)
#     # print('visited', visited)
#     while len(stack) >= 0:
#         # if i >= 5:
#         #    print('stack ', stack)
#         print('stack :  {}'.format(stack))
#         for search in matrix[stack[-1]]: # 최상위 노드부터 탐색
#             # print('search', search)
#             if visited[search] == False: # 아직 방문하지 않은 노드라면 나를 노리고 있는 node들이 작업완료 되었는지 확인
#                 # stack.append(search)  # 스택에 추가
#                 result = True
#                 for k in range(len(rev_matrix[search])):
#                     if visited[rev_matrix[search][k]] == False: # 나를 노리고 있는 node중 방문하지 않은 node가 있다면
#                         result = False
#                         break
#                 if result == True: # 아직 방문하지 않았고 나를 노리고 있는 node가 전부 방문완료라면
#                     stack.append(search) # 스택에 추가
#                     print('stack 2', stack)
#                     visited[search] = True # 방문표시
#                     ans_list.append(str(search)) # 경로에 추가
#                     break
#         # if visited[stack[-1]] == True: and len(matrix[stack[-1]]) == 0:
#         if visited[stack[-1]] == True:
#             result2 = False
#             for k in matrix[stack[-1]]: # [102, 85, 101]
#                 result3 = True
#                 for l in rev_matrix[k]:
#                     if visited[l] == False:
#                         result3 = False
#                         break
#                 if result3 == True:
#                     result2 = True
#                     break
#
#             if result2 == False:
#                 out = stack.pop()
#                 if len(stack) == 0:
#                     break
#                 matrix[stack[-1]].remove(out)
#
#     print(len(ans_list))
#     print('#{} {}'.format(i, ' '.join(ans_list)))












