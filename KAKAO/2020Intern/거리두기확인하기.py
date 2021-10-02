dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(arr, coop):

    visited = [[False] * 5 for _ in range(5)]
    visited[coop[0]][coop[1]] = True

    q = [(coop[0], coop[1], 0)]

    while q:
        x, y, distance = q.pop(0)
        if [x, y] != coop and arr[x][y] == 'P':
            return False

        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < 5 and 0 <= dy < 5 and not visited[dx][dy] and arr[dx][dy] != 'X':
                if distance + 1 < 3:
                    q.append((dx, dy, distance+1))
                    visited[dx][dy] = True

    return True


def is_keep_distance(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                print(i, j)
                result = dfs(place, [i, j])
                if not result:
                    return 0

    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(is_keep_distance(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))