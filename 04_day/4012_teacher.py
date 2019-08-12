arr = [1, 2, 3, 4]

n = 4

for set in range(1 << 4):
    a , b = [], []
    for i in range(n):
        if set & (i << 1):
            a.append(i)
        else:
            b.append(i)

    if len(a) == len(b):
        # list append
        pass

