t = int(input())

for i in range(1, t+1):
    nm = list(map(int, input().split()))
    n, m = nm[0], nm[1] # n : 배열 범위 n*n m : 파리채 크기 5, 2
    bug_list = []
    for j in range(0, n):
        bug_list.append(list(map(int, input().split())))

    sum = 0
    max_sum = 0
    for j in range(0, n-m+1): # 0
        for k in range(0, n-m+1): # row 순회
            for l in range(j, j+m):
                for o in range(k, k+m):
                    sum += bug_list[l][o]

            if sum > max_sum:
                max_sum = sum
            sum = 0

    print('#{} {}'.format(i, max_sum))

            # sum = bug_list[j][k] + bug_list[j][k+1] + bug_list[j+1][k] + bug_list[j+1][k+1]
            # if sum > max_sum:
            #     max_sum = sum


    print('#{} {}'.format(i, max_sum))
