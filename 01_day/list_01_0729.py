import sys
sys.stdin = open('input.txt','r')


for i in range(1, 11):
    count = 0
    test_len = int(input())
    tc = list(map(int, input().split()))

    for j in range(2, len(tc)-2):
        if tc[j] > tc[j-1] and tc[j] > tc[j-2] and tc[j] > tc[j+1] and tc[j] > tc[j+2]:
            max_val = 0
            for k in list([tc[j-2], tc[j-1], tc[j+1], tc[j+2]]):
                if k > max_val:
                    max_val = k
            count += (tc[j] - max_val)

    print('#{} {}'.format(i, count))








