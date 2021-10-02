n = int(input())
numbers = list(map(int, input().split(' ')))

dp = [0] * n
dp[0] = 1

for i in range(n):
    curr_value = numbers[i]
    curr_dp_value = 0
    for j in range(0, i):
        if numbers[j] < curr_value:
            curr_dp_value = max(curr_dp_value, dp[j])

    dp[i] = curr_dp_value + 1

answer = max(dp)
print(answer)


