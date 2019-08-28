paper_x, paper_y = map(int, input().split())
paper = []
for i in range(paper_y):
    paper.append([0] * paper_x)

# print(paper)

cut_count = int(input())
lines = []
for i in range(cut_count):
    lines.append(list(map(int, input().split())))
max = 0

squares = [[0, 0, paper_y, paper_x, paper_x * paper_y]] # 0 0 8 10 80

for line in lines:
    if line[0] == 0:
        square_temp = squares
        temp = []
        for square in square_temp:
            if square[0] < line[1] and line[1] < square[2]:

                temp.append(
                    [square[0],square[1],line[1],square[3],((line[1]-square[0])*(square[3]-square[1]))])
                temp.append(
                    [line[1], square[1], square[2], square[3],((square[2]-line[1])*(square[3]-square[1]))])

                # squares.remove(square)
            else:
                temp.append(square)
        squares = temp
        # print('검사 후 squares : {}'.format(squares))

    elif line[0] == 1:
        square_temp = squares
        temp = []
        for square in square_temp:
            if square[1] < line[1] and line[1] < square[3]:
                temp.append(
                    [square[0],square[1],square[2],line[1],((square[2]-square[0])*(line[1]-square[1]))])
                temp.append(
                    [square[0],line[1],square[2],square[3],((square[2]-square[0])*(square[3]-line[1]))])
            else:
                temp.append(square)
        squares = temp


max_val = 0
for check in squares:
    if check[4] > max_val:
        max_val = check[4]

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

