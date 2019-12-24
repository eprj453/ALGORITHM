# t = int(input())
# for i in range(1, t+1):
#     knm_list = list(map(int, input().split()))
#     stop_list = list(map(int, input().split()))
#
#     max_move = knm_list[0]
#
#     print('#최초의 최대 이동 거리는 {}'. format(max_move))
#     count = 0
#     for j in range(0, knm_list[1]+1):
#         print('현재 위치 {}'.format(j))
#         print('최대 이동 거리는 {}'.format(max_move))
#         if max_move < 0:
#             count = 0
#             break
#         if j in stop_list:
#             print('{} 정류장 만남'.format(j))
#             stop = 0
#             for k in stop_list: # 내 바로 앞에 있는 충전소 찾는 for문
#                 if j == stop_list[-1]: # 만약 내 위치가 마지막 정류소라면?
#                     stop = knm_list[1] # 마지막 위치를 정류소처럼 사용(거리 측정시, 다음 정류소까지 거리가 아닌 마지막 지점까지의 거리로 하기 위해 )
#                     break
#                 if j > k:
#                     continue
#                 elif j < k:
#                     stop = k
#                     break
#             print('{}번 정류장까지 거리? {}'.format(stop, stop-j))
#             print('현재 최대 이동거리 {}'.format(max_move))
#             if max_move < stop - j:
#                 count += 1
#                 max_move = knm_list[0]
#                 print('충전! 최대 이동거리 {}, 충전횟수 {} '.format(max_move, count))
#         max_move -= 1
#     print('#{} {}'.format(i, count))

#
# t = int(input())
# for i in range(1, t+1):
#     knm_list = list(map(int, input().split()))
#     stop_list = list(map(int, input().split()))
#
#     max_move = knm_list[0]
#
#     print('#최초의 최대 이동 거리는 {}'. format(max_move))
#     count = 0
#     for j in range(0, knm_list[1]+1):
#         print('현재 위치 {}'.format(j))
#         print('최대 이동 거리는 {}'.format(max_move))
#         if max_move < 0:
#             count = 0
#             break
#         if j in stop_list:
#             print('{} 정류장 만남'.format(j))
#             stop = 0
#             for k in stop_list: # 내 바로 앞에 있는 충전소 찾는 for문
#                 if j == stop_list[-1]: # 만약 내 위치가 마지막 정류소라면?
#                     stop = knm_list[1] # 마지막 위치를 정류소처럼 사용(거리 측정시, 다음 정류소까지 거리가 아닌 마지막 지점까지의 거리로 하기 위해 )
#                     break
#                 if j > k:
#                     continue
#                 elif j < k:    # 내 바로 앞 정류장을 찾으면 stop에 저장 후 break
#                     stop = k
#                     break
#             print('{}번 정류장까지 거리? {}'.format(stop, stop-j))
#             print('현재 최대 이동거리 {}'.format(max_move))
#             if max_move < stop - j: # 갈수 있는 거리 < 다음 정류장까지의 거리
#                 count += 1  # 충전 count += 1
#                 max_move = knm_list[0] # 이동가능거리도 다시 n만큼으로
#                 print('충전! 최대 이동거리 {}, 충전횟수 {} '.format(max_move, count))
#         max_move -= 1 # 이동 가능거리 1 감소
#     print('#{} {}'.format(i, count))


