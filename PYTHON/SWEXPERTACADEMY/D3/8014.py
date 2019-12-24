import sys
sys.stdin = open('8014_input.txt', 'r')

tcs = int(input())
for t in range(1, tcs+1):
    nk = list(map(int, input().split())) # n = 4, k = 6
    n, k = nk[0], nk[1]
    #print(nk[0], nk[1])
    # 1등부터 6등은 순서대로 1~6조에
    # 7등부터 12등까지는 역순으로 1~6조에
    # 13등부터 18등까지는 순서대로 1~6조에
    # 19등부터 24등까지는 역순으로 1~6조에

    group_list = []
    for j in range(0, k):
        group_list.append([0]*n)


    rank = 1
    for i in range(0, n):
        for j in range(0, k):
            print(j - (((2*j)-(k-1)) * (i%2)), i)
            group_list[j - (((2*j)-(k-1)) * (i%2))][i] = rank # 짝수일때 정순 홀수일때 역순
            rank += 1

    print('#{}'.format(t), end=' ')
    for i in group_list:
        print(sum(i), end=' ')

    '''
    00
    10
    20
    30
    ---
    31
    21
    11
    01
    --
    02
    12
    22
    32
    --
    33
    23
    13
    03
    --
    04
    '''


