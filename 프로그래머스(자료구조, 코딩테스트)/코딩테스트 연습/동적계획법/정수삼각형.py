def solution(triangle):
    answer = 0
    max_value = 9999 * 500
    n = len(triangle)
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if not j:
                dp[i][j] = dp[i - 1][0] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            # print(dp[i][j])
    print(dp[n-1])
    answer = max(dp[n-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))