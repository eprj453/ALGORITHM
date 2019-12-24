a_prize = [5000000, 3000000, 2000000, 500000, 300000, 100000]
b_prize = [5120000, 2560000, 1280000, 640000, 320000]
for _ in range(int(input())):
    total = 0
    a, b = map(int, input().split())

    a_temp = 0
    if a and a <= 21:
        p1 = 1
        for p in range(0, 6):
            a_temp += p1
            if a_temp >= a:
                total += a_prize[p]
                break
            else:
                p1 += 1

    b_temp = 0
    if b and b <= 31:
        p2 = 1
        for p in range(0, 5):
            b_temp += p2
            if b_temp >= b:
                total += b_prize[p]
                break
            else:
                p2 *= 2
    print(total)