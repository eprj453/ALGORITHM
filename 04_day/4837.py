import sys
sys.stdin = open('4837_input.txt', 'r')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

t = int(input())
for i in range(1, t+1):
    nk = list(map(int, input().split()))
    print(nk[0], nk[1])
    temp = []
    temp2 = []
    sum_list = []
    sum = 0
    count = 0
    n = len(list1)
    for j in range(1<<n):
        for k in range(n+1):
            if j & (1<<k):
               temp.append(list1[k])
               sum += list1[k]
        # print(temp)
        if len(temp) == nk[0]:
            if sum == nk[1]:
                count+=1
        # if len(temp) == nk[0] and sum(temp) == nk[1]:
        #     count += 1
       # print('temp : {}'.format(temp))
       # # print('sum : {}'.format(sum))
       #  if len(temp) == nk[0]:
       #      temp2.append(temp)
       #      sum_list.append(sum)
        # if sum == nk[1]:
        #     sum_list.append(sum)
        # if len(temp) == nk[0] and sum == nk[1]:
        #     count += 1
        sum = 0
        temp = []
    # print(temp2)
    # print(sum_list)

    # answer = list(map(sum, list(map(int, temp2)))).count(nk[1])
    # print('answer : {}'.format(answer))
    # print(temp2)

    print('#{} {}'.format(i, count))