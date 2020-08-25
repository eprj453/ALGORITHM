n, k = map(int, input().split())

count = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    if not k: break
    coin = coins[i]
    if k / coin > 0:
        count += (k // coin)
        k %= coin

print(count)
