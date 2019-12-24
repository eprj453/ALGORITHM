t = int(input())

for i in range(1, t+1):
    n = int(input())

    for j in range((n-1)**2 + n**2 - (2*(n-1))), ((n-1)**2 + n**2 + (2*(n-1))+1, 2):
        for k in range(1, n, 2):
            print(j, end=" ")


    print('#{} {} {}'.format(i, (n-1)**2 + n**2 - (2*(n-1)), (n-1)**2 + n**2 + (2*(n-1))))