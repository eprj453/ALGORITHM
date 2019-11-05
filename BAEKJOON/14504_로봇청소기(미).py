# from collections import deque
# n, m = map(int, input().split())
# r, c, d = map(int, input().split()) # 1, 1, 0
# maps = [list((input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# f_count = 0
# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
# s = deque()
# s.append([r, c, d])
# f_count += 1
# visited[r][c] = True
# while s:
#     print('돈다')
#     x, y, d2 = s[-1][0], s[-1][1], s[-1][2]
#     result = False
#     print(s)
#     for i in range(len(dx)):
#         if 0 <= x+dx[d2-(i+1)] < n and 0 <= y+dy[d2-(i+1)] < n:
#             print('x, y : ',x+dx[d2-(i+1)], y+dy[d2-(i+1)])
#             if visited[x+dx[d2-(i+1)]][y+dy[d2-(i+1)]] == False and maps[x+dx[d2-(i+1)]][y+dy[d2-(i+1)]] == '0':
#                 result = True
#                 s.append([x+dx[d2-(i+1)], y+dy[d2-(i+1)], (d2+3-i)%4])
#                 visited[x+dx[d2-(i+1)]][y+dy[d2-(i+1)]] = True
#                 f_count += 1
#                 break
#
#     if result == False:
#         d3 = d2 - 2 if d2 >= 2 else d2 + 2
#         if maps[x+dx[d3]][y+dy[d3]] == '0':
#             result = True
#             temp = s.pop()
#             s.append([temp[0]+dx[d3], temp[1]+dx[d3], d2])
#
#     if result == False:
#         break
#     print('f_count :',f_count)
# print(f_count)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
visited, maps = [], []
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x = 0
print((x+3) % 4)
for _ in range(n):
    maps.append(list(map(int, input().split())))
    visited.append([False] * m)
visited[r][c] = True
clean_count = 0
while True:
    left = (d+3) % 4

    if maps[r+dx[left]][c+dy[left]] == 0 and visited[r+dx[left]][c+dy[left]] == False: # 아직 방문 전
        result = True
        r, c, d = r+dx[left], c+dy[left], left
        visited[r+dx[left]][c+dy[left]] = True
        clean_count += 1





'''
r, c >> 청소기 위치 [r,c]

d = 0 > 북쪽 (-1, 0)
d = 1 > 동쪽 (0, +1)
d = 2 > 남쪽 (+1, 0)
d = 3 > 서쪽 (0, -1)
'''