n = int(input())
chars = list(input().split())
start = [1, 1]
dir_dict = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0]
}

for ch in chars:
    dx, dy = dir_dict.get(ch)
    x, y = start[0], start[1]
    if 1 <= x + dx < n and 1 <= y + dy < n:
        start[0] += dx
        start[1] += dy
    print(start)
print(start[0], start[1])