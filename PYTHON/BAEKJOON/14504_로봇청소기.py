n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

visited[r][c] = True
clean_count = 1

while True:
    for i in range(4):
        # left = (d - i + 3) % 4
        left = d - i
        print(left)
        rLeft, cLeft = r+dx[left], c+dy[left]
        if not visited[rLeft][cLeft] and maps[rLeft][cLeft] == 0:
            visited[rLeft][cLeft] = True
            r, c, d = rLeft, cLeft, left
            clean_count += 1
            break
    else:
        back = (d+2) % 4
        rBack, cBack = r + dx[back], c + dy[back]
        if maps[rBack][cBack] == 0:
            visited[rBack][cBack] = True
            r, c, d = rBack, cBack, d
        else:
            break

print(clean_count)

