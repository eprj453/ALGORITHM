n = int(input())
numbers = list(map(int, input().split()))
max_value = numbers[0]
dp = [0] * n
dp[0] = numbers[0]
for i in range(1, n):
    dp[i] = max(0, dp[i-1]) + numbers[i]
    max_value = max(max_value, dp[i])
print(dp)
print(max_value)
