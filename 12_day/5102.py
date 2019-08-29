import sys
sys.stdin = open('5102_input.txt', 'r')

# t = int(input())
# for i in range(1, t+1):
#     v, e = map(int, input().split())
#     link, q = [], []
#     visited = [False] * (v+1)
#     for j in range(v+1):
#         link.append(['0'] * (v+1))
#     for j in range(e):
#         x, y = map(int, input().split())
#         link[x][y] = '1'
#     s, g = map(int, input().split())
#     print(link)
#     q.append([s, 0])
#     visited[s] = True
#     count = 0
#     while len(q) > 0:
#         if count != 0: break
#         for node in range(len(link[q[0][0]])):
#             if link[q[0][0]][node] == '1':
#                 if node == g:
#                     count = q[0][1]+1
#                     break
#                 else:
#                     q.append([node, q[0][1] + 1])
#         q.pop(0)
#
#     print('#{} {}'.format(i, count))
#
#

t = int(input())
for i in range(1, t+1):
    v, e = map(int, input().split())
    link, q = [], []
    visited = [False] * (v+1)
    for j in range(v+1):
        link.append([])
    for j in range(e):
        x, y = map(int, input().split())
        link[x].append(y)
        link[y].append(x)
    print(link)
    s, g = map(int, input().split())
    q.append([s, 0])
    visited[s] = True
    count = 0
    while len(q) > 0:
        if count != 0: break
        for node in link[q[0][0]]:
            if node == g and visited[node] == False:
                count = q[0][1]+1
                break
            if visited[node] == False:
                q.append([node, q[0][1] + 1])
                visited[node] = True
        q.pop(0)

    print('#{} {}'.format(i, count))
