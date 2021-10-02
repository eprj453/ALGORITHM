import heapq




# class Food:
#     def __init__(self, i ,x):
#         self.i = i
#         self.x = x
#
#
#     def __lt__(self, other):
#         if self.x < other.x:
#             return True
#         elif self.x == other.x:
#             return self.i > other.i
#         else:
#             return False

def solution(food_times, k):
    answer = -1

    hq = []
    heapq.heapify(hq)
    for i, food_time in enumerate(food_times):
        heapq.heappush(hq, (food_time, i+1))
    #
    # while hq:
    #     print(heapq.heappop(hq))
    while hq:
        # total_food_count = len(hq)

        current_food = heapq.heappop(hq)
        left_food_count = len(hq)
        food_time_for_this_food, food_index = current_food
        if k > (left_food_count * food_time_for_this_food):
            print(k)

            k -= (left_food_count * food_time_for_this_food)
        else:
            return food_index

    return answer



print(solution([8,6,4],15))