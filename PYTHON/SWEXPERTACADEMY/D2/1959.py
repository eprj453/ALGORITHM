t = int(input())
for i in range(1, t+1):
    ab_len = list(map(int, input().split()))
    answer = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        max = a
        min = b
    else:
        max = b
        min = a

    sum_list = []
    print(len(max)-len(min)+1)
    print(f'max는 {max}')
    print(f'min은 {min}')
    for j in range(0, len(max)-len(min)+1):
        sum = 0
        for k in range(j, len(min)+j):
            sum += max[k] * min[k-j]
        sum_list.append(sum)
    print(sum_list)
    answer = sum_list[0]
    for val in sum_list:
        if val > answer:
            answer = val

    print('#{} {}'.format(i, answer))