import sys
sys.stdin = open('ladder_input.txt', 'r')

for i in range(10):
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
            under = [1, 0]
            left = [0, -1]
            right = [0, 1]

            status = under
            while k < 100:
                if status == under: # 방향이 아래라면
                    if ladder_list[k][l-1] == 1: # 좌측이 1이라면?
                        k, l = k, l-1
                        status = left
                    elif ladder_list[k][l+1] == 1: # 우측이 1이라면?
                        k, l = k, l+1
                        status = right

                    else:
                        k, l = k+1, l
                        status = under

                if status == left:
                    if ladder_list[k+1][l] == 1:
                        k, l = k+1, l
                        status = under
                    else:
                        k, l = k, l-1
                        status = left

                if status == right:
                    if ladder_list[k+1][l] == 1:
                        k, l = k+1, l
                        status = under
                    else:
                        k, l = k, l+1
                        status = right


                if k == 99:
                    if ladder_list[k][j] == 2:
                        result = str(j)
                        break
                    else:
                        break

    print(result)


