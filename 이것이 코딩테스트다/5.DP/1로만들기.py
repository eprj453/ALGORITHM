# x = int(input())
# dp = [0] * (x+1)
#
# for i in range(2, x+1):
#     dp[i] = dp[i-1] + 1
#     if not i % 5:
#         dp[i] = min(dp[i], dp[i//5]+1)
#     if not i % 3:
#         dp[i] = min(dp[i], dp[i//3]+1)
#     if not i % 2:
#         dp[i] = min(dp[i], dp[i//2]+1)
# print(dp)


x = int(input())

calculates = [float('inf')] * (x+1)

for i in range(len(calculates), 0, -1):
    calculates[i-1] = calculates[i] - 1

