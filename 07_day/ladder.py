import sys
sys.stdin = open('ladder_input.txt', 'r')

for i in range(1, 11):
    t = int(input())
    ladder_list = []
    for j in range(100):
        ladder_list.append(list(map(int, input().split())))

    result = ''
    for j in range(0, 100):
        if result != '':
            break
        if ladder_list[0][j] == 1:
            k, l = 1, j # 위치 좌표
            # print(k, l)
            status = 'under'
            while k < 100:
                if k == 99:
                    if ladder_list[k][l] == 2:
                        result = str(j)
                        break
                    else:
                        break

                if status == 'under': # 방향이 아래라면
                    if l != 0 and ladder_list[k][l-1] == 1: # 좌측이 1이라면?
                        l = l-1
                        # print(k, l)
                        status = 'left'
                    elif l != 99 and ladder_list[k][l+1] == 1: # 우측이 1이라면?
                        l = l+1
                        # print(k, l)
                        status = 'right'
                    else:
                        k = k + 1
                        # print(k, l)
                        status = 'under'

                if status == 'left':
                    if ladder_list[k+1][l] == 1:
                        k = k + 1
                        # print(k, l)
                        status = 'under'
                    else:
                        l = l - 1
                        # print(k, l)
                        status = 'left'

                if status == 'right':
                    if ladder_list[k+1][l] == 1:
                        k = k + 1
                        # print(k, l)
                        status = 'under'
                    else:
                        l = l + 1
                        # print(k, l)
                        status = 'right'

    print('#{} {}'.format(i, result))


