import sys
sys.stdin = open('4012_input.txt', 'r')

from collections import deque

def comb(s, start):
    if s == n // 2:
        all_food = set(arr)
        food1 = set(temp)
        food2 = all_food - food1
        # print(list(food1))
        # print(food2)
        make_food(list(food1), list(food2))
        return
    else:
        for k in range(start, n):
            temp.append(arr[k])
            comb(s+1, k+1)
            temp.pop()

def make_food(arr1, arr2):
    global min_differ

    first_food, second_food = 0, 0

    for j in range(len(arr1)):
        for k in range(j,len(arr2)):
            x, y = arr1[j], arr1[k]
            x2, y2 = arr2[j], arr2[k]
            first_food += (foods[x][y] + foods[y][x])
            second_food += (foods[x2][y2] + foods[y2][x2])

    min_differ = min(abs(first_food - second_food), min_differ)





for i in range(1, int(input())+1):
    n = int(input())
    foods = [list(map(int, input().split())) for _ in range(n)]
    temp = []
    arr = list(range(n))
    min_differ = 0xffffff
    comb(0, 0)
    print('#{} {}'.format(i, min_differ))
