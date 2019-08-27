import sys
sys.stdin = open('작업순서_input.txt', 'r')

for i in range(1, 11):
    v, e = map(int, input().split())
    print(v)
    line_list = list(map(int, input().split()))
    matrix = []
    rev_matrix = []
    target_list = []
    for j in range(v+1):
        temp = []
        temp2 = []
        matrix.append(temp)
        rev_matrix.append(temp2)
    # print(matrix)
    for j in range(len(line_list) // 2):
        matrix[line_list[j*2]].append(line_list[(j*2)+1])
        rev_matrix[line_list[(j*2)+1]].append(line_list[j*2])
        target_list.append(line_list[(j*2)+1])
    for j in range(1, len(rev_matrix)):
        if len(rev_matrix[j]) == 0:
            rev_matrix[j].append(0)
            matrix[0].append(j)
    # print(matrix)
    # print(len(target_list))
    print('matrix', matrix)
    print('rev_matrix', rev_matrix)
    # print(target_list)

    stack = [0]
    visited = [False] * (v+1)
    visited[0] = True
    ans_list = []

    # print('rev_matrix', rev_matrix)
    # print('matrix', matrix)
    # print('visited', visited)
    while len(stack) >= 0:
        # if i >= 5:
        #    print('stack ', stack)
        print('stack :  {}'.format(stack))
        for search in matrix[stack[-1]]: # 최상위 노드부터 탐색
            # print('search', search)
            if visited[search] == False: # 아직 방문하지 않은 노드라면 나를 노리고 있는 node들이 작업완료 되었는지 확인
                # stack.append(search)  # 스택에 추가
                result = True
                for k in range(len(rev_matrix[search])):
                    if visited[rev_matrix[search][k]] == False: # 나를 노리고 있는 node중 방문하지 않은 node가 있다면
                        result = False
                        break
                if result == True: # 아직 방문하지 않았고 나를 노리고 있는 node가 전부 방문완료라면
                    stack.append(search) # 스택에 추가
                    print('stack 2', stack)
                    visited[search] = True # 방문표시
                    ans_list.append(str(search)) # 경로에 추가
                    break
        # if visited[stack[-1]] == True: and len(matrix[stack[-1]]) == 0:
        if visited[stack[-1]] == True:
            result2 = False
            for k in matrix[stack[-1]]: # [102, 85, 101]
                result3 = True
                for l in rev_matrix[k]:
                    if visited[l] == False:
                        result3 = False
                        break
                if result3 == True:
                    result2 = True
                    break

            if result2 == False:
                out = stack.pop()
                if len(stack) == 0:
                    break
                matrix[stack[-1]].remove(out)

    print(len(ans_list))
    print('#{} {}'.format(i, ' '.join(ans_list)))

            # elif visited[search] == True:
            #     result2 == True
            #     for k in range(rev_matrix[stack[-1]]):  # 나를 노리고 있는 node 검사
            #         if visited[rev_matrix[stack[-1]]][k] == False:
            #             result2 = False
            #             break
            #     if result2 == True:  # 나를 노리는 node가 없거나 전부 작업완료라면
            #         matrix[stack - 1].remove(search)
            #         stack.pop()
    # print(visited)
#     #
#     # while len(ans_list) < v:
#     for num in range(1, v+1):
#
#         if visited[num] == False:
#             # stack.append(num)  #
#             # visited[num] = True
#             result = True
#             if num not in ans_list and result == True:
#                 stack.append(num)  #
#                 visited[num] = True
#                 ans_list.append(str(num))
#
#                 while len(stack) > 0:
#                     pos = num
#                     for j in range(len(matrix[pos])):
#                         if visited[matrix[pos][j]] == False:
#                             stack.append(matrix[pos][j])
#                             num = matrix[pos][j]
#                             result = True
#                             for k in rev_matrix[num]:
#                                 if visited[k] == False:
#                                     result = False
#                                     break
#                             if num not in ans_list and result == True:
#                                 visited[matrix[pos][j]] = True
#                                 ans_list.append(str(num))
#                             break
#                     if pos == num:
#                         num = stack.pop()
#     print(len(ans_list))
#     print('#{} {}'.format(i, ' '.join(ans_list)))

    #
    # for pos in range(1, v+1):
    #     if visited[pos] == False:
    #         result = True
    #         for k in range(len(rev_matrix[pos])): # 현재 위치를 노리고 있는 해결되지 않은 node가 있는가
    #             if visited[rev_matrix[pos][k]] == False:
    #                 result = False
    #                 break
    #         if not pos in ans_list and result == True:
    #             stack.append(pos)
    #             visited[pos] = True
    #             ans_list.append(pos)
    #
    #         while len(stack) > 0: # 스택이 빌 때까지 반복
    #             for search in matrix[pos]: # 현재 위치가 가리키고 있는 node를 탐색
    #                 if visited[search] == False and len(rev_matrix[search]) == 0: # 방문한적이 없고 나를 가리키는 node가 없다면
    #                     visited[search] = True # 방문표시
    #                     stack.append(search) # 스택에 추가
    #                     pos = search # 위치를 가리키던 node로 변경.
    #                     ans_list.append(search) # 답 리스트에 추가.
    #                     break
    #                 result = True
    #                 for check in matrix[search]:
    #                     if visited[check] == False:
    #                         result = False
    #                         break
    #                 if result == False:
    #                     continue
    #                 if visited[search] == True:
    #                     stack.pop()
    #                     pos = stack[-1]
    #                     break
    #
    #
    # print(ans_list)





    # for num in range(1, v+1):
    #     # print('num : {}'.format(num))
    #     if visited[num] == False:
    #         result = True
    #         for k in rev_matrix[num]: # num을 노리고 있는 방문한 적 없는 node가 있는지 확인.
    #             if visited[k] == False:
    #                 result = False
    #                 break
    #         if not num in ans_list and result == True:
    #             stack.append(num)  #
    #             print('초기 stack : {}'.format(stack))
    #             visited[num] = True
    #             print('{} > true'.format(num))
    #             ans_list.append(str(num))
    #         print('num : {}'.format(num))
    #         while len(stack) > 0:
    #             pos = num
    #             for j in range(len(matrix[pos])):
    #                 print('확인 : {}'.format(matrix[pos][j]))
    #                 result2 = True
    #                 if visited[matrix[pos][j]] == False:
    #                     for k in rev_matrix[num]:
    #                         if visited[k] == False:
    #                             result2 = False
    #                             break
    #                 if pos not in ans_list and result2 == True:
    #                     stack.append(matrix[pos][j])
    #                     print('stack 추가 : {}'.format(stack))
    #                     num = matrix[pos][j]
    #                     print('num 변경. {}'.format(num))
    #                     visited[matrix[pos][j]] = True
    #                     print('{} > true'.format(matrix[pos][j]))
    #                     ans_list.append(str(num))
    #                     print('ans_list in {}'.format(num))
    #                     break
    #             print('pos : {}, num : {}'.format(pos,num))
    #             result3 = True
    #             print('len_rev_matrix is {}'.format(len(matrix[pos])))
    #             if pos == num: # num이 바뀌지 않았다면(탐색 가능한 node가 없었다면)
    #                 num = stack.pop()
    #
    #                 print('{} out of stack'.format(num))
    # print('#{} {}'.format(i, ' '.join(ans_list)))

# for i in range(1, 11):
#     v, e = map(int, input().split())
#     # print(v)
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
#     # print(matrix)
#     # print(len(target_list))
#     # print(matrix)
#     # print(target_list)
#
#     stack = []
#     visited = [False] * (v+1)
#     ans_list = []
#     # for j in range(v+1):
#     #     temp = 0
#     #     visited.append(temp)
#     # print('target_list : {}'.format(target_list))
#     # print('matrix : {}'.format(matrix))
#     # print(matrix)
#     # print(rev_matrix)
#     range_list = list(range(1, v+1))
#     while len(ans_list) < v:
#         for num in range_list: # node 중 가리켜지는 edge가 없는 node 탐색
#             if visited[num] == False:
#                 result = True
#                 for k in rev_matrix[num]:
#                     if visited[k] == False:
#                         result = False
#                         break
#                 if num not in ans_list and result == True:
#                     stack.append(num)  #
#                     visited[num] = 1
#                     ans_list.append(str(num))
#                     range_list.remove(num)
#                 # print('stack : {}'.format(stack))
#                 while len(stack) > 0: # stack의 길이가 0이 될때까지 반복
#                     pos = num  # 현재 위치 표시
#                     for j in range(len(matrix[pos])):
#                         if visited[matrix[pos][j]] == False: # 방문한 적이 없다면
#                             stack.append(matrix[pos][j])
#                             # print('stack : {}'.format(stack))
#                             num = matrix[pos][j]
#                             visited[matrix[pos][j]] = True
#                             result2 = True
#                             for k in rev_matrix[num]:
#                                 if visited[k] == False:
#                                     result2 = False
#                                     break
#                             if num not in ans_list and result2 == True:
#                                 ans_list.append(str(num))
#                                 range_list.remove(num)
#                             break
#                     if pos == num:
#                         pos = stack.pop()
#                         # print('stack : {}'.format(stack))
#     print(len(ans_list))
#     print('#{} {}'.format(i, ' '.join(ans_list)))
    #             print('stack : {}'.format(stack))
    #             visited[stack[-1]] = 1  # 방문 완료
    #             ans_list.append()
    #             if len(matrix[stack[-1]]) == 0: # 방문해서 갔는데 가리키고 있는 node가 없다면?
    #                 stack.pop() # 스택에서 빼버린다.
    #             #     print('stack : {}'.format(stack))
    #             # print('pos : {}'.format(pos))
    #             print(len(matrix[stack[-1]]))
    #             for j in range(len(matrix[stack[-1]])): # 가리키고 있는 node 탐색, 가리키고 있는 node가 없다면(길이가 0이라면) 돌지 않는다.
    #                 if visited[matrix[stack[-1]][j]] == 0: # 만약 아직 방문하지 않은 node라면?
    #                     visited[matrix[stack[-1]][j]] = 1 # 방문 완료
    #                     stack.append(matrix[stack[-1]][j]) # 스택에 추가
    #                     break # 탈출
    #
    #             if visited[stack[-1]] == 1:
    #                 stack.pop()
    # #
    #
    # print('ans_list : {}'.format(ans_list))
            # print('stack : {}'.format(stack))
            # print('ans_list in {}'.format(pos))
            # print('ans_list : {}'.format(ans_list))
            # if len(matrix[pos]) == 0: # 가리키고 있는 node가 없을 경우 stack에서 pop.
            #     stack.pop()
            #     # print('stack : {}'.format(stack))
            #     if len(stack) != 0:
            #         pos = stack[-1]
            # for j in range(len(matrix[pos])): # 가리키고 있는 node 탐색.
            #     if visited[matrix[pos][j]] != 1:
            #         visited[matrix[pos][j]] = 1
            #         # print('visited : {}'.format(visited))
            #         if matrix[pos][j] not in ans_list:
            #             ans_list.append(matrix[pos][j])
            #         # print('ans_list in {}'.format(matrix[pos][j]))
            #         # print('ans_list : {}'.format(ans_list))
            #         stack.append(matrix[pos][j])
            #         # print('stack : {}'.format(stack))
            #         break
            #     # elif visited[matrix[pos][j]] == 1:
            #     #     stack.pop()
            #         # print('stack : {}'.format(stack))
            #
            # if len(stack) == 0:
            #     break


        # while len(stack) > 0:
        #     pos = stack[-1]
        #     if len(matrix[pos]) > 0:
        #         for k in range(matrix[pos]):
        #             if visited[matrix[pos][k]] != 1:
        #                 stack.append(matrix[pos][k])
        #                 visited[matrix[pos][k]] = 1
        #     else:
        #         stack.pop()
        #     # if len(matrix[pos]) > 0:






    # for
    # print(matrix)
    # print(line_list)
    # matrix = [[0]]*v
    # print(matrix)
    # for j in range(len(line_list)):
    #     matrix[line_list[j][0]].append(line_list[j][1])
    #     if 0 in matrix[line_list[j]]:
    #         matrix[line_list[j]].remove(0)
    # print(matrix)


    # for j in range(v+1):
    #     temp = [0]*v
    #     matrix.append(temp)
    # for j in range(e):
    #     row, col = map(int, input().split())
    #     matrix[row-1].append(col)
    #     if 0 in matrix[row]:
    #         matrix[row].remove(0)
    # print(matrix)
    # while True:











# import sys
# sys.stdin = open('작업순서_input.txt', 'r')
#
# for i in range(1, 11):
#     v, e = map(int, input().split())
#     line_list = list(map(int, input().split()))
#
#     dot_list, target_list = [], []
#     for j in range(len(line_list) // 2):
#         stack_list.append()
#         dot_list.append(line_list[j*2])
#         target_list.append(line_list[(j*2)+1])
#
#     stack_list, complete_list = [], []
#     target = 0
#     visited = [False] * v
#     for j in range(1, len(list(range(v)))+1):
#         if j not in target_list and j not in stack_list:
#             stack_list.append(j)
#             target = stack_list[-1]
#             for k in range(0, len)
#
#     while len(stack_list) > 0:












# for i in range(1, 11):
#     v, e = map(int,input().split())
#     line_list = list(map(int, input().split()))
#     line_list2 = []
#     target_list = []
#     dot_list = []
#     complete_list = []
#     for j in range(len(line_list) // 2):
#         temp = []
#         temp.append(line_list[j*2])
#         dot_list.append(line_list[j*2])
#         temp.append(line_list[(j*2)+1])
#         target_list.append(line_list[(j*2)+1])
#         line_list2.append(temp)
#     # print(line_list2)
#     stack_list = []
#     visited = [False] * v
#     for j in range(0, len(line_list2)):
#         if line_list2[j][0] not in target_list and line_list2[j][0] not in complete_list:
#             # print(line_list2[j][0])
#             visited[line_list2[j][0]-1] = True
#             complete_list.append(line_list2[j][0])
#             stack_list.append(line_list2[j][0])
#
#             while len(stack_list) > 0:
#                 visit = stack_list[-1] # stack의 맨 마지막 지점이 방문지. 여기서 다음 방문지를 찾아본다.
#                 for j in range(len(line_list2)):
#                     # result = True
#                     if visit == line_list2[j][0]: # 위치가 현재 목적지일때,\
#                         result = True
#                         for k in range(len(line_list2)): # 반복문을 돌아 다음 목적지의 선행작업이 모두 완수되었는지 체크
#                             if line_list2[j][1] == line_list2[k][1]:
#                                 if line_list2[k][0] not in complete_list: # 아직 선행되지 않은 작업이 있다면 break, 다음 목적지로 쓸 수 없다.
#                                     result = False
#                                     break
#                         if result: # 모든 선행작업이 완료되었다면
#                             visited[line_list2[j][1]-1] = True
#                             stack_list.append(line_list2[j][1])
#                         else:
#                             stack_list.pop()
#                             break
#
#     print(complete_list)















