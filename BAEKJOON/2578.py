
my_list, other_list, temp = [], [], []
bingo = False
count = 0

for i in range(0, 5):
    temp.append([0]*5)

for i in range(0, 10):
    if i < 5:
        my_list.append(list(map(int, input().split())))
    else:
        other_list += list(map(int, input().split()))

print(my_list)
print(other_list)
for num in other_list:
    bingo_count = 0
    print(bingo_count)
    temp_sum, temp_sum2 = 0, 0

    for i in range(0, len(my_list)):
        for j in range(0, len(my_list[0])):
            if num == my_list[i][j]:
                my_list[i][j] = 0
                count += 1

    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp_sum += my_list[i][j]
            temp_sum2 += my_list[j][i]
        if temp_sum == 0:
            bingo_count += 1
        if temp_sum2 == 0:
            bingo_count += 1

    if bingo_count >= 3:
        print(count)
        break

    for i in range(len(temp)):
        temp_sum += my_list[i][i]
        temp_sum2 += my_list[i][len(my_list)-1-i]
    if temp_sum == 0:
        bingo_count += 1
    if temp_sum2 == 0:
        bingo_count += 1

    if bingo_count >= 3:
        print(count)
        break






