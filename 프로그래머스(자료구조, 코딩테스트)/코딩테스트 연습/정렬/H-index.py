def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for c in range(len(citations)):
        if c+1 > citations[c]:
            return c
    return answer



print(solution([3, 3, 3, 3, 3]))