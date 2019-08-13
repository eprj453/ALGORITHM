import sys
sys.stdin = open('8_13_palindrome2_input.txt', 'r')

for i in range(1, 11):
    t = int(input())
    p_list = []
    for j in range(100):
        p_list.append(input())

    '''
    0 0 0 99
    0 1 0 98
    0 2 0 97
    다르면?
    0 0 0 98
    0 1 0 97
    0 2 0 96
    0 3 0 95
    다르면?
    0 0 0 97
    0 1 0 96
    0 2 0 95

    '''

    count = 0
    max_val = 0
    for j in range(0, 100): # 열 번호
        for k in range(0, 100): # 0~99까지 탐색
            for l in range(99, max_val, -1): # 회문의 길이는 줄어듬
                for m in range(k, l):
                    # if j == 0:
                    #     print('{} {}, {} {}'.format(j, m, j, l-m))
                    if p_list[j][m] == p_list[j][l-m-1]:
                        count += 1
                    else:
                        count = 0
                        break

                if count > max_val:
                    max_val = count
                    count = 0
                    break

    '''
       0 0 99 0
       1 0 98 0
       2 0 97 0
       다르면?
       0 0 98 0
       1 0 97 0
       '''

    count = 0
    for j in range(0, 100):
        for k in range(0, 100):
            for l in range(99, max_val, -1):
                for m in range(k, l):
                    if p_list[m][j] == p_list[l-m-1][j]:
                        count += 1
                    else:
                        count = 0
                        break

                if count > max_val:
                    max_val = count
                    count = 0
                    break

    print('#{} {}'.format(i, max_val))

