t = int(input())
for i in range(1, t+1):

    n = int(input())
    array_list = []
    list_90 = []
    list_180 = []
    list_270 = []
    answer = ''

    for j in range(0, n):
        array_list += [list(map(int,input().split()))]

    for j in range(0, n):
        temp = []
        for k in range(n-1, -1, -1):
            temp.append(array_list[k][j])
        list_90.append(''.join(list(map(str, temp))))

    for j in range(n-1, -1, -1):
        temp = []
        for k in range(n-1, -1, -1):
            temp.append(array_list[j][k])
        list_180.append(''.join(list(map(str, temp))))

    for j in range(n-1, -1, -1):
        temp = []
        for k in range(0, n):
            temp.append(array_list[k][j])
        list_270.append(''.join(list(map(str, temp))))

    for j in range(0, n):
        if j == n-1:
            answer += (list_90[j]+' '+list_180[j]+' '+list_270[j])
            break
        else:
            answer += (list_90[j] + ' ' + list_180[j] + ' ' + list_270[j] + '\n')

    print('#{} {}'.format(i, '\n'+answer))