paper_list = []
count_list = []
square_list = []
for count in range(101):
    paper_list.append([0]*101)

n = int(input())
for i in range(n):
    square_list.append(list(map(int, input().split())))

for i in range(1, n+1):
    count = 0
    for j in range(square_list[i-1][0], square_list[i-1][0]+square_list[i-1][2]):
        for k in range(square_list[i-1][1], square_list[i-1][1] + square_list[i-1][3]):
            if paper_list[j][k] != 0:
                count_list[paper_list[j][k]-1] -= 1
                # print(j, k)
                paper_list[j][k] = i
                count += 1
            else:
                paper_list[j][k] = i
                count += 1
    count_list.append(count)

for count in count_list:
    print(count)

