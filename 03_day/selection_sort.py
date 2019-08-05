# arr = [60,80,11,65,32]
#
# # 최소값의 위치를 찾는다.
#
# for j in range(0, len(arr)):
#     min_idx = j
#     for i in range(min_idx+1, len(arr)):
#         if arr[i] < arr[min_idx]:
#             min_idx = i
#     arr[j], arr[min_idx] = arr[min_idx], arr[j]
#
# print(arr)


arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][(j + -(2*j+1) * (i%2))])
        #             j
        #             0   1
        #             1   3
        #             2   5
        #             3   7
                    # 4   9
                        #
    print()