import sys
sys.stdin = open('2383_input.txt', 'r')

from collections import deque


def popPeople(arr, wait, stair, length):
    n = 0
    while n < len(arr):
        if arr[n] == 0:
            if len(arr) >= 3:
                wait.append(length)
            else:
                stair.append(length)
            arr.pop(n)
        else:
            arr[n] -= 1
            n += 1
    return arr, wait, stair

def subset(arr):
    for j in range(1 << len(arr)):
        arr_set = set(arr)
        arr_1, arr_2 = set(), set()
        for k in range(len(arr)):
            if j & (1 << k):
                arr_1.add(arr[k])
        arr_2 = arr_set - arr_1
        people_1, people_2 = list(arr_1), list(arr_2)

        if people_1:
            for i in range(len(people_1)):
                people_1[i] = abs(people[people_1[i]][0] - stairs[0][0]) + abs(people[people_1[i]][1] - stairs[0][1])
        if people_2:
            for i in range(len(people_2)):
                people_2[i] = abs(people[people_2[i]][0] - stairs[1][0]) + abs(people[people_2[i]][1] - stairs[1][1])

        go_to_lunch(people_1, people_2, [], [], [], [], 0)

def go_to_lunch(people1, people2, wait1, wait2, stair1, stair2, time):

    s1, s2 = maps[stairs[0][0]][stairs[0][1]], maps[stairs[1][0]][stairs[1][1]]

    global min_time

    if not people1 and not people2 and not wait1 and not wait2 and not stair1 and not stair2:
        min_time = min(min_time, time)
        return

    if people1:
        people1, wait1, stair1 = popPeople(people1, wait1, stair1)


    if people2:
        people2, wait2, stair2 = popPeople(people2, wait2, stair2)


    if stair1:
        n = 0
        temp = 0
        while n < len(stair1):
            stair1[n] -= 1
            if stair1[n] <= 0:
                temp += 1
            n += 1

        for t in range(0, temp):
            stair1.remove(0)


    if stair2:
        n2 = 0
        temp2 = 0
        while n2 < len(stair2):
            stair2[n2] -= 1
            if stair2[n2] <= 0:
                temp2 += 1
            n2 += 1
        # print('temp2 : ', temp2)
        # print('stair2 :', stair2)
        for t in range(0, temp2):
            stair2.remove(0)

    if len(stair1) < 3:
        if wait1:
            while wait1:
                if len(stair1) >= 3:
                    break
                wait1.pop(0)
                stair1.append(s1)

    if len(stair2) < 3:
        if wait2:
            while wait2:
                if len(stair2) >= 3:
                    break
                wait2.pop(0)
                stair2.append(s2)

    go_to_lunch(people1, people2, wait1, wait2, stair1, stair2, time+1)


for i in range(1, int(input())+1):
    n = int(input())
    people, stairs = [], []
    maps = []
    for j in range(n):
        temp = list(map(int, input().split()))
        for k in range(n):
            if temp[k] == 1:
                people.append([j, k])
            if 2 <= temp[k] <= 10:
                stairs.append([j, k])
        maps.append(temp)
    # print(people)
    # print(stairs)
    # print()
    people_len = len(people)
    min_time = 0xffffff
    # print(min_time)
    subset(list(range(people_len)))
    print('#{} {}'.format(i, min_time+1))
