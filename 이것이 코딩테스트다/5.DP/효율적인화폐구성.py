n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
print(moneys)
check = [0xffff] * (m+1)
dp = [[0xffff] * n for _ in range(m+1)]

for i in range(0, m+1):
    for j, money in enumerate(moneys):
        print("i {} , j  {}, money : {}, i-money : {}".format(i, j, money, i-money))
        if i == money:
            dp[i][j] = 1
        elif i > money:
            dp[i][j] = dp[i-money][j]+1
        # print(dp[j])
    if min(dp[i]) != 0xffff:
        check[i] = min(dp[i])

answer = check[-1] if check[-1] != 0xffff else -1




