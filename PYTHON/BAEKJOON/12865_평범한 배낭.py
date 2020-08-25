n, k = map(int, input().split())
objects = [[]] * (n+1)
for i in range(1, n+1):
    objects[i] = list(map(int, input().split()))
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = objects[i][0], objects[i][1]
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], (dp[i-1][j-w] + v))

print(dp[n][k])