paper = [list(input().split()) for _ in range(10)]
# visited = [[False] * 10 for _ in range(10)]
c_paper = [5,5,5,5,5]
count = 0
paper_width = 5
while paper_width > 0:

    for i in range(10-paper_width+1):
        for j in range(10-paper_width+1):
            if paper[i][j] == '1':
                result = True
                for k in range(i, i+paper_width):
                    if result == False:
                        break
                    for l in range(j, j+paper_width):
                        if paper[k][l] == '0':
                            result = False
                            break
                if result == True:
                    for k in range(i, i+paper_width):
                        for l in range(j, j+paper_width):
                            paper[k][l] = '0'
                    c_paper[paper_width-1] -= 1
                    if c_paper[paper_width-1] < 0:
                        count = -1
                        break
                    count += 1
    paper_width -= 1
print(c_paper)
print(count)

'''
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

'''
# for i in range(10):
#     for j in range(10):
#         if paper[i][j] == '1' and visited[i][j] == False:
#             print('found : ', i , j)
#             # x, y = i, j
#             visited[i][j] = True
#             n = 0
#             c = 0
#             result = True
#             while n < 5:
#                 if result == False:
#                     break
#                 for x in range(i, i+n):
#                     for y in range(j, j+n):
#                         print('탐색 : ',x, y)
#                         if paper[x][y] == '0':
#                             c = n-1
#                             result = False
#                             break
#                 print('------')
#                 if result == False:
#                     break
#                 n += 1
#                 # n += 1
#             print(c)
#             for x in range(i, i + c):
#                 for y in range(j, j + c):
#                     visited[x][y] = True
#             c_paper[n-1] -= 1
#             count += 1
#     # print(visited)



