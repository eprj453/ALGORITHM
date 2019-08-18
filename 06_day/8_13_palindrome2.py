# import sys
# sys.stdin = open('8_13_palindrome2_input.txt', 'r')



    #
    # 0 0 0 99
    # 0 1 0 98
    # 0 2 0 97
    # 다르면?
    # 0 0 0 98
    # 0 1 0 97
    # 0 2 0 96
    # 0 3 0 95
    # 다르면?
    # 0 0 0 97
    # 0 1 0 96
    # 0 2 0 95


    # for j in range(0, len(p_list)): # 행 도는 j 0~9
    #     for k in range(0, len(p_list[0])): # 인덱스 찾는 k 0~9
    #         for l in range(0, ):
    #             count = 0
    #             for m in range(len(p_list[0])-1-l, k, -1):
    #                 print(j, k, l ,m)
    #                 if p_list[j][k] == p_list[j][m+l]:

    # print('final : {}'.format(max_count))


import sys
sys.stdin = open('8_13_palindrome2_input.txt', 'r')

for i in range(10):
    t = int(input())
    p_list = []
    for j in range(100):
        p_list.append(list(input()))
    max_len = 1
    for j in range(0, len(p_list)):
        for k in range(0, len(p_list[0])-max_len+1):
            for l in range(k, len(p_list[0])):
                count = 0
                for m in range(0, ((len(p_list[0])) // 2)-(l // 2)):
                    if p_list[j][k+m] == p_list[j][len(p_list[0])-1-m-l+k]:
                        count += 1
                    else:
                        count = 0
                        break

                if count > 0 and len(p_list[0])-l > max_len:
                    max_len = len(p_list[0])-l

        for k in range(0, len(p_list[0])-max_len+1):
            for l in range(k, len(p_list[0])):
                count = 0
                for m in range(0, ((len(p_list[0])) // 2)-(l // 2)):
                    if p_list[k+m][j] == p_list[len(p_list[0])-1-m-l+k][j]:
                        count += 1
                    else:
                        count = 0
                        break

                if count > 0 and len(p_list[0])-l > max_len:
                    max_len = len(p_list[0])-l
    print('#{} {}'.format(t, max_len))