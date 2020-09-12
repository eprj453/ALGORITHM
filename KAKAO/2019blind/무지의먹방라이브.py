from queue import PriorityQueue
import heapq
def solution(food_times, k):
    hq = []
    answer = 0
    heapq.heapify(hq)
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i+1))
    # print(hq)

    pre = 0
    remain = k
    length = len(hq)
    sum_value = 0
    while sum_value + (((hq[0][0]) - pre) * length):
        


    hq.sort(key=lambda x:x[1])
    print(hq)
    print()
    return hq[(remain % len(hq))][1]

# print(solution([3,1,2], 5))
# print(solution([8,6,9,5,2,2], 12))
print(solution([7,9,1,2,5,3], 13))