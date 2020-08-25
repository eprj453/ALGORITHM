
# 17 4
# answer -> 3

# 25 5
# answer -> 2

n, k = map(int, input().split())

answer = 0
while n > 1:
    print(n)
    if not n % k:
        answer += 1
        n //= k
    else:
        answer += (n % k)
        n -= (n % k)
print('-------------')
print(answer)