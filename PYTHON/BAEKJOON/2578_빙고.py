
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
            temp_char2 += str(temp[j][i])
        if temp_char == '11111':
            bingo_count += 1
        if temp_char2 == '11111':
            bingo_count =+ 1
        temp_char = ''
        temp2_char = ''


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




