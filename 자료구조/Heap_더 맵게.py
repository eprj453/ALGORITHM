import heapq
def solution(scoville, K):
    answer = 0
    isCan = False
    heapq.heapify(scoville)
    while scoville:
        minScoville = heapq.heappop(scoville)
        if len(scoville) == 0 or minScoville >= K:
            isCan = True
            break
        else:
            if scoville:
                nextMinScoville = heapq.heappop(scoville)
                newScoville = minScoville + (nextMinScoville * 2)
                heapq.heappush(scoville, newScoville)
                answer += 1
    return answer if isCan else -1

print(solution([1, 2, 3, 9, 10, 12], 7))