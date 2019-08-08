import sys
sys.stdin = open('4012_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    food_list = []
    for j in range(n):
        food_list.append(list(map(int, input().split())))

    taste = 10000000000
    for j in range(len(food_list)):
        a, b = 0, 0
        a_sum, b_sum = 0
        for k in range(len(food_list[0])):
            if j == k:
                pass
            else:
                a += food_list[j][k]
                a += food_list[k][j]
            for m in range(len(food_list)):
                for l in range(len(food_list[0])):
                    if m == l or (j == m and k == l):
                        pass
                    else:
                        b += food_list[m][l]
                        b += food_list[l][m]
            if abs(a+b) < taste:
                taste = abs(a+b)

    print(taste)



'''
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
4
0 7 1 1
7 0 6 2
1 1 0 2
10 1 9 0
'''