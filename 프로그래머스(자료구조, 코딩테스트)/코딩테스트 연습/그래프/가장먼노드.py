from collections import deque
def solution(n, edge):
    answer = 0
    max_distance = 0
    connected = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for e in edge:
        a,b = e[0], e[1]
        connected[a].append(b)
        connected[b].append(a)

    q = []
    q.append([1, 0])
    visited[1] = True
    while q:
        node, distance = q[0][0], q[0][1]
        for c in connected[node]:
            if not visited[c]:
                visited[c] = True
                q.append([c, distance+1])
                if distance+1 > max_distance:
                    answer = 1
                    max_distance = distance+1
                elif distance + 1 == max_distance:
                    answer += 1
        q.pop(0)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))