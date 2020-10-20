n, m = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]

directions = [
    [[0, 1], [-1, 0]],
    [[0, 1], [1, 0]],
    [[1, 0], [0, -1]],
    [[0, -1], [-1, 0]]
]

answer = 0

def in_range(i, j, direction):
    x1, y1 = direction[0]
    x2, y2 = direction[1]

    if 0 <= i + x1 < n and 0 <= j + y1 < m and 0 <= i + x2 < n and 0 <= j + y2 < m:
        return True

    return False

for i in range(n):
    for j in range(m):
        center = trees[i][j]
        for direction in directions:
            x1, y1 = direction[0]
            x2, y2 = direction[1]
            if in_range(i, j, direction):
                strength = (center*2) + trees[x1][y1] + trees[x2][y2]
                answer = max(answer, strength)

print(answer)

print(36000000000 ** 2)

'''
3 3
32 83 75
24 96 56
71 88 12

632
'''

'''
2 3
7 5 4
3 2 9

45


'''