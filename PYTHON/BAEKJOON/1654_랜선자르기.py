n, k = list(map(int, input().split()))

lines = []
for _ in range(n):
    lines.append(int(input()))

lines.sort()

answer = 0
start, end = 0, lines[-1]

while start <= end:
    mid = (start + end) // 2

    line_cnt = sum([x // mid for x in lines])

    if line_cnt >= k: # 라인이 너무 많이 생기는 경우 길이를 좀 늘려도 됨
        start = mid + 1
        answer = max(mid, answer)
    else:
        end = mid - 1

print(answer)
# print(3//0)
print(1//2)
