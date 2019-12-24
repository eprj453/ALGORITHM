n, m = map(int, input().split())
r, c, d = map(int, input().split())
visited, maps = [], []
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x = 0

for _ in range(n):
    maps.append(list(map(int, input().split())))
    temp = [False] * m
    visited.append(temp)

visited[r][c] = True
clean_count = 1

while True:
    can_spin = False
    for i in range(4):
        left = (d - i + 3) % 4
        if not visited[r+dx[left]][c+dy[left]] and maps[r+dx[left]][c+dy[left]] == 0:
            visited[r + dx[left]][c + dy[left]] = True
            r, c, d = r+dx[left], c+dy[left], left
            can_spin = True
            clean_count += 1
            break

    can_back = False
    if can_spin == False:
        back = (d+2) % 4
        if maps[r+dx[back]][c+dy[back]] == 0:
            can_back = True
            visited[r+dx[back]][c+dy[back]] = True
            r, c, d = r+dx[back], c+dy[back], d

    if can_spin == False and can_back == False:
        break

print(clean_count)

