for _ in range(int(input())):
    check = [0] * 10
    check_2 = []
    a, b = map(int, input().split())

    num = a
    while True:
        target = int(str(num)[-1])
        if check[target]: break
        else:
            check[target] = 1
            check_2.append(target)
            num *= a

    n = (b % len(check_2))-1
    answer = check_2[n] if check_2[n] != 0 else 10
    print(check_2[n])