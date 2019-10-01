import sys
sys.stdin = open('1244_input.txt', 'r')

# def shuffle(number, count):
#     global max_price
#
#     if count > 0 and max(max_val) > int(number[0]):
#         print('return, count : ', count)
#         return
#
#     elif count == c:
#         print(numbers)
#         max_price = max(max_price, int(''.join(number)))
#         return
#
#
#     else:
#         for i in range(len(number)):
#             for j in range(len(number)):
#                 if i == j: continue
#                 # if i == j: continue
#                 # temp = []
#                 # for j in range(len(numbers)):
#                 #     temp.append(numbers[j])
#                 # if numbers[0] == max(numbers): continue
#                 # if numbers[i] <= numbers[j]: continue
#                 # temp[i], temp[j] = temp[j], temp[i]
#                 # shuffle(temp, count+1)
#                 # temp[j], temp[i] = temp[i], temp[j]
#                 if number[i] <= number[j]: continue
#                 # if numbers[i] == max(numbers) : continue
#                 number[i], number[j] = number[j], number[i]
#                 # print(numbers)
#                 shuffle(number, count+1)
#                 number[j], number[i] = number[i], number[j]
#                 # shuffle(number, count+1)
# for i in range(1, int(input())+1):
#     nums, c = map(int, input().split())
#     numbers = list(map(str, str(nums)))
#     max_val = list(map(int, str(nums)))
#     print(max_val)
#     print('numbers : ', numbers)
#     print('c : ', c)
#     print('max_val : ', max(max_val))
#     max_price = 0
#     shuffle(numbers, 0)
#
#     print(max_price)



# for i in range(1, int(input())+1):
#     nums, c = map(int, input().split())
#     int_nums = list(map(int, str(nums)))
#     # print(int_nums)
#     # print(c)
#     count = 0
#     for j in range(len(int_nums)):
#         # if int_nums[j] == max(int_nums):
#         #     continue
#         m_idx = j
#         for k in range(j+1, len(int_nums)):
#             if int_nums[m_idx] <= int_nums[k]:
#                 m_idx = k
#
#         if m_idx != j:
#             int_nums[m_idx], int_nums[j] = int_nums[j], int_nums[m_idx]
#             count += 1
#         if count >= c:
#             break
#     # print(count, int_nums)
#     if count < c:
#         while count < c:
#
#             int_nums[len(int_nums)-1], int_nums[len(int_nums)-2] = int_nums[len(int_nums)-2], int_nums[len(int_nums)-1]
#             count += 1
#             # print(count, int_nums)
#
#     print(int_nums)
        # if count > c:
        #     break
        # if int_nums[j] == max(int_nums):
        #     continue
        # else:
        #     max_temp = int_nums[j]
        #     max_temp_idx = j
        #     for k in range(j, len(int_nums)):
        #         if int_nums[k] > max_temp:
        #             max_temp_idx = k
        #     int_nums[j], int_nums[max_temp_idx] = int_nums[max_temp_idx], int_nums[j]
        #     count += 1
    # print('count : ', count)
    # print(int_nums)
    #     if count < c:
    #         while count < c:
    #             int_nums[len(int_nums)-1], int_nums[len(int_nums)-2] = int_nums[len(int_nums)-2], int_nums[len(int_nums)-1]
    #             count += 1
    #
    # #
    # print(int_nums)

# def shuffle(count, k):
#     global max_price
#
#     # if count > 0 and int_nums[0] != max(int_nums):
#     #     return
#
#     # if count > 0 and int_nums[0] != max(int_nums):
#     #     return
#
#     if count == c:
#         max_price = max(max_price, int(''.join(map(str, int_nums))))
#         return
#
#     else:
#         for i in range(k, len(int_nums)):
#             for j in range(i+1, len(int_nums)):
#                 if int_nums[i] <= int_nums[j]:
#                     int_nums[i], int_nums[j] = int_nums[j], int_nums[i]
#                     shuffle(count + 1, i)
#                     int_nums[j], int_nums[i] = int_nums[i], int_nums[j]
#
# for i in range(1, int(input())+1):
#     nums, c = map(int, input().split())
#     int_nums = list(map(int, str(nums)))
#     max_price = 0
#     shuffle(0, 0)
#     print('#{} {}'.format(i, max_price))


for i in range(1, int(input())+1):
    nums, c = map(int, input().split())
    int_nums = list(map(int, str(nums)))
    nums = str(nums)
    num_set = set()
    num_set.add(nums)
    int_nums = list(map(int, str(nums)))
    n = 0
    max_val = 0
    temp2 = set()
    while n < c:
        while num_set:
            temp = num_set.pop()
            temp = list(temp)
            print(temp)
            for i in range(len(temp)-1):
                for j in range(i, len(temp)):
                    temp[i], temp[j] = temp[j], temp[i]
                    temp2.add(''.join(temp))
                    temp[j], temp[i] = temp[i], temp[j]
                num_set = temp2
                print(num_set)
                temp2 = set()
        n += 1

    print(max(num_set))
    print()
