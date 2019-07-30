t = int(input())
for i in range(1, t+1):
    nm_list = list(map(int, input().split()))
    int_list = list(map(int, input().split()))
    result_list = []
    for j in range(0, nm_list[0] - nm_list[1]+1):
        # print('j는 {}'.format(j))
        # print('nm_list[0] - nm_list[1]+1는 {}'. format(nm_list[0] - nm_list[1]+1))
        sum = 0
        for k in range(j, j + nm_list[1]):
            # print(int_list[k])
            sum += int_list[k]
        result_list.append(sum)
    # print('합계는 {}'.format(sum))
    max_val = result_list[0]
    min_val = result_list[0]
    for value in result_list:
        if value > max_val:
            max_val = value
        elif value < min_val:
            min_val = value
    print('#{} {}'.format(i, (max_val - min_val)))


