temp = '01101110111011010001100100110111011011101100010110001101'
count = [1]
for t in range(len(temp)-1):
    if temp[t] == temp[t+1]:
        count[-1] += 1
    else:
        count.append(1)

print(count)
# #
# a = '13'
# b = '23'
# print(a+b)
list1 = [4,4,4,16]

# list1[1] = round(list1[1] / 2)
# print(list1[1] == 4)
# print(list1)
# for i in range(len(list1)):
#     list1[i] = round(list1[i] / 2)
# print(list1)
# result = False
# while result == False:
#     if result == True:
#         break
#     for i in range(len(list1)):
#         if list1[i] == 1:
#             result = True
#             break
#     if result == False:
#         for i in range(len(list1)):
#             list1[i] = round(list1[i] // 2)
#
# print(list1)
# print(list1)
#
# my_dict = {'0': [3, 2, 1, 1], '1': [2, 2, 2, 1], '2': [2, 2, 1, 2], '3': [1, 4, 1, 1], '4': [1, 1, 3 ,2],
#            '5': [1, 2, 3, 1], '6': [1, 1, 1, 4], '7': [1, 3, 1, 2], '8': [1, 2, 1, 3], '9': [3, 1, 1, 2]
#            }
my_dict = {'3221': 0, '2221': 1, '2212': 2, '1411': 3, '1132': 4,
           '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9
            }
# my_dict = {[3, 2, 1, 1]: 0, [2, 2, 2, 1]: 1, [2, 2, 1, 2]: 2, [1, 4, 1, 1]: 3, [1, 1, 3 ,2]: 4,
#            [1, 2, 3, 1]: 5, [1, 1, 1, 4]: 6, [1, 3, 1, 2]: 7, [1, 2, 1, 3]: 8, [3, 1, 1, 2]: 9
#             }
# print(my_dict.keys())
print(my_dict['3221'])

my_dict2 = {'0': '0001101', '1': '0011001', '2': '0010011', '3': '0111101', '4': '0100011',
           '5': '0110001', '6': '0101111', '7': '0111011', '8': '0110111', '9': '0001011'
            }

# print(my_dict['0'])
# print([1,2,3,1] in my_dict.values())