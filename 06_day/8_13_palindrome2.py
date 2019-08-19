import sys
sys.stdin = open('8_13_palindrome2_input.txt', 'r')


for i in range(10):
    t = int(input())
    p_list = []
    for j in range(100):
        p_list.append(list(input()))
    max_len = 1
    for j in range(0, len(p_list)):
        for k in range(0, len(p_list[0]) - max_len + 1):
            for l in range(k, len(p_list[0])):
                count = 0
                for m in range(0, ((len(p_list[0])) // 2) - (l // 2)):
                    if p_list[j][k + m] == p_list[j][len(p_list[0]) - 1 - m - l + k]:
                        count += 1
                    else:
                        count = 0
                        break

                if count > 0 and len(p_list[0]) - l > max_len:
                    max_len = len(p_list[0]) - l

        for k in range(0, len(p_list[0]) - max_len + 1):
            for l in range(k, len(p_list[0])):
                count = 0
                for m in range(0, ((len(p_list[0])) // 2) - (l // 2)):
                    if p_list[k + m][j] == p_list[len(p_list[0]) - 1 - m - l + k][j]:
                        count += 1
                    else:
                        count = 0
                        break

                if count > 0 and len(p_list[0]) - l > max_len:
                    max_len = len(p_list[0]) - l
    print('#{} {}'.format(t, max_len))