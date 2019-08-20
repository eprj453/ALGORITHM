import sys
sys.stdin = open('작업순서_input.txt', 'r')

for i in range(1, 11):
    v, e = map(int, input().split())
    line_list = list(map(int, input().split()))

    dot_list, target_list = [], []
    for j in range(len(line_list) // 2):
        dot_list.append(line_list[j*2])
        target_list.append(line_list[(j*2)+1])







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















