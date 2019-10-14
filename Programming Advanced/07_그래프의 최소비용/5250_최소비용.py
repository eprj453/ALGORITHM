import sys
sys.stdin = open('5250_input.txt', 'r')

def min_fare(q):
    global min_distance
    new_q = []
    min_val = 1000

    for k in range(len(q)):
        x, y, z = q[k][0], q[k][1], q[k][2]
        if x == n-1 and y == n-1:
            min_distance = min(min_distance, z)
            return
        for l in range(len(dx)):
            if 0 <= x + dx[l] < n and 0 <= y + dy[l] < n:
                if maps[x+dx[l]][y+dy[l]] - maps[x][y] < min_val:
                    min_val = maps[x+dx[l]][y+dy[l]] - maps[x][y]
    print('min_val : ', min_val)
    for k in range(len(q)):
        x, y, z = q[k][0], q[k][1], q[k][2]
        for l in range(len(dx)):
            if 0 <= x+dx[l] < n and 0 <= y + dy[l] < n:
                if maps[x+dx[l]][y+dy[l]] - maps[x][y] <= min_val and [x+dx[l], y+dy[l], z+1+min_val] not in new_q:
                    new_q.append([x+dx[l], y+dy[l], z+1+min_val])
                elif maps[x][y] == maps[x+dx[l]][y+dy[l]] and [x+dx[l], y+dy[l], z+1] not in new_q:
                    new_q.append([x+dx[l], y+dy[l], z+1])
    print(new_q)
    min_fare(new_q)
    # global min_distance
    # if d >= (n-1) * 2:
    #     min_distance = min(min_distance, z)
    #     return
    # p_val = maps[x][y]
    # min_val = 1000
    # t_x, t_y = 0, 0
    # for k in range(len(dx)):
    #     if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
    #         if maps[x+dx[k]][y+dy[k]] - p_val < min_val:
    #             min_val = maps[x+dx[k]][y+dy[k]] - p_val
    #             t_x, t_y = x+dx[k], y+dy[k]
    # for k in range(len(dx)):
    #     if 0 <= x+dx[k] < n and 0 <= y + dy[k] < n:
    #         if p_val >= maps[x+dx[k]][y+dy[k]] :
    #             min_fare(t_x)
    # min_fare(t_x, t_y, z+1+min_val, d+1)
    # for k in range(len(dx)):
    #     if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
    #         if maps[x+dx[k]][y+dy[k]] - p_val == min_val:
    #             min_fare(x+dx[k], y+dy[k], z+1+min_val)
    #         # if p_val >= maps[x+dx[k]][y+dy[k]]:
    #             # min_fare(x+dx[k], y+dy[k], z+1)


dx, dy = [0, 1], [1, 0]
for i in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    min_distance = 100 * 100 * 1000
    qq = [[0, 0, 0]]
    min_fare(qq)
    print('#{} {}'.format(i, min_distance))