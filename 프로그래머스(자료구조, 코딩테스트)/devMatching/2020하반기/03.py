def solution(n, groups):
    answer = 0
    group_dict = {}
    for group in groups:
        s, e = group
        group_dict[s] = max(group_dict.get(s, 0), e)

    start = 1
    while start < n:
        max_dist = start+1
        dist = group_dict.get(start)
        for light in range(start, max_dist+1):
            max_dist = max(group_dict.get(light, 0), max_dist)
        start = max_dist
        answer += 1
    return answer


print(solution(10, [[1, 5],[2, 7],[4, 8],[3, 6]]))
print(solution(100, [[1, 50],[1,100],[51, 100 ]]))
print(solution(7, [[6, 7],[1, 4],[2, 4]]))