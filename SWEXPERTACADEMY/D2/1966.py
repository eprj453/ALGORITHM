t = int(input())
for i in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    for j in range(n-1, 0, -1):
        for k in range(0, j):
            if num_list[k] > num_list[k+1]:
                num_list[k], num_list[k+1] = num_list[k+1], num_list[k]
    print('#{} {}'.format(i, ' '.join(list(map(str, num_list)))))


    # for j in range(n-1, -1, -1):
    #     if num_list[j] < num_list[j-1]:
    #         num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
    # print(num_list)
