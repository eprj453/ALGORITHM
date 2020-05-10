from collections import deque
#
#
# def solution(customer, K):
#     answer = []
#     wait = []
#     customer_dict, wait_dict, room_dict = {}, {}, {}
#     for c in customer:
#         customer_id, request = c[0], c[1]
#         if request == 1:  # 방 예약
#             if len(answer) < K:  # 남은 방 있을 경우
#                 room_dict[customer_id] = 1
#             else:
#                 wait.append(customer_id)
#         else:  # 예약 취소
#             if customer_id in answer:
#                 answer.remove(customer_id)
#                 if wait:  # 대기 손님 있을 경우
#                     answer.append(wait.pop(0))
#             else:
#                 wait.remove(customer_id)
#
#     return sorted(answer)

from queue import PriorityQueue
# import time
# def solution(customer, K):
#     answer = []
#     wait, room = PriorityQueue(), []
#     for c in customer:
#         customer_id, request = c[0], c[1]
#         if request == 1:  # 방 예약
#             if len(room) < K:
#                 room.append(customer_id)
#             else:
#                 wait.put((time.time(), customer_id))
#         else:  # 예약 취소
#             if customer_id in room:
#                 room.remove(customer_id)
#             else:
#
#     return sorted(room)

# print(solution([[4, 1], [3, 1], [2, 1], [4, 0], [1, 1], [1, 0], [4, 1], [4, 0]], 3))
# print(solution([[2, 1], [3, 1], [4, 1], [3, 0], [1, 1], [2, 0], [4, 0], [2, 1]], 3))
# print(solution([[3, 1], [4, 1], [4, 0], [3, 0], [2, 1], [1, 1]], 2))
# print(solution([[2, 1], [1, 1], [3, 1], [1, 0], [1, 1], [2, 0], [2, 1]], 1))

# di = {
#     1: 1,
#     2: 1,
#     3: 1,
#
# }
# print(sorted(di))
#
# d = deque()
# d.append(1, 2, 3)
# d.

d = PriorityQueue()
d.put((1, 'a'))
d.put((2, 'b'))
d.put((3, 'c'))
print(d.get_nowait())