# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# answer -> 2

# 2 4
# 7 3 1 8
# 3 3 3 4
# answer -> 3

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = max([min(arr[i]) for i in range(n)])
print(answer)
