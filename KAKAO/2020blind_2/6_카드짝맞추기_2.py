dists = [(0 ,1), (1, 0), (0, -1), (-1, 0)]

def get_ctl_dest(board, d, start):
    x, y = start
    dx, dy = d

    i = 0
    while i < 4:

        if 0 <= x < 4 and 0 <= y < 4:
            if [x, y] != start and board[x][y] != 0:
                return x, y

        if 0 <= x + dx < 4 and 0 <= y + dy < 4:
            x += dx
            y += dy
        else:
            break

        i += 1

    return x, y


def get_min_press(board, start, target):
    tx, ty = target
    sx, sy = start

    dijk = [[0xffffff] * 4 for _ in range(4)]
    dijk[sx][sy] = 0

    q = [start]

    while q:
        # print(q)
        x, y = q.pop()
        for d in dists:
            dx, dy = d
            if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                if dijk[x+dx][y+dy] > dijk[x][y] + 1:
                    dijk[x+dx][y+dy] = dijk[x][y] + 1
                    q.append([x+dx, y+dy])

            ctl_x, ctl_y = get_ctl_dest(board, d, [x, y])
            # print('d ', d)
            # print('ctl_x, ctl_y', ctl_x, ctl_y)
            # print()
            if dijk[ctl_x][ctl_y] > dijk[x][y] + 1:
                dijk[ctl_x][ctl_y] = dijk[x][y] + 1
                q.append([ctl_x, ctl_y])

    return dijk[tx][ty]+1

print(
    get_min_press(
        [[1,0,0,0],[0,0,0,0],[0,0,0,2],[0,0,1,0]],
        [0, 0],
        [3, 2]
    )
)