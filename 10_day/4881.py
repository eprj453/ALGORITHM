import sys
sys.stdin = open('4881_input.txt', 'r')

def comb(s, e, nums_sum):
    global min_sum
    if nums_sum >= min_sum:
        return
    if s == e:
        min_sum = min(nums_sum, min_sum)
        return

    for i in range(len(temp)):
        if visited[i] : continue
        else:
            visited[i] = True
            comb(s+1, e, nums_sum + nums[s][i])
            visited[i] = False


for i in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 10 * 10
    temp = list(range(n))
    visited = [False] * n
    comb(0, n, 0)
    print('#{} {}'.format(i, min_sum))