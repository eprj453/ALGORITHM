# import heapq
# # def solution(n, works):
# #     answer = 0
# #     heap = []
# #     for work in works:
# #         heapq.heappush(heap, (-work, work))
# #     # heapq._heapify_max(works)
# #     # print(heap)
# #     for _ in range(n):
# #         maxWork = heapq.heappop(heap)
# #         # print(maxWork)
# #         if maxWork[1] == 0: break
# #         afterWork = maxWork[1]-1
# #         heapq.heappush(heap, (-afterWork, afterWork))
# #
# #     for work in heap:
# #         answer += (work[1]**2)
# #     return answer
# #
# # print(solution(4, [4,3,3]))
# # print(solution(3, [1,1]))

# def solution(tickets):
#     answer = []
#     ticket_dict = {}
#     for ticket in tickets:
#         flight, arrival = ticket[0], ticket[1]
#         ticket_dict[flight] = ticket_dict.get(flight, []) + [arrival]
#         ticket_dict[flight].sort()
#     stk = ['ICN']
#     while stk:
#         flight = stk[-1]
#         arrival = ticket_dict.get(flight)
#         if arrival:
#             stk.append(arrival[0])
#             arrival.pop(0)
#         else:
#             answer.append(stk.pop())
#     print(answer)
#     return list(reversed(answer))
# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
# from collections import deque
# # dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# # answer = 10000
# # def bfs(q, n, m, maps):
# #     global answer
# #     while q:
# #         x, y, visited, distance = q[0][0], q[0][1], q[0][2], q[0][3]
# #         # print(distance)
# #         for k in range(4):
# #             kx, ky = dx[k], dy[k]
# #             if kx == n - 1 and ky == m - 1:
# #                 answer = min(answer, distance + 1)
# #                 return
# #             if 0 <= kx < n and 0 <= ky < m and maps[kx][ky] == 1 and visited[kx][ky] == False:
# #                 visited[kx][ky] = True
# #                 q.append([kx, ky, visited, distance + 1])
# #                 bfs(q, n, m, maps)
# #                 visited[kx][ky] = False
# #         q.popleft()
# # def solution(maps):
# #     global answer
# #     n, m = len(maps), len(maps[0])
# #     print(n, m)
# #     visited = [[False] * m for _ in range(n)]
# #     visited[0][0] = True
# #     q = deque()
# #     q.append([0, 0, 1, visited])
# #     # bfs(q, n, m, maps)
# #     # print(q)
# #     while q:
# #         # print(q)
# #         x, y, distance, visit = q[0][0], q[0][1], q[0][2], q[0][3]
# #         # print(distance)
# #         for k in range(4):
# #             kx, ky = x+dx[k], y+dy[k]
# #             if kx == n - 1 and ky == m - 1:
# #                 # print('change')
# #                 answer = min(answer, distance + 1)
# #             if 0 <= kx < n and 0 <= ky < m and maps[kx][ky] == 1 and visit[kx][ky] == False:
# #                 # print('true')
# #                 visit[kx][ky] = True
# #                 q.append([kx, ky, distance+1, visit])
# #                 # visit[kx][ky] = False
# #         q.popleft()
# #     return answer
# #
# # print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))



# def goTravel(k, travel, start, totalMoney, totalTime):
#     global ans
#     if totalTime > k: return
#
#     if start == len(travel):
#         if totalTime <= k:
#             ans = max(totalMoney, ans)
#         return
#
#     t = travel[start]
#     print(t)
#     walkTime, walkMoney, bikeTime, bikeMoney = t[0], t[1], t[2], t[3]
#     if walkTime + totalTime <= k:
#         goTravel(k, travel, start+1, totalMoney+walkMoney, totalTime+walkTime)
#     if bikeTime + totalTime <= k:
#         goTravel(k, travel, start + 1, totalMoney + bikeMoney, totalTime + bikeTime)
# import copy
# def solution(K, travel):
#     answer = 0
#     # goTravel(K, travel, 0, 0, 0)
#     n = 1
#     canGo = [[travel[0][0], travel[0][1]], [travel[0][2], travel[0][3]]]
#     while n < len(travel):
#         next = []
#         print(canGo)
#         walkTime, walkMoney, bikeTime, bikeMoney = travel[n][0], travel[n][1], travel[n][2], travel[n][3]
#         for go in canGo:
#             totalTime, totalMoney = go[0], go[1]
#             if walkTime + totalTime <= K:
#                 next.append([walkTime + totalTime, walkMoney + totalMoney])
#             if bikeTime + totalTime <= K:
#                 next.append([bikeTime + totalTime, bikeMoney + totalMoney])
#         canGo = next.copy()
#         if not canGo: break
#         n += 1
#
#     canGo.sort(reverse=True, key=lambda x : x[1])
#     return canGo[0][1]
#
# # print(solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))
#
# print(solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]))

# ope_dict = {
#     '(' : 1,
#     '+' : 2,
#     '*' : 3,
# }
# for i in range(1, 11):
#     n = int(input())
#     formula = input()
#     postfix = []
#     stk= []
#     answer = 0
#     for f in formula:
#         if f.isdigit(): # 숫자라면
#             postfix.append(f)
#         else:
#             if not stk: # 스택에 아무것도 없으면
#                 stk.append(f)
#             elif f == '(':
#                 stk.append(f)
#             elif f == ')':
#                 while stk:
#                     ope = stk.pop()
#                     if ope == '(': break
#                     else:
#                         postfix.append(ope)
#             else:
#                 while stk:
#                     if ope_dict[f] <= ope_dict[stk[-1]]:
#                         postfix.append(stk.pop())
#                     if not stk or ope_dict[f] > ope_dict[stk[-1]]:
#                         stk.append(f)
#                         break
#     while stk:
#         postfix.append(stk.pop())
#
# x`    for f in postfix:
#         if f.isdigit(): stk.append(int(f))
#         else:
#             result = 0
#             ope1 = int(stk.pop())
#             ope2 = int(stk.pop())
#             if f == '*':
#                 result = ope1 * ope2
#             else:
#                 result = ope1 + ope2
#             stk.append(result)
#         answer = stk[-1]
#     print('#{} {}'.format(i, answer))

print((1, 2)[0])

