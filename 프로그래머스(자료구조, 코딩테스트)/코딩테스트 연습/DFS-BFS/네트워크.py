def solution(n, computers):
    answer = 0
    visited = [False] * n
    connected = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                connected[i][j] = True
                connected[j][i] = True

    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            q = [i]
            while q:
                c = q[-1]
                for j in range(len(connected[c])):
                    if connected[c][j] and not visited[j]: # 연결되어있다면
                        q.append(j)
                        visited[j] = True
                        break
                else:
                    q.pop()
    return answer

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1,1,0], [1,1,1], [0,1,1]]))