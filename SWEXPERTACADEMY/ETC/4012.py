import sys
sys.stdin = open('4012_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    food_list = []
    for j in range(n):
        food_list.append(list(map(int, input().split())))
    temp_list = list(range(n))
    temp_list2, temp_list3, count_list, count_list2 = [], [], [], []

    for j in range(1 << len(temp_list)):
        for k in range(len(temp_list)+1):
            if j & ( 1 << k ):
                temp_list2.append(temp_list[k])
        if len(temp_list2) == n/2:
            for cnt in range(n):
                if cnt not in temp_list2:
                    temp_list3.append(cnt)
            count_list.append(temp_list2)
            count_list2.append(temp_list3)
        temp_list2 = []
        temp_list3 = []

    print(count_list)
    print(count_list2)

    taste = 10000000000
    for j in range(len(count_list)//2):
        a, b = 0, 0
        for k in range(len(count_list[0])):
            for p in range(k, len(count_list[0])):
                a += (food_list[count_list[j][k]][count_list[j][p]] + food_list[count_list[j][p]][count_list[j][k]])
                b += (food_list[count_list2[j][k]][count_list2[j][p]] + food_list[count_list2[j][p]][count_list2[j][k]])
        if abs(a-b) < taste:
            taste = abs(a-b)

    print('#{} {}'.format(i, taste))