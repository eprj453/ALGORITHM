# import heapq
#
#
# class Boxer:
#     def __init__(self, win_rate, heavier_win_count, weight, number):
#         self.win_rate = win_rate
#         self.heavier_win_count = heavier_win_count
#         self.weight = weight
#         self.number = number
#
#     def __lt__(self, other):
#         if self.win_rate > other.win_rate:
#             return True
#
#         if self.win_rate == other.win_rate:
#             if self.heavier_win_count > other.heavier_win_count:
#                 return True
#
#             if self.heavier_win_count == other.heavier_win_count:
#                 if self.weight > other.weight:
#                     return True
#
#                 if self.weight == other.weight:
#                     return self.number < other.number
#
#         # elif self.heavier_win_count > other.heavier_win_count:
#         #     return True
#         # elif self.weight > other.weight:
#         #     return True
#         # elif self.number < other.number:
#         #     return True
#         # else:
#         #     return False
#
#
# def solution(weights, head2head):
#     answer = []
#     boxer_queue = []
#
#     for idx, info_str in enumerate(head2head):
#         my_weight = weights[idx]
#         win_count, lose_count, heavier_win_count = 0, 0, 0
#
#         for idx2, s in enumerate(info_str):
#             opponent_weight = weights[idx2]
#             if s == 'N': continue
#             if s == 'L':
#                 lose_count += 1
#             else:
#                 if my_weight < opponent_weight:
#                     heavier_win_count += 1
#                 win_count += 1
#
#         win_rate = round(win_count / (win_count + lose_count), 2) if win_count + lose_count > 0 else 0
#         boxer = Boxer(
#             win_rate=win_rate,
#             heavier_win_count=heavier_win_count,
#             weight=my_weight,
#             number=idx+1
#         )
#
#         heapq.heappush(boxer_queue, boxer)
#
#     while boxer_queue:
#         boxer = heapq.heappop(boxer_queue)
#         answer.append(boxer.number)
#
#     return answer


def solution(weights, head2head):
    answer = []

    for boxer_idx, boxer_info in enumerate(head2head):
        my_weight = weights[boxer_idx]
        win_count, lose_count, heavier_win_count = 0, 0, 0
        for op_idx, op_info in enumerate(boxer_info):
            op_weight = weights[op_idx]
            if op_info == 'N': continue

            if op_info == 'L':
                lose_count += 1
            elif op_info == 'W':
                if my_weight < op_weight:
                    heavier_win_count += 1
                win_count += 1
        win_rate = win_count / (win_count + lose_count) if win_count + lose_count > 0 else 0
        answer.append(
            (win_rate, heavier_win_count, my_weight, boxer_idx+1)
        )

    answer.sort(key=lambda x:(x[0], x[1], x[2], -x[3]), reverse=True)
    print(answer)
    return [x[3] for x in answer]

solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])

solution([145,92,86], ["NLW","WNL","LWN"])

solution([60,70,60], ["NNN","NNN","NNN"])

