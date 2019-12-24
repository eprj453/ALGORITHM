import sys
sys.stdin = open('1486_input.txt', 'r')

def my_func(s, e, tall_sum):
    global min_val


    if tall_sum >= b:
        min_val = min(tall_sum - b, min_val)
        return

    if s > e:
        return

    my_func(s+1, e, tall_sum + talls[s])
    my_func(s+1 ,e, tall_sum)


for i in range(1, int(input())+1):
    n, b = map(int, input().split())
    talls = list(map(int, input().split()))
    min_val = 10000 * 20
    my_func(0, n-1, 0)
    print('#{} {}'.format(i, min_val))
