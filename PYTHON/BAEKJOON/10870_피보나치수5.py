fibo = [0, 1] + [None] * 19

def get_fibo(n):
    if fibo[n] is not None:
        return fibo[n]

    return get_fibo(n-1) + get_fibo(n-2)

n = int(input())
print(get_fibo(n))