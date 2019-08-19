# import sys
# sys.stdin = open('8_13_palindrome2_input.txt', 'r')



for i in range(1, 11):
    max_count = 0
    t = int(input())
    p_list = []
    for j in range(100):
        p_list.append(input())

    for j in range(0, len(p_list)):  # 행 도는 j 0~9
        for k in range(0, len(p_list[0])):  # 인덱스 찾는 k 0~9
            for l in range(len(p_list[0]) - k, k, -1):
                count = 0
                for m in range(0, (len(p_list[0]) - k) // 2):
                    # print(j, k, l ,m)
                   # print(f' 가로 {j}, {k + m}, {j}, {l + k - m - 1}')
                    if p_list[j][k + m] == p_list[j][l + k - m - 1]:  # k = 0 l = 10-0
                        count += 1

                        # print('max_count : {}'.format(max_count))
                    else:
                        count = 0
                    #    print('break!')
                        break
                if count > max_count:
                  #  print('count : {}'.format(count))
                    max_count = count
                   # print('max_count : {}'.format(max_count))
                    # print('max_count : {}'.format(max_count))
                    count = 0
                    break

    print(max_count)

    for j in range(0, len(p_list)):  # 행 도는 j 0~9
        for k in range(0, len(p_list[0])):  # 인덱스 찾는 k 0~9
            for l in range(len(p_list[0]) - k, k, -1):
                count = 0
                for m in range(0, (len(p_list[0]) - k) // 2):
                    # print(j, k, l ,m)
                    #print(f' 가로 {j}, {k + m}, {j}, {l + k - m - 1}')
                    if p_list[k + m][j] == p_list[l + k - m - 1][j]:  # k = 0 l = 10-0
                        # if count < (k + m) - (l + k - m - 1)  + 1:
                        #     count = (k + m) - (l + k - m - 1) + 1
                        # if count > max_count:
                        #     break
                        count +=1
                        # print('max_count : {}'.format(max_count))
                    else:
                        count = 0
                     #   print('break!')
                        break
                if count > max_count:
                    #print('count : {}'.format(count))
                    max_count = count
                    #print('max_count : {}'.format(max_count))
                    # print('max_count : {}'.format(max_count))
                    count = 0
                    break
    print('final : {}'.format(max_count))
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

    # for j in range(0, len(p_list)): # 행 도는 j 0~9
    #     for k in range(0, len(p_list[0])): # 인덱스 찾는 k 0~9
    #         for l in range(0, ):
    #             count = 0
    #             for m in range(len(p_list[0])-1-l, k, -1):
    #                 print(j, k, l ,m)
    #                 if p_list[j][k] == p_list[j][m+l]:

    print('final : {}'.format(max_count))


