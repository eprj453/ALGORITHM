ans = []
def shuffle(num_list, num_list2, num_list3, count):
    global ans
    if num_list == num_list2 or num_list == num_list3:
        ans.append(count)
        # return count

    if count >= 5:
        return -1

    N = len(num_list)

    for i in range(N):
        if i < (N//2):
            list1, list2 = num_list[0:N//2], num_list[N//2: N]
            for j in range(i):
                list1.insert(-(i - j), list2[0])
                list2.remove(list2[0])
            # print(list1+list2)
            if list1+list2 == num_list2 or list1+list2 == num_list3:
                # print('일치')
                ans.append(count+1)
                # return count+1
            else:
                shuffle(list1+list2, num_list2, num_list3, count+1)

        else:
            list1, list2 = num_list[0 : N//2], num_list[N//2 : N]
            for j in range(i - (N//2)):
                # print('반복문')
                # print(j)
                list2.insert(N - i + j, list1[0])
                list1.remove(list1[0])
            if list2+list1 == num_list2 or list2+list1 == num_list3:
                # print('일치')
                # return count+1
                ans.append(count+1)
            else:
                shuffle(list2 + list1, num_list2, num_list3, count + 1)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    list1 = list(map(int, input().split()))
    ans = []
    shuffle(list1, sorted(list1), sorted(list1, reverse=True), 0)
    if len(ans) == 0:
        print('#{} {}'.format(i, -1))
    else:
        print('#{} {}'.format(i, min(ans)))

'''
5
4
1 2 3 4 
4
4 2 3 1 
6
6 5 4 2 3 1 
8
6 1 4 7 2 5 8 3 
12
2 7 4 1 3 5 8 10 12 9 6 11 

'''