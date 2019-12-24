t = int(input())
date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# 5 5 8 15 103
# 26 30 31 15
print(type(date_dict[5]))
for i in range(1, t+1):
    date_list = list(map(int, input().split()))
    date_list2 = []
    answer = 0
    for j in range(0, len(date_list), 2):
        temp = []
        for k in range(j, j+2):
            temp.append(date_list[k])
        date_list2.append(temp)

    if date_list2[0][0] == date_list2[1][0]:
        answer = date_list2[1][1] - date_list2[0][1] + 1

    elif date_list2[1][0] > date_list2[0][0]:
        answer += (date_dict[date_list2[0][0]] - date_list2[0][1])
        for j in range(date_list2[0][0]+1, date_list2[1][0]):
            answer += date_dict[j]
        answer += (date_list2[1][1]+1)

    print('#{} {}'.format(i, answer))





