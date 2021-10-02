def print_star(n, i):
    if i == 4:
        print(' ')

    if n == 1:
        print('*')

    for j in range(9):
        print_star(n - 1, j)

        if j in [2, 5, 8]:
            print('\n')
    # return star_str


for j in range(9):
    print(print_star(3, j), end='')
    if j in [2, 5, 8]:
        print('\n')
