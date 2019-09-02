import sys
sys.stdin = open('s_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    bus = [0]
    ans = []
    for j in range(n):
        a, b = map(int, input().split())
        # print(a, b)
        for k in range(a-1, b): # 1, 4
            if bus[k]:
                bus[k] += 1
            else:
                bus.insert(k, 1)
    print(bus)
    # for j in range(n):
    #     bus.append(list(map(int, input().split())))
    p = int(input())
    print('#{}'.format(i), end = ' ')
    # print('#{} {}'.format(i, ' '.join(bus)))
    for j in range(p):
        c = int(input())
        if c <= len(bus):
            ans.append(str(bus[c-1]))
        else:
            ans.append('0')
    print('#{} {}'.format(i, ' '.join(ans)))
# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     bus = [0] * 5000
#     ans = []
#     for j in range(n):
#         a, b = map(int, input().split())
#         for k in range(a-1, b):
#             bus[k] += 1
#     p = int(input())
#     for j in range(p):
#         c = int(input())
#         ans.append(str(bus[c-1]))
#     print('#{} {}'.format(i,' '.join(ans)))