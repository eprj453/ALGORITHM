for i in range(1, int(input())+1):
    # print(type(2**(-1)))
    cnt, ans = 1, ''
    num = float(input())
    while num != 0:
        if cnt > 12:
            ans = 'overflow'
            break
        if num >= 2**(-cnt):
            num -= 2**(-cnt)
            ans += '1'
        else:
            ans += '0'
        cnt += 1
    print('#{} {}'.format(i, ans))
