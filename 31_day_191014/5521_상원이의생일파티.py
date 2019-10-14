import sys
sys.stdin = open('5521_input.txt', 'r')

for i in range(1, int(input())+1):
    n, m = map(int, input().split())

    u = []
    for _ in range(n+1):
        t = []
        u.append(t)
    for _ in range(m):
        a, b = map(int, input().split())
        u[a].append(b)
        u[b].append(a)

    invite = set()
    if u[1]:
        for k in range(len(u[1])):
            invite.add(u[1][k])
        for k in list(invite):
            for l in u[k]:
                if l != 1:
                    invite.add(l)

    print('#{} {}'.format(i, len(invite)))
    # print('#{} {}'.format(i, invite))