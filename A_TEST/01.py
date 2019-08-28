
def shuffle(num_list, num_list2, num_list3, count):
    if num_list == num_list2 or num_list == num_list3:
        return count

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
                print('일치')
                return count+1
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
                print('일치')
                return count+1
            else:
                shuffle(list2 + list1, num_list2, num_list3, count + 1)



list1 = [6,5,4,2,3,1]
N=len(list1)
print(list1)
print(sorted(list1))
print(sorted(list1, reverse=True))
print(list1[0:N//2])
print(list1[N//2:N])
print(shuffle(list1, sorted(list1), sorted(list1, reverse=True), 0))

    # print(cards1, cards2)

# t = int(input())
# for i in range(1, t+1):
#     cards_len = int(input())
#     cards = list(map(int, input().split()))
#     print(shuffle(cards,0))


# list1,list2 = [1,2,3,4], [5,6,7,8]


# num_list = [6,1,4,7,2,5,8,3]
# N = len(num_list)
# for i in range(0, N):
#     if i < N//2:
#         list1, list2 = num_list[0:N//2], num_list[N//2 : N]
#         for j in range(i):
#             list1.insert(-(i-j),list2[0])
#             list2.remove(list2[0])
#         print(list1 + list2)
#     else:
#         list1, list2 = num_list[0:N//2], num_list[N//2:N]
#         for j in range(i-(N//2)):
#             list2.insert(N-i+j, list1[0])
#             list1.remove(list1[0])
#         print(list2 + list1)