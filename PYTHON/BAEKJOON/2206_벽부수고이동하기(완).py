from queue import PriorityQueue
from pprint import pprint
n, m = list(map(int, input().split()))
# print(n, m)
map_arr = []
for i in range(n):
    map_arr.append(list(input()))
# print(map_arr)
start = [0, 0]

dijk = []
for _ in range(n):
    temp = []
    for _ in range(m):
        temp.append([1000*1000, 1000*1000]) # 벽을 아직 안부쉈을때 / 부쉈을때
    dijk.append(temp)

dijk[0][0] = [1, 1]



# queue = PriorityQueue()
#
# queue.put((0, 0, 0, 0)) # 거리, 벽 부쉈는지 여부, 위치 x, 위치 y
# queue = []
# queue.append((0, 0, 0)) # 부쉈는지 여부, 위치
#
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# while queue:
#     # print(queue)
#     # for d in dijk:
#     #     print(d)
#     # print()
#     crushed, x, y = queue.pop(0)
#     if crushed: # 이미 벽을 부순 경우
#         for d in directions:
#             dx, dy = d
#             if 0 <= xdx < n and 0 <= ydy < m:
#                 if map_arr[xdx][ydy] == '0' and dijk[xdx][ydy][1] > dijk[x][y][1] + 1:
#
#                     dijk[x + dx][y + dy][1] = dijk[x][y][1] + 1
#                     queue.append((1, xdx, ydy))
#
#     else: # 아직 벽 안부순 경우
#         for d in directions:
#             dx, dy = d
#             if 0 <= x + dx < n and 0 <= y + dy < m:
#                 if map_arr[xdx][ydy] == '0' and dijk[x + dx][y + dy][0] > dijk[x][y][0] + 1:
#                     dijk[x + dx][y + dy][0] = dijk[x][y][0] + 1
#                     queue.append((0, x + dx, y + dy))
#
#                 if map_arr[x + dx][y + dy] == '1' and dijk[x + dx][y + dy][1] > dijk[x][y][1] + 1:
#                     dijk[x + dx][y + dy][1] = dijk[x][y][1] + 1
#                     queue.append((1, x + dx, y + dy))

queue = PriorityQueue()
# queue = []
queue.put((0, 0, 0)) # 부쉈는지 여부, 위치

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while not queue.empty():
    # print(queue)
    # for d in dijk:
    #     print(d)
    # print()
    crushed, x, y = queue.get(0)
    if crushed: # 이미 벽을 부순 경우
        for d in directions:
            dx, dy = d
            xdx, ydy = x + dx, y + dy
            if 0 <= xdx < n and 0 <= ydy < m:
                if map_arr[xdx][ydy] == '0' and dijk[xdx][ydy][1] > dijk[x][y][1] + 1:

                    dijk[x + dx][y + dy][1] = dijk[x][y][1] + 1
                    queue.put((1, xdx, ydy))

    else: # 아직 벽 안부순 경우
        for d in directions:
            dx, dy = d
            xdx, ydy = x + dx, y + dy
            if 0 <= xdx < n and 0 <= ydy < m:
                if map_arr[xdx][ydy] == '0' and dijk[xdx][ydy][0] > dijk[x][y][0] + 1:
                    dijk[xdx][ydy][0] = dijk[x][y][0] + 1
                    queue.put((0, xdx, ydy))

                if map_arr[xdx][ydy] == '1' and dijk[xdx][ydy][0] > dijk[x][y][0] + 1:
                    # print('pick')
                    dijk[xdx][ydy][1] = dijk[x][y][0] + 1
                    queue.put((1, xdx, ydy))

    # for d in dijk:
    #     print(d)
    # print()
    # print(queue)

# pprint(dijk)
# for d in dijk:
#     print(d)
answer = min(dijk[n-1][m-1])
print(answer if answer != 1000*1000 else -1)

# for d in dijk:
#     print(d)
'''
6 5
00000
00000
00111
00000
11100
00000

'''