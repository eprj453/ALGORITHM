import sys
sys.stdin = open('8_13_palindrome1_input.txt', 'r')

for i in range(1, 11):
    n = int(input()) # n = 4
    p_list = []
    for j in range(8):
        p_list.append(input())
    # if i == 2:
    #     print(p_list)
    # print(p_list)
    result_count = 0

    count = 0
    for j in range(len(p_list)):
        for k in range(8-n+1): # k : 0 ~ 5 (4까지 탐색)
            if i == 2:
                print('가로 k : {}-----------------'.format(k))
            for l in range(0, n // 2): # l : 0 ~ 2 0,1 순차
                if i == 2:
                    print('l : {}'.format(l))
                    print(j,l + k,j, n - l + k - 1)
                    print(p_list[j][l+k], p_list[j][n-l+k-1])
                if p_list[j][l+k] == p_list[j][n-l+k-1]:
                    count += 1
                    print('가로에서 count 추가', count)
                else:
                    count = 0
                    break

            if count == n // 2:
                result_count += 1
                count = 0
                if i == 2:
                    print('result count 추가 {}'.format(result_count))

    count = 0
    for j in range(len(p_list)):
        for k in range(8 - n + 1):  # k : 0 ~ 5 (4까지 탐색)
            if i == 2:
                print('세로 k : {}-----------------'.format(k))
            for l in range(0, n // 2):  # l : 0 ~ 2 0,1 순차
                if i == 2:
                    print('l : {}'.format(l))
                    print(j,l + k,j, n - l + k - 1)
                    print(p_list[l+k][j], p_list[n-l+k-1][j])
                if p_list[l+k][j] == p_list[n-l+k-1][j]:
                    count += 1
                    print('세로에서 count 추가', count)
                else:
                    count = 0
                    break

            if count == n // 2:
                result_count += 1
                count = 0
                if i == 2:
                    print('result count 추가 {}'.format(result_count))

    print('#{} {}'.format(i, result_count))
                # print('{} 회문은 {},{}부터 {},{} 까지'.format(i, j, k, j, k+n-1))


