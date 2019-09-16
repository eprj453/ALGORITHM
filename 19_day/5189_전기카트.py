import sys
sys.stdin = open('5189_input.txt', 'r')

def search(s, e):
    # print('돈다')
    if s == e:
        # print(f'--------{temp}---------')
        back(0, n, temp)

    else:
        for i in range(n):
            if visited[i] or s == i: continue
            else:
                temp[s] = arr[i]
                visited[i] = True
                search(s+1, e)
                visited[i] = False

def back(s, e, temp):
    global ans
    if s == e:
        print(temp2)
        min_sum = 0
        for i in range(len(temp2)):
            min_sum += nums[temp2[i]][i]
        ans = min(ans, min_sum)
    else:
        for i in range(n):
            if visited2[i] or s == i or temp[s] == arr[i]: continue
            else:
                temp2[s] = arr[i]
                visited2[i] = True
                back(s+1, e, temp)
                visited2[i] = False





for i in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    visited2 = [False] * n
    arr = list(range(n))
    temp = [0] * n
    temp2 = [0] * n
    ans = 1000
    search(0, n)
    print(ans)


