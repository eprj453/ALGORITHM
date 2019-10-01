import sys
sys.stdin = open('1861_input.txt', 'r')
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(1, int(input())+1):
    n = int(input())
    square = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    max_count, max_node = 0, 0
    for j in range(n):
        temp = [False] * n
        visited.append(temp)


    for j in range(n):
        for k in range(n):
            temp_node = 0
            if visited[j][k] == False:
                temp_node = square[j][k]
                visited[j][k] = True
                q = []
                q.append([j, k])
                count = 1
                while q:
                    x, y, = q[0][0], q[0][1]
                    for l in range(len(dx)):
                        if 0 <= x + dx[l] < n and 0 <= y + dy[l] < n:
                            if square[x][y] + 1 == square[x+dx[l]][y+dy[l]]:
                                q.append([x+dx[l], y+dy[l]])
                                visited[x+dx[l]][y+dy[l]] = True
                                count += 1
                    q.pop(0)


                if max_count <= count:
                    max_count = count
                    max_node = min(temp_node, max_node) if count == max_count else max_node

                # if count == max_count:
                #     if temp_node < max_node:
                #         max_node = temp_node

    print('#{} {} {}'.format(i, max_node, max_count))
