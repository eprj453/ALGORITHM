t = int(input())

for i in range(1, t+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    print(N_list)
    min_val = N_list[0]
    max_val = N_list[0]
    for value in N_list:
        if value > max_val:
            max_val = value
        elif value < min_val:
            min_val = value
    print('#{} {}'.format(i, (max_val - min_val)))