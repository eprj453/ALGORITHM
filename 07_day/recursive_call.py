# 문제를 재귀적으로 푼다.
# 재귀적 정의를 구현할때 재귀호출이 좋다
# 재귀적 정의 > 좀 더 작은 문제의 답을 사용해서 더 큰 문제의 답을 구하는 방법
# ex 팩토리얼 구하는 문제

def fact(n):
    if n == 0 or n == 1: # 만약 1! 이나 0!이라면
        return 1
    else:
        return fact(n-1) * n



print(fact(5))



def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

memo = [-1] * 100
def fibo2(n):
    if n == 1 or n == 0:
        return n
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo2(n - 1) + fibo2(n - 2)