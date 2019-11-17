
import sys
sys.stdin = open('4013_input.txt', 'r')

for i in range(1, int(input())+1):
    k = int(input())
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    spins = [list(map(int, input().split())) for _ in range(k)]

    d = [-1, 1]
    for spin in spins:
        m = spin[0]-1
        is_spin = [0, 0, 0, 0]
        is_spin[m] = spin[1]
        for j in range(2):
            mag = m
            dir = spin[1]
            while 0 <= mag + d[j] < 4:
                if (d[j] == 1 and magnetics[mag][2] != magnetics[mag+d[j]][6]) or \
                    (d[j] == -1 and magnetics[mag][6] != magnetics[mag+d[j]][2]):
                    dir = - dir
                    is_spin[mag+d[j]] = dir
                else:
                    break
                mag += d[j]

        for s in range(len(is_spin)):
            if is_spin[s] == 1:
                temp = magnetics[s].pop()
                magnetics[s].insert(0, temp)
            elif is_spin[s] == -1:
                temp = magnetics[s].pop(0)
                magnetics[s].append(temp)

    mag_sum = (magnetics[0][0] * 1) + (magnetics[1][0] * 2) + (magnetics[2][0] * 4) + (magnetics[3][0] * 8)

    print('#{} {}'.format(i ,mag_sum))



            