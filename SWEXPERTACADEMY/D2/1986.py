t = int(input())
for i in range(1, t+1):
    count = 0
    n = int(input())
    for i in range(1, n+1):
        if i % 2:
            count += i
        else:
            count -= i
    print('#{} {}',i,count)