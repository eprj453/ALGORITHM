import copy
def solution(begin, target, words):
    answer = 50
    visited = dict()
    visited[begin] = True

    q = []
    q.append((begin, visited, 0))
    while q:
        print(q)
        word, visit, dist = q.pop(0)
        if answer < dist:
            continue
        if word == target:
            answer = min(answer, dist)
            continue
        for w in words:
            if not visit.get(w):
                flag = 0
                for x, y in zip(w, word):
                    if x != y:
                        flag += 1
                if flag == 1:
                    visit[w] = True
                    q.append((w, visit, dist + 1))
                    del visit[w]

    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))