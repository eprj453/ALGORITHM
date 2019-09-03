n = int(input())
sc = [list(map(int, input().split())) for _ in range(n)]
# # print(sc)
done = [False] * n
# count = 0
# for i in range(len(sc)):
#     if sc[i][0] + i + 1 < n:



count = 0
ans = []
def sche(start, end):
    for i in range(start, end):
        # print(i)
        if sc[i][0] + i <= n:
            ans.append(sc[i][0])
            sche(i+1, end)
        else:
            print(ans)
            ans = []

sche(0, n)