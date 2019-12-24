def num_check(check):
    x, y = 1, 1
    dx, dy = 1, -1
    count = 1
    num = 1
    check = check
    while True:
        if check == num:
            return [x, y]
        if y + dy == 0:
            count += 1
            x = 1
            y = count
        else:
            x, y = x+dx, y+dy
        num += 1

def coop_check(x, y):
    x_sum = 0
    for i in range(x, 0, -1):
        x_sum += i
    y_num = x
    for i in range(y-1):
        x_sum += y_num
        y_num += 1
    return x_sum

t = int(input())
for i in range(1, t+1):
    p, q = map(int, input().split())
    print('#{} {}'.format(i, coop_check(num_check(p)[0] + num_check(q)[0], num_check(p)[1]+num_check(q)[1])))
