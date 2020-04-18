import heapq
def solution(people, limit):
    answer = 0
    heapq.heapify(people)
    boat = 0
    while people:
        person = heapq.heappop(people)


# print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))