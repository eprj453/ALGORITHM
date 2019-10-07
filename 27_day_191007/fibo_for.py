def fibo(n):
    memo[0], memo[1] = 0, 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

n = 100
memo = [-1] * (n+1)
print(fibo(n))
print(memo)
