import sys
sys.stdin = open('8_13_palindrome1_input.txt', 'r')

for i in range(1, 11):
    n = int(input())  # n = 4
    p_list = []
    for j in range(8):
        p_list.append(input())

    result_count = 0

    count = 0
    for j in range(len(p_list)):
        for k in range(8 - n + 1):
            for l in range(0, n // 2):
                if p_list[j][l + k] == p_list[j][n - l + k - 1]:
                    count += 1
                else:
                    count = 0
                    break

            if count == n // 2:
                result_count += 1
                count = 0

    count = 0
    for j in range(len(p_list)):
        for k in range(8 - n + 1):
            for l in range(0, n // 2):
                if p_list[l + k][j] == p_list[n - l + k - 1][j]:
                    count += 1
                else:
                    count = 0
                    break

            if count == n // 2:
                result_count += 1
                count = 0

    print('#{} {}'.format(i, result_count))
                # print('{} 회문은 {},{}부터 {},{} 까지'.format(i, j, k, j, k+n-1))


