t = int(input())
num_list = [2, 3, 5, 7, 11]
for i in range(1, t+1):
    multi_count = [0, 0, 0, 0, 0]
    n = int(input())
    # n이 20이라면?
    quotient = 0
    remainder = 0
    while quotient != 1:
        for j in range(0, len(num_list)):
            if n % num_list[j] == 0:
                multi_count[j] += 1
                quotient = n // num_list[j]
                n = quotient
                #print('몫은 {}'.format(quotient))

    print('#{} {}'.format(i, ' '.join(list(map(str, multi_count)))))