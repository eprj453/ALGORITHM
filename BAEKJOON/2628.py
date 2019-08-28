paper_x, paper_y = map(int, input().split())
paper = []
for i in range(paper_y):
    paper.append([0] * paper_x)
<<<<<<< HEAD
# print(paper)
=======

>>>>>>> e461e5d66bbf678b46626e6879bc954aa37b9692
cut_count = int(input())
lines = []
for i in range(cut_count):
    lines.append(list(map(int, input().split())))
max = 0
<<<<<<< HEAD
squares = [[0, 0, paper_y, paper_x, paper_x * paper_y]] # 0 0 8 10 80

n = 0
# while n < cut_count:
#     if lines[n] == 0:

for line in lines:
    # square_temp = squares
    if line[0] == 0: # 0, 3 가로절단
        # print(squares)
        # print('가로절단')
        # print('검사 전 squares : {}'.format(squares))
        square_temp = squares
        temp = []
        for square in square_temp:
            # print('square_temp : {}'.format(square_temp))
            if square[0] < line[1] and line[1] < square[2]: # 사각형 범위 안에 걸린다면
                # print('square 절단 {}'.format(square))
                # temp.append(square)
=======
squares = [[0, 0, paper_y, paper_x, paper_x * paper_y]]

n = 0

for line in lines:
    if line[0] == 0:
        square_temp = squares
        temp = []
        for square in square_temp:
            if square[0] < line[1] and line[1] < square[2]:
>>>>>>> e461e5d66bbf678b46626e6879bc954aa37b9692
                temp.append(
                    [square[0],square[1],line[1],square[3],((line[1]-square[0])*(square[3]-square[1]))])
                temp.append(
                    [line[1], square[1], square[2], square[3],((square[2]-line[1])*(square[3]-square[1]))])
<<<<<<< HEAD
                # squares.remove(square)
            else:
                temp.append(square)
        squares = temp
        # print('검사 후 squares : {}'.format(squares))

    elif line[0] == 1: # 0,0,3,10 30
        # print('세로절단')
        # print('검사 전 sqaures: {}'.format(squares))
        square_temp = squares
        temp = []
        # print('square_temp : {}'.format(square_temp))
        for square in square_temp:
            if square[1] < line[1] and line[1] < square[3]:  # 사각형 범위 안에 걸린다면
                # temp.append(square)
                # print('square 절단 {}'.format(square))
=======
            else:
                temp.append(square)
        squares = temp

    elif line[0] == 1:
        square_temp = squares
        temp = []
        for square in square_temp:
            if square[1] < line[1] and line[1] < square[3]:
>>>>>>> e461e5d66bbf678b46626e6879bc954aa37b9692
                temp.append(
                    [square[0],square[1],square[2],line[1],((square[2]-square[0])*(line[1]-square[1]))])
                temp.append(
                    [square[0],line[1],square[2],square[3],((square[2]-square[0])*(square[3]-line[1]))])
<<<<<<< HEAD
                # squares.remove(square)
            else:
                temp.append(square)
        squares = temp
        # print('검사 후 squares : {}'.format(squares))
    # print(squares)
=======
            else:
                temp.append(square)
        squares = temp

>>>>>>> e461e5d66bbf678b46626e6879bc954aa37b9692

max_val = 0
for check in squares:
    if check[4] > max_val:
        max_val = check[4]

<<<<<<< HEAD
print(max_val)



# min_y, min_x = 0, 0
# max_y, max_x = paper_y, paper_x
# # max_len = [[min_y, min_x],[max_y, max_x]] # [0,0] [8,10]
# for line in lines:
#     print(line)
#     if line[0] == 0: # 가로절단
#         # print('가로절단')
#         if line[1] >= max_y or line[1] <= min_y: # 최대 넓이보다 큰 곳이나 최대 넓이보다 작은 곳을 자르려하면
#             continue    # 무시
#         else:
#             if line[1]-min_y > max_y-line[1]: # 잘린쪽 중 큰 쪽을 다시 범위로
#                 max_y = line[1]
#             else:
#                 min_y = line[1]
#     if line[0] == 1:
#         # print('세로절단')
#         if line[1] > max_x or line[1] <= min_x:
#             continue
#         else:
#             if line[1]-min_x > max_x - line[1]:
#                 max_x = line[1]
#             else:
#                 min_x = line[1]
# #     print(min_y, min_x, max_y, max_x)
# # print(min_y, min_x, max_y, max_x)
# # print(max_len)
# print((max_x - min_x) * (max_y - min_y))
=======
print(max_val)
>>>>>>> e461e5d66bbf678b46626e6879bc954aa37b9692
