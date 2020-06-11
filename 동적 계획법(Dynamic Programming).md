# 동적 계획법(Dynamic Programming)



## 피보나치 수열

```python
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-2) + fib(n-1)
```

위와 같은 재귀적인 방법은 많은 계산이 중복된다.



### 메모이제이션(기억해놓음)

```python
memo = [-1] * (n+1)

def fib(n):
    if n == 1 or n == 2:
        return 1
    elif memo[n] != -1:
        return memo[n]
    else:
        f[n] = fib(n-1) + fib(n-2)
        return f[n]
```

중간 결과서 caching(저장)함으로써 계산의 중복을 피함.

for문을 이용한 bottom-up 계산 방식도 가능.

```python
fibo = [0] * n
fibo[0], fibo[1] = 0, 1
for i in range(2, n+1):
	fibo[i] = fibo[i-1] + fibo[i-2]
return fibo[n]
```





## 이항 계수

n개의 경우의 수 중 k개를 고르는 방법

```python
def binomial(n, k):
    if (n == k or k == 0):
        return 1
    return binomial(n-1, k) + binomial(n-1, k-1)
```



### 메모이제이션

```python
memo = [[-1] * k for _ in range(n)]
def binomial(n, k):
    if n == k or k == 0:
        return 1
    elif if memo[n][k] > -1:
        return memo[n][k]
    else:
        memo[n][k] = binomial(n-1, k) + binomial(n-1, k-1)
       	return memo[n][k]
```

중간 결과서 caching(저장)함으로써 계산의 중복을 피함.



## 메모이제이션

- 순환식의 값을 계산하는 기법
- 동적 계획법으로 보기도 한다.
- recursion에서 수반되는 overhead가 없다.
- 

