# t = int(input())
# money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for i in range(1, t+1):
#     my_money = int(input()) # 만약 32850원이라면?
#     count_list = [0, 0, 0, 0, 0, 0, 0, 0]
#     print('내 거스름돈은 {}'.format(my_money))
#     while my_money > 0:
#         minus_money = 0
#         for j in range(0, len(money_list)):
#             if money_list[j] <= my_money:
#                 minus_money = money_list[j]
#                 my_money = my_money - minus_money
#                 print('빼는 돈은 {}'.format(money_list[j]))
#                 print('남는 돈은 {}'.format(my_money))
#                 count_list[j] += 1
#                 break
#     print(count_list)
#     answer = ' '.join(list(map(str, count_list)))
#     print('#{}'.format(i))
#     print('{}'. format(' '.join(list(map(str, count_list)))))


# t = int(input())
# money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for i in range(1, t+1):
#     my_money = int(input())
#     count_list = [0, 0, 0, 0, 0, 0, 0, 0]
#     while my_money > 0:
#         if my_money <= 0:
#             break
#         minus_money = 0
#         for j in range(0, len(money_list)):
#             if money_list[j] <= my_money:
#                 minus_money = money_list[j]
#                 count_list[j] += 1
#                 break
#         my_money -= minus_money
#     print('#{}\n{}'.format(i, ' '.join(list(map(str, count_list)))))
#
#
t = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(1, t+1):
    my_money = int(input())
    count_list = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(0, len(money_list)):
        if my_money // money_list[j] == 0:
            continue
        elif my_money // money_list[j] > 0:
            count_list[j] += (my_money // money_list[j])
            my_money -= (money_list[j] * (my_money // money_list[j]))

    print('#{}\n{}'.format(i, ' '.join(list(map(str, count_list)))))


# print(32850 // 10000)