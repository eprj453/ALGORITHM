paper_x, paper_y = map(int, input().split())
paper = []
for i in range(paper_y):
    paper.append([0] * paper_x)

cut_count = int(input())
lines = []
for i in range(cut_count):
    lines.append(list(map(int, input().split())))
max = 0
squares = [[0, 0, paper_y, paper_x, paper_x * paper_y]]

n = 0

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
            else:
                temp.append(square)
        squares = temp

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