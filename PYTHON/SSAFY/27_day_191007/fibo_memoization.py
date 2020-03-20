def fibo(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]
    # else:




cnt = 0
n = 20
memo = [-1] * (n+1)
memo[0], memo[1] = 0, 1
print(fibo(n))
print('함수 호출 횟수 : ',cnt)
print(memo)