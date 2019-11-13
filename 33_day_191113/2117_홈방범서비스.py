import sys
sys.stdin = open('2117_input.txt', 'r')

'''
for i in range(1, int(input())+1):
    n = int(input())
    f = [list(map(int, input())) for _ in range(n)]
    x, y, f_sum = n//2, 0, 0
    for j in range(n):
        x2, y2 = x, y
        while x2 >= y:
            f_sum += f[x2][y2]
            x2 -= 1
            y2 += 1
        if j % 2:
            x += 1
        else:
            y += 1
    print('#{} {}'.format(i, f_sum))
'''


for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    maps = [list(input().split()) for _ in range(n)]
    k = 1
    max_house_count = 0
    while k < n+2:
        # print('돈다')
        # print("k : ", k)
        cost = k * k + (k-1) * (k-1)
        for j in range(n):
            for l in range(n):
                house_count = 0
                benefit = 0
                # print('j, l : ',j, l)
                s_x, s_y = j - k + 1, l
                start, end = 0, 2*k-1 # 3
                r = 1
                while start < end:
                    t = 0
                    tx, ty = s_x, s_y
                    while t < r:
                        if 0 <= tx < n and 0 <= ty < n:
                            if maps[tx][ty] == '1':
                                house_count += 1
                                benefit += m
                        ty += 1
                        t += 1
                    if start < end // 2:
                        r += 2
                        s_y -= 1
                        s_x += 1
                    else:
                        r -= 2
                        s_y += 1
                        s_x += 1

                    start += 1
                if benefit - cost >= 0:
                    max_house_count = max(max_house_count, house_count)
        k += 1

    print('#{} {}'.format(i, max_house_count))
        #         x, y = j-k+1, l # k=2일때 0,0이면 -1, 0부터 시작
        #         start = 1
        #         # x2, y2 = x, y
        #         print('x , y : ',x,y)
        #         for o in range(2*k-1):
        #             x2, y2 = x, y # 반복문 시작
        #             for p in range(x2, y2 + start):# start번만큼 반복
        #                 if 0 <= x2 < n and 0 <= y2 < n:
        #                     print(x2, p)
        #                     # print('y :', y2)
        #             if o <= k // 2:
        #                 y -= 1
        #                 start += 2
        #             else:
        #                 y += 1
        #                 start -= 2
        #             x += 1
        #             print()
        #             # x2, y2 = x, y
        #             # while x2 >= y-k:
        #             #     print(x2, y2)
        #             #     x2 -= 1
        #             #     y2 += 1
        #             # if o % 2:
        #             #     x += 1
        #             # else:
        #             #     y += 1
        #         print()
        # k += 1
        #         x, y = j, l-k+1
        #         for o in range(2*k-1):
        #             x2, y2 = x, y
        #             # print(x2, y2)
        #             while x2 >= y:
        #                 print(x2, y2)
        #                 x2 -= 1
        #                 y2 += 1
        #             if o % 2:
        #                 x += 1
        #             else:
        #                 y += 1
        #
        #         print()


    # print(maps)
    # max_benefit = 0
    # house_count = 0
    # kk = 1
    # while kk < n+1:
    #     cost = kk * kk + (kk - 1) * (kk - 1)
    #     print('cost : ',cost)
    #     is_escape = False
    #     for j in range(n):
    #         for k in range(n):
    #             # print('탐색 : ',j, k)
    #             benefit = 0
    #             houses = 0
    #             x, y = j, k - kk + 1
    #             count = 0
    #             for l in range(2*kk-1):
    #                 x2, y2 = x, y #
    #                 while x2 >= y:
    #                     if 0 <= x2 < n and 0 <= y2 < n:
    #                         print(x2, y2)
    #                         if maps[x2][y2] == '1':
    #                             benefit += m
    #                             houses += 1
    #                     x2 -= 1
    #                     y2 += 1
    #
    #                 if l % 2:
    #                     x += 1
    #                 else:
    #                     y += 1
    #                 print()
    #             if benefit - cost > 0:
    #                 house_count = max(houses, house_count)
    #     kk += 1
    #
    # print(house_count)
