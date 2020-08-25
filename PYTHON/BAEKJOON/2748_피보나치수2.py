n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    fibo = [[]] * n
    fibo[0], fibo[1] = 1, 1
    for i in range(2, n):
        fibo[i] = fibo[i-1] + fibo[i-2]

    print(fibo[n-1])