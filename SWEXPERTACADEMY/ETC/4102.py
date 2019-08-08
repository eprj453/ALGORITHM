import sys
sys.stdin = open('4012_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    food_list = []
    for j in range(n):
        food_list.append(list(map(int, input().split())))

    

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