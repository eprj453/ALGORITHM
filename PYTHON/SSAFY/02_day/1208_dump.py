# for i in range(1, 11):
#     dump = int(input())
#     box_list = list(map(int, input().split()))
#
#     max_idx = 0
#     min_idx = 0
#
#     count = 0
#
#     for j in range(0, dump + 1):
#
#         box_list[max_idx] -= 1
#         box_list[min_idx] += 1
#
#         for idx, value in enumerate(box_list):
#             if value > box_list[max_idx]:
#                 max_idx = idx
#             elif value < box_list[min_idx]:
#                 min_idx = idx
#
#         # box_list[max_idx] -= 1
#         # box_list[min_idx] += 1
#
#         if box_list[max_idx] - box_list[min_idx] <= 1:
#             break
#
#         count += 1
#     print('최대값 {} 최소값 {} 최대값인덱스 {} 최소값인덱스 {} 차이 {} 연산횟수 {}'.format(box_list[max_idx], box_list[min_idx], max_idx, min_idx, (box_list[max_idx] - box_list[min_idx]),count))


import sys
sys.stdin = open('4831.txt', 'r')
T = int(input())

for num in range(T):
    K, N, M = list(map(int, input().split()))
    charger = list(map(int, input().split()))
    count = 0
    result = []
    for number in range(N+1):
        for i in range(count, count + K + 1):
            if i in charger and count + K < N:
                count = i
        result.append(count)

    for i in range(1, len(result)-1):
        if result[i] != result[i-1]:
            if result[i-1] == result[i+2]:
                result = []
                break
        if result[0] == result[1]:
            result = []
            break

    print(result)
    result = len(set(result))



    print('#{} {}'.format(num+1, result))


