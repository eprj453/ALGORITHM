import sys
sys.stdin = open('1486_input.txt', 'r')

def subset():
    global min_val
    N = len(talls)
    for j in range(1 << N):
        tall_sum = 0
        for k in range(N):
            if j & (1 << k):
                tall_sum += talls[k]
            if (tall_sum - b) > min_val:
                break
        if tall_sum >= b:
            min_val = min(min_val, tall_sum - b)

for i in range(1, int(input())+1):
    n, b = map(int, input().split())
    talls = list(map(int, input().split()))
    min_val = 10000 * 20
    subset()
    print('#{} {}'.format(i, min_val))
