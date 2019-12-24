import sys
sys.stdin = open('4861_input.txt', 'r')

t = int(input())

for i in range(1, t+1):
    nm_list = list(map(int, input().split()))
    n, m = nm_list[0], nm_list[1]
    puzzle_list = []
    for j in range(n):
        puzzle_list += input().split()

    result = ''
    count = 0
    for j in range(0, len(puzzle_list)):
        if result != '':
            break
        for k in range(0, n-m+1): # m == 13
            for l in range(0, m // 2): # (0, 6)
                # if i == 3:
                #     print('{}, {} 비교'.format(puzzle_list[j][l+k], [j][m-l-1+k]))
                if puzzle_list[j][l+k] == puzzle_list[j][m-l-1+k]:
                    count += 1
                else:
                    count = 0
                    break

            if count == m // 2:
                print('{} 회문은 {},{}부터 {},{} 까지'.format(i, j, k, j, k+m-1))
                for num in range(k, k+m):
                    result += puzzle_list[j][num]
                break

    count = 0
    for j in range(0, len(puzzle_list)):
        if result != '':
            break
        for k in range(0, n-m+1):
            for l in range(0, m//2):
                if puzzle_list[l+k][j] == puzzle_list[m-l-1+k][j]:
                    count += 1
                else:
                    count = 0
                    break

            if count == m // 2:
                print('{} 회문은 {},{}부터 {},{} 까지'.format(i, k, j, k + m - 1, j))
                for num in range(k, k+m):
                    result += puzzle_list[num][j]
                break

    print('#{} {}'.format(i, result))

'''
0 1 2 3 4 5 6 7 8 9 10 11 12
'''