import sys
sys.stdin = open('5099_input.txt', 'r')


# t = int(input())
# for i in range(1, t+1):
#     n, m = map(int, input().split())
#     pizza = list(map(int, input().split()))
#     pizza_q = []
#     for j in range(m):
#         pizza[j] = [pizza[j], j+1]
#     for j in range(n):
#         pizza_q.append(pizza[0])
#         pizza.pop(0)
#     count = m
#     while count > 1:
#         # print(count)
#         # print('돈다')
#         # print(pizza_q)
#         if len(pizza_q[0]) == 0:
#             pizza_q.insert(n, pizza_q.pop(0))
#         else:
#             pizza_q[0][0] = (pizza_q[0][0] // 2)
#             if pizza_q[0][0] == 0:
#                 pizza_q.pop(0)
#                 if len(pizza) > 0:
#                     pizza_q.insert(0, pizza.pop(0))
#                     count -= 1
#                 else:
#                     pizza_q.insert(0, [])
#                     count -= 1
#             pizza_q.insert(n, pizza_q.pop(0))
#
#     for j in range(len(pizza_q)):
#         if len(pizza_q[j]) != 0:
#             print('#{} {}'.format(i, pizza_q[j][1]))
#             break

t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza_q = []
    for j in range(m):
        pizza[j] = [pizza[j], j+1]
    for j in range(n):
        pizza_q.append(pizza[0])
        pizza.pop(0)
    while len(pizza_q) > 1:
        if pizza_q[0][0] == 0:
            if len(pizza) > 0:
                pizza_q.pop(0)
                pizza_q.insert(0, pizza.pop(0))
            else:
                pizza_q.pop(0)
        else:
            pizza_q[0][0] = (pizza_q[0][0] // 2)
            pizza_q.insert(n, pizza_q.pop(0))

    print('#{} {}'.format(i, pizza_q[0][1]))