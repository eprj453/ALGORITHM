# n = int(input())
#
# house = [list(input()) for _ in range(n)]
#
# visited = [[False]*(n+2) for _ in range(n+2)]
# # print(len(visited))
# for i in range(n+2):
#     if i == 0 or i == n+1:
#         house.insert(i,['0'] * (n+2))
#     else:
#         house[i].insert(0,'0')
#         house[i].insert(n+2,'0')
#
# #
# # print(visited)
# # print(house)
#
# q = []
# ans = []
# dx, dy = [-1, 1, 0, 0], \
#         [0, 0, -1, 1]
#
# for i in range(1, n+2): # 1, 8 1부터 7까지
#     for j in range(1, n+2): # 상동
#         count = 0
#         if house[i][j] == '1' and visited[i][j] == False:
#             # print('{}, {} false'.format(i,j))
#             q.append([i, j])
#             # print('{} {} in q'.format(i,j))
#             visited[i][j] = True
#             count += 1
#             while len(q) > 0:
#                 # print('q : {}'.format(q))
#                 # print(q[0][1])
#                 for k in range(len(dx)):
#                     # print(visited[q[0][0] + dx[k]][q[0][1] + dy[k]])
#                     # print('check', q[0][0] + dx[k],q[0][1]+ dy[k])
#                     if house[q[0][0] + dx[k]][q[0][1] + dy[k]] == '1' and visited[q[0][0] + dx[k]][q[0][1] + dy[k]] == False:
#                          q.append([q[0][0] + dx[k], q[0][1]+ dy[k]])
#                          visited[q[0][0] + dx[k]][q[0][1] + dy[k]] = True
#                          count += 1
#                 q.pop(0)
#             ans.append(count)
#
# print(len(ans))
# for i in ans:
#     print(i)

n = int(input())

house = [list(input()) for _ in range(n)]

visited = [[False]*(n+2) for _ in range(n+2)]

for i in range(n+2):
    if i == 0 or i == n+1:
        house.insert(i,['0'] * (n+2))
    else:
        house[i].insert(0,'0')
        house[i].insert(n+2,'0')

q = []
ans = []
dx, dy = [-1, 1, 0, 0], \
        [0, 0, -1, 1]

for i in range(1, n+2):
    for j in range(1, n+2):
        count = 0
        if house[i][j] == '1' and visited[i][j] == False:
            q.append([i, j])
            visited[i][j] = True
            count += 1
            while len(q) > 0:
                for k in range(len(dx)):
                    if house[q[0][0] + dx[k]][q[0][1] + dy[k]] == '1' and visited[q[0][0] + dx[k]][q[0][1] + dy[k]] == False:
                         q.append([q[0][0] + dx[k], q[0][1]+ dy[k]])
                         visited[q[0][0] + dx[k]][q[0][1] + dy[k]] = True
                         count += 1
                q.pop(0)
            ans.append(count)
ans.sort()

print(len(ans))
for i in ans:
    print(i)
