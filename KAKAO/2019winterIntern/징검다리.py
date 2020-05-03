def solution(stones, k):
    answer = 0
    ans = stones[0:k]
    compare = stones[0:k]
    for s in range(0, len(stones)-k):
        print(compare)
        cpr = compare.pop(0)
        compare.append(stones[s+k])
        print(ans)
        print()
        if max(ans) > max(compare):
            ans = compare
            answer = max(compare)
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))