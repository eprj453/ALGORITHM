import sys
sys.stdin = open('1_input.txt', 'r')

for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    codes = [list(input()) for _ in range(n)]
    result = 0
    password = ['1011000','1001100','1100100','1011110','1100010',
                '1000110','1111010','1101110','1110110','1101000']
    for j in range(n):
        if result == True:
            break
        if '1' not in codes[j]:
            continue
        else:
            for k in range(m-1, -1, -1):
                if codes[j][k] == '1':
                    ans = []
                    result = True
                    for l in range(k, k-56, -1):
                        if l < 0:
                            break
                        compare = codes[j][l]
                        for o in range(j, j + 5):
                            if compare != codes[o][l]:
                                result = False
                                break
                    if result == True:
                        for l in range(k, k-56, -7):
                            temp = ''
                            for o in range(l, l-7, -1):
                                temp += codes[j][o]
                            ans.insert(0, password.index(temp))
                        o_idx, e_idx, n_sum = 0, 0, 0
                        for num in range(len(ans)-1):
                            if num % 2:
                                o_idx += ans[num]
                            else:
                                e_idx += ans[num]
                            n_sum += ans[num]
                        if ((3 * e_idx) + o_idx + ans[len(ans) - 1]) % 10 == 0:
                            print('#{} {}'.format(i, n_sum + ans[len(ans)-1]))
                        else:
                            print('#{} {}'.format(i, 0))
                        break


            # print('j : ',j)
            # for k in range(m):
            #     temp = ''
            #     temp2 = []
            #     for l in range(k, k + 7):
            #         temp += codes[j][l]
            #     print(j, k)
            #     if temp in password and codes[j][k] == codes[j+1][k] and codes[j][k] == codes[j+2][k] \
            #             and codes[j][k] == codes[j+3][k] and codes[j][k] == codes[j+4][k]:
            #         temp2.append(password.index(temp))
            #         for o in range(k+7, k+56, 7):
            #             temp = ''
            #             for p in range(o, o+7):
            #                 temp += codes[j][p]
            #             temp2.append(password.index(temp))
            #
            #         o_idx, e_idx, temp_sum = 0, 0, 0
            #         for num in range(len(temp2)-1):
            #             if num%2:
            #                 o_idx += temp2[num]
            #             else:
            #                 e_idx += temp2[num]
            #             temp_sum += temp2[num]
            #
            #         if ((3*e_idx)+o_idx+temp2[len(temp2)-1]) % 10 == 0:
            #             result = str(temp_sum + temp2[len(temp2)-1])
            #         else:
            #             result = '0'
            #         break

