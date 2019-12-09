# def anagram(s, e, word):
#     if s == e:
#         print(temp)
#         return
#     else:
#         for k in range(s, )
import sys
sys.stdin = open('3816_input.txt', 'r')
for i in range(1, int(input())+1):
    s1, s2 = input().split()
    ans = 0
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    alpha_count = [0] * 26
    for s in s1:
        alpha_count[alphas.index(s)] += 1
    # print(alpha_count)
    temp_count = [0] * 26
    j = 0
    while j < len(s1):
        temp_count[alphas.index(s2[j])] += 1
        j += 1

    k = 0
    while k < len(s2) - len(s1) + 1:
        # print(temp_count)
        if alpha_count == temp_count:
            ans += 1

        if k == len(s2) - len(s1):
            break

        temp_count[alphas.index(s2[k])] -= 1
        temp_count[alphas.index(s2[k+len(s1)])] += 1
        # print(s2[k])
        # print(alphas.index(s2[k]))
        # print(s2[alphas.index(s2[k+len(s1)])])
        # temp_count[alphas.index(s2[k])] -= 1
        # temp_count[alphas.index(s2[k + len(s1)])] += 1
        k += 1
        # print('------------------------')
    print('#{} {}'.format(i, ans))



'''

슬라이딩 윈도우
누적합

'''