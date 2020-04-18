def solution(office, r, c, move):
    answer = 0
    moveX, moveY = [-1, 0, 1, 0], [0, -1, 0, 1]
    v, h = len(office[0]), len(office)
    visited = [[False] * v for _ in range(h)]
    position, d = [r, c], 0
    answer += office[r][c]
    visited[r][c] = True
    for m in move:
        if m == 'go':
            x, y = position[0], position[1]
            dx, dy = x + moveX[d], y + moveY[d]
            if 0 <= dx < h and 0 <= dy < v:
                if office[dx][dy] == -1 : continue
                position = [dx, dy]
                if not visited[dx][dy]:
                    print(dx,dy)
                    visited[dx][dy] = True
                    answer += office[dx][dy]
        elif m == 'left':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
    return answer

print(solution([[5,-1,4],[6,3,-1],[2,-1,1]], 1, 0, ['go','go','right','go','right','go','left','go']))