import sys
sys.stdin = open('5189_input.txt', 'r')

def search(s, e):
    # print('돈다')
    global ans
    if s == e:
        print(temp)
        min_sum = 0
        for i in range(n):
            # print(i, temp[i])
            min_sum += nums[i][temp[i]]
        ans = min(ans, min_sum)

    else:
        for i in range(n):
            if visited[i] or s == i: continue
            else:
                temp[s] = arr[i]
                visited[i] = True
                search(s+1, e)
                visited[i] = False


for i in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    arr = list(range(n))
    temp = [0] * n
    ans = 1000
    search(0, n)
    print(ans)


