import sys
sys.stdin = open('5209_input.txt', 'r')

def perm(s, e, cost_cnt):
    global min_cost
    if cost_cnt >= min_cost:
        return
    if s == e:
        min_cost = min(cost_cnt, min_cost)
        return
    else:
        for i in range(len(t_list)):
            if visited[i]: continue
            else:
                temp[s] = t_list[i]
                visited[i] = True
                perm(s+1, e, cost_cnt + factory[s][temp[s]])
                visited[i] = False


for i in range(1, int(input())+1):
    n = int(input())
    factory = [list(map(int, input().split())) for _ in range(n)]
    t_list = list(range(n))
    temp = [0] * n
    visited = [False] * n
    min_cost = 15 * 15 * 99
    perm(0, n, 0)
    print('#{} {}'.format(i, min_cost))