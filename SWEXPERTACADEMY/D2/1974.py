def check_sudoku(sudoku_list):
    check_list = [0]*9
    result = 1
    for k in range(0, 9):
        if result == 0:
            break
        for i in range(0, 9):
            check_list[sudoku_list[k][i] - 1] += 1
        for check in check_list:
            if check != 1:
                result = 0
                break
        check_list = [0]*9
    return result



t = int(input())
for i in range(1, t+1):
    sudoku_list = [list(map(int, input().split())) for _ in range(9)]
    sudoku_list2 = []
    sudoku_list3 = []

    for j in range(9):
        temp = []
        for k in range(9):
            temp.append(sudoku_list[k][j])
        sudoku_list2.append(temp)

    temp = []
    n = 0
    m = 3
    for j in range(3):
        for k in range(0, 9):
            for l in range(n, m):
                temp.append(sudoku_list[k][l])
                if len(temp) == 9:
                    sudoku_list3.append(temp)
                    temp = []
        n += 3
        m += 3

    if check_sudoku(sudoku_list) and check_sudoku(sudoku_list2) and check_sudoku(sudoku_list3):
        result = 1
    else:
        result = 0

    print('#{} {}'.format(i, result))












    """
   0 012 0 345 0 678
   1 012 1 345 1 678
   2 012 2 345 2 678
   3 012 3 345 3 678
   4 012 4 345 4 678
   5 012 5 345 5 678
   6 012 6 345 6 678 
   7 012 7 345 7 678
   8 012 8 345 8 678
    
    
    """


    # if check_sudoku(sudoku_list) == 0:
    #     result += 1
    # if check_sudoku(sudoku_list2) == 0:
    #     result += 1
    #
    # for j in range(0, 8, 3):
    #     for k in range(3):






    # check_list = [0]*9
    # for k in range(0, 9):
    #     for i in range(0, 9):
    #         check_list[sudoku_list[k][i]-1] += 1
    # for check in check_list:
    #     if check != 0:
    #         print('#{} 0'.format(i))
    #
    # check_list = [0]*9

    # for k in range(0, 9):
    #     for i in range(0, 9):
    #         check = sudoku_list[k][i]
    #         sudoku_list[k].replace(sudoku_list[[k][i]], '*')
    #         if check in sudoku_list[k]:
    #             result = 0
    #         sudoku_list[k].replace('*', check)
    #
    # for k in range(0, 9):
    #     for i in range(0, 9):
    #         check = sudoku_list[i][k]
    #         sudoku_list[i].replace(sudoku_list[[i][k]], '*')
    #         if check in sudoku_list[k]:
    #             result = 0
    #         sudoku_list[k].replace('*', check)
    #

