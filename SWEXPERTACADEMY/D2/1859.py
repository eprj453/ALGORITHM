
import sys
sys.stdin = open('input_1859.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    money_list = list(map(int, input().split()))
    #print(money_list)
    idx = 0
    my_buy = 0
    benefit = 0
    count = 0
    start = 0
    while True:
        if count == n:
            break
        max_val = max(money_list, default=0)
        for j in range(start, len(money_list)):
            if money_list[j] < max_val:
                my_buy += money_list[j]
                buy_count += 1
            if money_list[j] == max_val:
                benefit += ((max_val*buy_count)-(my_buy))
                buy_count = 0
                my_buy = 0
                money_list = money_list[j+1:]
                break
        count += 1
    print('#{} {}'.format(i, benefit))

# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     money_list = list(map(int, input().split()))
#     #print(money_list)
#     max_val = money_list[-1]
#     my_buy = 0
#     benefit = 0
#     for j in range(n-1, -1, -1):
#         if n == 10:
#             print('present benefit : {}'.format(benefit))
#         if max_val < money_list[j]:
#             max_val = money_list[j]
#             if n == 10:
#                 print('max_val > {}'.format(money_list[j]))
#         else:
#             benefit += (max_val - money_list[j])
#             if n == 10:
#                 print('benefit += {} - {} ({}) > {}'.format(max_val, money_list[j],max_val-money_list[j], benefit))
#     print('#{} {}'.format(i, benefit))