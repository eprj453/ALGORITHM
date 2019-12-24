import sys
sys.stdin = open('4881_input.txt', 'r')



t = int(input())
for i in range(1, t+1):
    n = int(input())
    min_val = 10000000
    perm_list = [list(map(int, input().split())) for _ in range(n)]
    perm_chk = list(range(n))
    visited = [False] * n
    t = [0] * n
    min_val = 10000000
    temp = 0
    def perm(k):
        global temp
        global ans
        global min_val
        if k == n:
            print(t)
            # print('calculate')
            # for j in range(n):
            #     temp += perm_list[j][t[j]]
            if temp < min_val:
                min_val = temp
                temp = 0
            else:
                temp = 0
        else:
            for j in range(n):
                if visited[j] == True:
                    continue
                t[k] = perm_chk[j]
                # temp += perm_list[perm_chk[j]][j]
                # print('k : ', k)
                print(k)
                print(j)
                print(t[k])
                print()
                # print('temp : ', temp)
                # print()
                visited[j] = True
                perm(k+1)
                visited[j] = False
        return min_val

    print('#{} {}'.format(i, perm(0)))
#
# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     min_val = 10000
#     perm_list = list(range(n))
#     nums = [list(map(int, input().split())) for _ in range(n)]
#     print(perm(0))

# t = int(input())
# for i in range(1, t+1):
#     n = int(input())
#     min_val = 10000000
#     perm_list = [list(map(int, input().split())) for _ in range(n)]
#     # [0, 1, 2]
#     for j in range():
#
#     print('#{}'.format(i))
