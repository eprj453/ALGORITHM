def fibo(n):
    global cnt

    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


cnt = 0
print(fibo(20))
print('함수 호출 횟수 : ',cnt)
