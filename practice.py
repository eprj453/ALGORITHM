# temp_list = [1,2,3,4,5,6,7,8]
# temp_list2 = []
# count_list = []
# count = 0
# for j in range(1 << len(temp_list)):
#     for k in range(len(temp_list) + 1):
#         if j & (1 << k):
#             temp_list2.append(temp_list[k])
#     if len(temp_list2) == 4:
#         count_list.append(temp_list2)
#         count+=1
#     temp_list2 = []
#
# print(count)
# print(count_list)

print(list(range(4)))