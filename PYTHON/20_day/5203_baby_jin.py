import sys
sys.stdin = open('5203_input.txt', 'r')

for i in range(1, int(input())+1):
    cards = list(map(int, input(). split()))
    p1, p2, result = [], [], 0
    for j in range(0, 12, 2):

        p1.append(cards[j])
        p1.sort()

        if len(p1) >= 3 and result == 0:
            for k in range(len(p1)-2):
                if (p1[k] == p1[k+1] == p1[k+2]) or \
                        (p1[k]+2 == p1[k+1]+1 == p1[k+2]):
                    result = 1
                    break

        p2.append(cards[j + 1])
        p2.sort()

        if len(p2) >= 3 and result == 0:
            for k in range(len(p2)-2):
                if (p2[k] == p2[k+1] == p2[k+2]) or \
                        (p2[k]+2 == p2[k+1]+1 == p2[k+2]):
                    result = 2
                    break

        if result: break

    print('#{} {}'.format(i, result))



