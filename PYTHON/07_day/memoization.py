# memoization
memo = [-1] * 100
def fibo2(n):
    if n == 1 or n == 0:
        return n
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo2(n - 1) + fibo2(n - 2)


# 재귀호출의 memoization
# 재귀적 DP
memo2 = [-1] * 100
def fibo3(n):
    memo2[0], memo2[1] = 0, 1
    for i in range(2, n+1): # 문제의 크기를 나타내는 i
        memo2[i] = memo2[i-1] + memo2[i-2]
    return memo2[n]
# 0과 1은 이미 알고 있고, 0과 1의 값을 알면 2의 값을 알 수 있다.
# 1과 2의 값을 알면 3의 값을 알 수 있고, 이러한 과정으로 n번째까지의 값을 빠르게 구할 수 있다.
# 함수를 재귀적으로 호출하면 스택 오버헤드가 발생할 수 있기 때문에 2번째 방법이 메모리상 더 효율적이다.


