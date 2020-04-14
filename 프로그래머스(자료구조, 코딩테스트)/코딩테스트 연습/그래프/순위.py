def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    for result in results:
        a, b = result[0], result[1]
        win[a].append(b)
        lose[b].append(a)
    print(win)
    print(lose)
    for a in range(1, n+1):
        cnt = 1
        visited = [False] * (n+1)
        win_q, lose_q = [a], [a]
        while win_q:
            for i in win[win_q[0]]:
                if not visited[i]:
                    visited[i] = True
                    win_q.append(i)
                    cnt += 1
            win_q.pop(0)

        while lose_q:
            for i in lose[lose_q[0]]:
                if not visited[i]:
                    visited[i] = True
                    lose_q.append(i)
                    cnt += 1
            lose_q.pop(0)

        if cnt == n:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))