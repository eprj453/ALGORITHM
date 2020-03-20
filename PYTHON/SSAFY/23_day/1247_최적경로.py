import sys
sys.stdin = open('1247_input.txt', 'r')

def perm(s, e, distance_sum): # 1, 5, 0
    global min_distance
    if distance_sum >= min_distance:
        return

    if s == e:
        min_distance = min(min_distance, distance_sum + (abs(customers[temp[s-1]][0] - company[0]) + abs(customers[temp[s-1]][1] - company[1])))
        return

    else:
        for i in range(0, len(customers)): # 0, 5
            if visited[i]: continue
            else:
                temp[s] = list1[i]
                visited[i] = True
                if s == 0:
                    perm(s+1, e, distance_sum + (abs(home[0] - customers[temp[s]][0]) + abs(home[1] - customers[temp[s]][1])))
                else:
                    perm(s + 1, e, distance_sum + (abs(customers[temp[s-1]][0] - customers[temp[s]][0]) + abs(customers[temp[s-1]][1] - customers[temp[s]][1])))
                visited[i] = False



for i in range(1, int(input())+1):
    n = int(input())
    t = list(map(int, input().split()))
    # print(t)
    home, company = [], []
    customers = []
    for j in range(0, len(t), 2):
        if j == 0:
            home = [t[j], t[j+1]]
        elif j == 2:
            company = [t[j], t[j+1]]
        else:
            customers.append([t[j], t[j+1]])
    temp = [0] * len(customers)
    list1 = list(range(len(customers)))
    visited = [0] * len(customers)
    min_distance = 100 * 100
    perm(0, len(customers), 0)

    print('#{} {}'.format(i, min_distance))


    # perm(0, 6, 0)
