# my_list = []
# other_list = []
# temp = []
# temp_char = ''
# count = 0
# for i in range(0, 10):
#     if i < 5:
#         my_list.append(list(map(str, input().split())))
#     else:
#         other_list += list(map(str, input().split()))

# for num in range(0, len(other_list)):
#     for j in range(0, len(my_list)):
#         for k in range(0, len(my_list[0])):
#             if num == my_list[j][k]:
#                 my_list[j][k] = 0
#                 count += 1
#
#     for j in range(0, len(my_list)):
#         for k in range(0, len(my_list[0])):


my_list, other_list, temp = [], [], []
bingo = False
count = 0

for i in range(0, 5):
    temp.append([0]*5)

for i in range(0, 10):
    if i < 5:
        my_list += list(map(str, input().split()))
    else:
        other_list += list(map(str, input().split()))

for num in other_list:
    bingo_count = 0
    temp_char, temp_char2 = '', ''
    if num in my_list:
        idx = my_list.index(num)
        temp[idx // len(temp)][idx % len(temp)] = 1
        count += 1

    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp_char += str(temp[i][j])
        if temp_char == '11111':
            bingo_count += 1
        temp_char = ''

    if bingo_count >= 3:
        print(count)
        break

    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp_char += str(temp[j][i])
        if temp_char == '11111':
            bingo_count += 1
        temp_char = ''

    if bingo_count >= 3:
        print(count)
        break

    for i in range(len(temp)):
        temp_char += str(temp[i][i])
        temp_char2 += str(temp[i][len(temp)-1-i])
    if temp_char == '11111':
        bingo_count += 1
    if temp_char2 == '11111':
        bingo_count += 1

    if bingo_count >= 3:
        print(count)
        break






