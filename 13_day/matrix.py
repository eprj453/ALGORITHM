import sys
sys.stdin = open('matrix_input.txt', 'r')

t = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(1, t+1):
    visited, ans, q = [], [], []
    n = int(input())
    matrix = [list(input().split()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]


    for j in range(n):
        for k in range(n):
            if matrix[j][k] != '0' and visited[j][k] == False:
                q.append([j, k])
                visited[j][k] = True
                temp = []
                temp.append([j, k])
                while len(q) > 0:
                    for l in range(len(dx)):
                        if q[0][0] + dx[l] >= 0 and q[0][0] + dy[l] < n and q[0][1] + dy[l] >= 0 and q[0][1] + dy[l] < n:
                            if matrix[q[0][0]+dx[l]][q[0][1]+dy[l]] != '0' and visited[q[0][0]+dx[l]][q[0][1]+dy[l]] == False:
                                q.append([q[0][0] + dx[l], q[0][1] + dy[l]])
                                visited[q[0][0] + dx[l]][q[0][1] + dy[l]] = True
                                temp.append([q[0][0]+dx[l], q[0][1]+dy[l]])
                    q.pop(0)
                ans.append([((temp[-1][0] - temp[0][0] + 1)*(temp[-1][1] - temp[0][1] + 1)), temp[-1][0] - temp[0][0] + 1, temp[-1][1] - temp[0][1] + 1])
    ans.sort()
    print(ans)
    # print('#{} {}'.format(i, len(ans)), end = ' ')
    # for j in range(len(ans)):
    #     print('{} {}'.format(ans[j][1], ans[j][2]), end = ' ')
    # print()
