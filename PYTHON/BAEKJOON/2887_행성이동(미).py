from itertools import permutations

n = int(input())
planets = []


class Planet:
    def __init__(self, idx, x, y, z):
        self.idx = idx
        self.x = x
        self.y = y
        self.z = z


def get_min_distance(planet1, planet2):
    return min(
        abs(planet1[0] - planet2[0]),
        abs(planet1[1] - planet2[1]),
        abs(planet1[2] - planet2[2])
    )


for i in range(n):
    x, y, z = map(int, input().split(' '))
    planets.append(Planet(i, x, y, z))

answer = float('inf')
for p in list(permutations([0, 1, 2], 3)):
    i, j, k = p
    sorted_planets = sorted(planets, key=lambda x: (x[i], x[j], x[k]))
    print(sorted_planets)
    dist = 0
    for idx in range(n-1):
        dist += get_min_distance(sorted_planets[idx], sorted_planets[idx+1])

    answer = min(answer, dist)

print(answer)