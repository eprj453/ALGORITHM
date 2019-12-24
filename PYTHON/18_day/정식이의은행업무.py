import sys
sys.stdin = open('4366_input.txt', 'r')

for i in range(1, int(input())+1):
    binary = list(map(int, input()))
    tetra = list(map(int, input()))
    bin_t, tet_t = [], []
    n = 0
    for j in range(len(binary)):
        b_t = []
        for k in range(len(binary)):
            b_t.append(binary[k])
        b_t[n] = 0 if b_t[n] == 1 else 1
        bin_t.append(''.join(map(str,(b_t))))
        n += 1

    n2 = 0
    for j in range(len(tetra)):
        t_t = []
        for k in range(len(tetra)):
            t_t.append(tetra[k])
        t_list = [0, 1, 2]
        t_list.remove(t_t[n2])
        for k in range(len(t_list)):
            t_t[n2] = t_list[k]
            tet_t.append(''.join(map(str,(t_t))))
        n2 += 1


    b_list, t_list = [], []
    for j in bin_t:
        n = len(binary)-1
        # print(j)
        b_ans = 0
        for k in range(len(j)):
            b_ans += (2**(n) * int(j[k]))
            n -= 1
        b_list.append(b_ans)

    for j in tet_t:
        n = len(tetra)-1
        t_ans = 0
        for k in range(len(j)):
            t_ans += (3**(n) * int(j[k]))
            n -= 1
        t_list.append(t_ans)

    # print(t_list)
    # print(b_list)
    # print(tet_t)
    # print(bin_t)

    ans = 0
    for j in t_list:
        if ans:
            break
        for k in b_list:
            if j == k:
                ans = j
                break

    print('#{} {}'.format(ans))
# for
#
#
# for i in range(len(a)):
#     ans += (3**(n) * int(a[i]))
#     n -= 1
# print(ans)