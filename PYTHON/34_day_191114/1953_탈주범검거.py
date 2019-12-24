from collections import deque
import sys
sys.stdin = open('1953_input.txt', 'r')
def bfs(q, cnt):
    global can_go

    if cnt == l-1:
        return
    new_q = []
    while q:
        x, y = q[0][0], q[0][1]
        num = maps[x][y]
        dir = road_dict[num]
        dx, dy = dir[0], dir[1]
        # print(dx, dy)
        for k in range(len(dx)):
            # print(dx[k], dy[k])
            if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
                if maps[x+dx[k]][y+dy[k]] != 0 and visited[x+dx[k]][y+dy[k]] == False:
                    target_dict = road_dict[maps[x + dx[k]][y + dy[k]]]
                    for d in range(len(target_dict[0])):
                        if target_dict[0][d] == (dx[k] * -1) and target_dict[1][d] == (dy[k] * -1):
                            new_q.append([x+dx[k], y+dy[k]])
                            visited[x + dx[k]][y + dy[k]] = True
                            can_go += 1
        q.pop(0)

    bfs(new_q, cnt+1)


road_dict = {
    1: [(0, 1, 0, -1), (1, 0, -1, 0)],
    2: [(-1, 1), (0, 0)],
    3: [(0, 0), (1, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(0, 1), (-1, 0)],
    7: [(0, -1), (-1, 0)],
    }

for i in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    q = [[r, c]]
    visited[r][c] = True
    can_go = 1
    bfs(q, 0)
    print('#{} {}'.format(i, can_go))
    # visited[r][c] = True
    # # print(visited)
    # cnt = 1
    # while q:
    #     print(q)
    #     t = q.popleft()
    #     x, y = t[0], t[1]
    #     # print('x, y', x, y)
    #     dx, dy = road_dict[maps[x][y]][0], road_dict[maps[x][y]][1]
    #     # print(dx, dy)
    #     # print()
    #     for k in range(len(dx)):
    #         if 0 <= x+dx[k] < n and 0 <= y + dy[k] < m:
    #             if maps[x+dx[k]][y+dy[k]] == 0:
    #                 continue
    #             elif maps[x+dx[k]][y+dy[k]] != 0 and visited[x+dx[k]][y+dy[k]] == False:
    #                 print([(dx[k] * -1), (dy[k] * -1)])
    #                 if [(dx[k] * -1), (dy[k] * -1)] in road_dict[maps[x+dx[k]][y+dy[k]]]:
    #                     q.append([x+dx[k], y+dy[k]])
    #                     visited[x+dx[k]][y+dy[k]] = True
    #                     cnt += 1
    # # for j in range(n):
    # #     print(visited[j])
    # # print()
    # print(cnt)




