import sys
sys.stdin = open('1865_input.txt', 'r')



def search(s, n, t_sum):
    global max_per
    if s == n:
        max_per = max(t_sum*100, max_per)

    else:
        for i in range(n):
            if visited[i]: continue
            else:
                if (t_sum * (nums[s][i]/100))*100 <= max_per:
                    continue

                visited[i] = True
                search(s+1, n, t_sum * (nums[s][i] / 100))
                visited[i] = False

for i in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    max_per = 0
    search(0, n, 1)

    print('#%d %.6f'%(i, max_per))

