
# # 방향키처럼 이동하기
# arr = [[9, 20, 2, 18, 11],[19, 1, 25, 3, 21],[8, 24, 10, 17, 7], [15, 4, 16, 5, 6],[12, 13, 22, 23, 14]]
#
# '''
# 09 20 02 18 11
# 19 01 25 03 21
# 08 24 10 17 07
# 15 04 16 05 06
# 12 13 22 23 14
# '''
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# tx, ty = 2, 2
# while True:
#     print('0: 위로, 1: 아래로 2: 좌 3: 우 4: 종료')
#     print('현재 좌표는 {}, {}'.format(tx, ty))
#     print('현재 위치는 {}입니다.'.format(arr[tx][ty]))
#
#     key = int(input())
#
#     if key == 4:
#         print('종료합니다.')
#         break
#
#     elif tx + dx[key] < 0 or ty + dy[key] < 0 or tx + dx[key] >= len(arr) or ty + dy[key] >= len(arr):
#         print('이동할 수 없습니다.')
#
#     else:
#         tx, ty = tx + dx[key], ty + dy[key]





# 인접 4요소 탐색하기
arr2 = [[9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

'''
09 20 02 18 11
19 01 25 03 21
08 24 10 17 07
15 04 16 05 06
12 13 22 23 14
'''

# print('탐색할 원소의 좌표는? : ')
# tx, ty = tuple(map(int, input().split()))

for i in range(len(arr2)): # 몇번째줄?
    for j in range(len(arr2[i])): #몇번째 원소?
        for key in range(len(dx)):
            if i + dx[key] < 0 or j + dy[key] < 0 or i + dx[key] >= len(arr2) or j + dy[key] >= len(arr2):
                print('탐색할 수 없는 원소')
            else:
                print(i, j)
                print(arr2[i+dx[key]][j + dy[key]])
            print('--------------------')
