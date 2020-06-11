# zero, one = 0, 0
# memo = [-1] * 41
# memo[1] = 1
# memo[2] = 1
#
# def fibo(n):
#     global zero, one
#     if n == 0:
#         zero += 1
#         return 0
#     if n == 1:
#         one += 1
#         return 1
#     else:
#         if memo[n] > -1:
#             return memo[n]
#         else:
#             memo[n] = fibo(n-1) + fibo(n-2)
#             return memo[n]
    # return memo[n]
for _ in range(int(input())):
    n = int(input())
    check = [[0, 0] for _ in range(41)]
    check[0], check[1] = [1, 0], [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            check[i] = [check[i-1][1], check[i-1][0] + check[i-1][1]]
    print(check[n][0], check[n][1])
    # fibo(int(input()))
    # for i in range(0, n):

    # print('{} {}'.format(zero, one))