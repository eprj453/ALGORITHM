import sys
sys.stdin = open('2805_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n = int(input()) # 5
    farm_list = []

    for j in range(n):
        farm_list.append(list(map(int, input())))

    farm_sum = 0

    for j in range(0, (n//2)+1):
        farm_sum += farm_list[n // 2 - j][n // 2]
        farm_sum += farm_list[n // 2 + j][n // 2]
        for k in range(1, (n//2)-j+1):
            if j == 0:
                # print(n // 2, (n // 2) - k)
                # print(n // 2, (n // 2) + k)
                # print('-----------------')
                farm_sum += farm_list[n // 2][(n // 2) - k]
                farm_sum += farm_list[n // 2][(n // 2) + k]

            else:
                # print((n // 2) - j, (n // 2) + k)
                # print((n // 2) - j, (n // 2) - k)
                # print((n // 2) + j, (n // 2) + k)
                # print((n // 2) + j, (n // 2) - k)
                farm_sum += farm_list[(n // 2) - j][(n // 2) + k]
                farm_sum += farm_list[(n // 2) - j][(n // 2) - k]
                farm_sum += farm_list[(n // 2) + j][(n // 2) + k]
                farm_sum += farm_list[(n // 2) + j][(n // 2) - k]

        # print('------------------')
    farm_sum -= farm_list[n//2][n//2]
    print('#{} {}'.format(i, farm_sum))




        # if center1[0] == center2 == [0] and center1[1] == center2[1]: # 맨 중앙일때
        #     farm_sum += farm_list[center1[0]][center1[1]]
        #     print('center center1 : {}'.format(farm_list[center1[0]][center1[1]]))
        #     print('center center2 : {}'.format(farm_list[center2[0]][center2[1]]))
        #     for k in range(n // 2, 0, -1):  # 2, 1
        #         print('+{} center'.format(farm_list[center1[0]][center1[0]+k]))
        #         print('+{} center'.format(farm_list[center1[0]][center1[0]-k]))
        #         farm_sum += (farm_list[center1[0]][center1[0]+k] + farm_list[center1[0]][center1[0]-k])
        # else:
        #     print('no_center center1 : {}'.format(farm_list[center1[0]][center1[1]]))
        #     print('no_center center2 : {}'.format(farm_list[center2[0]][center2[1]]))
        #     print(farm_list[center1[0]][center1[1]])
        #     print('j : {}'.format(j))
        #     print('------------')
        #     farm_sum += (farm_list[center1[0]][center1[1]] + farm_list[center2[0]][center2[1]])
        #     for k in range(n//2, 0, -1):
        #         print('+{} no_center'.format(farm_list[center1[0]][center1[0] + k]))
        #         print('+{} no_center'.format(farm_list[center1[0]][center1[0] - k]))
        #         farm_sum += (farm_list[center1[0]][center1[0] + k] + farm_list[center1[0]][center1[0] - k])
        #         farm_sum += (farm_list[center2[0]][center2[0] + k] + farm_list[center2[0]][center2[0] - k])

        #
        # print('farm_sum : {}'.format(farm_sum))

'''
        0,2
    1,1 1,2 1,3
2,0 2,1 2,2 2,3 2,4
    3,1 3,2 3,3
        4,2

'''

