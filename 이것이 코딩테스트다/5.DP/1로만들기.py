x = int(input())
dp = [0] * (x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if not i % 5:
        dp[i] = min(dp[i], dp[i//5]+1)
    elif not i % 3:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif not i % 2:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp)
# # index : num // value : 최소연산
# def make_one(num):
#     print('make_one')
#     if num == 1:
#         return
#     if not num % 5:
#         if dp[]
#         dp[num // 5] = min(dp[num // 5]+1, dp[num])
#         make_one(num//5)
#     elif not num % 3:
#         dp[num // 3] = min(dp[num // 3]+1, dp[num])
#         make_one(num//3)
#     elif not num % 2:
#         dp[num // 2] = min(dp[num // 2]+1, dp[num])
#         make_one(num//2)
#     else:
#         dp[num-1] = min(dp[num], dp[num-1]+1)
#         make_one(num-1)
#
# make_one(x)
# print(dp)