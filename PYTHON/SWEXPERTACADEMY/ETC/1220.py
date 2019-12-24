import sys
sys.stdin = open('1220_input.txt', 'r')

for i in range(1, 11):
    t = int(input())
    magnetic = []
    for j in range(t):
        magnetic.append(list(map(int, input().split())))

    crash = 0
    for j in range(t): # 0~99
        count = ''
        for k in range(t): # 0~99
            if magnetic[k][j] == 1 or magnetic[k][j] == 2:
                count += str(magnetic[k][j])
        for k in range(len(count)-1):
            if count[k] + count[k+1] == '12':
                crash += 1

    print('#{} {}'.format(i, crash))
