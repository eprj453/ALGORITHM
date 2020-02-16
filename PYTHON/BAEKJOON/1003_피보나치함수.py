zero, one = 0, 0
pibos = [0] * 40
pibos[0], pibos[1] = 1, 1

def pibo(n):
    global zero, one
    if n == 0:
        zero += 1
        return 0
    if n == 1:
        one += 1
        return 1
    else:
        return pibo(n-1) + pibo(n-2)
for _ in range(int(input())):
    zero, one = 0, 0
    pibo(int(input()))
    print('{} {}'.format(zero, one))