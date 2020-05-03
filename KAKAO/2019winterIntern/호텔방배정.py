import sys
sys.setrecursionlimit(1000)

# rooms = dict()
def find(empty_number, rooms):
    if rooms.get(empty_number) == None: # 빈 방일 경우
        rooms[empty_number] = empty_number + 1
        return empty_number
    else:
        rooms[empty_number] += 1
        empty_number = rooms[empty_number]-1
    ans = find(empty_number, rooms)
    rooms[empty_number] = ans + 1
    return ans


def solution(k, room_number):
    answer = []
    rooms = dict()
    for r in room_number:
        empty = find(r, rooms)
        answer.append(empty)
    return answer

print(solution(10, [1,3,4,1,3,1]))


# def solution(k, room_number):
#     answer = []
#     rooms = dict()
#     for r in room_number:
#         tmp = r
#         while rooms.get(tmp):
#             if tmp > 10**12: break
#             rooms[tmp] += 1
#             tmp = rooms[tmp]-1
#         answer.append(tmp)
#         rooms[tmp] = tmp + 1
#
#     return answer