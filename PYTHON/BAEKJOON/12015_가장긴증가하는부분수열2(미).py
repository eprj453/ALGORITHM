n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(1, n):
    if arr[i] > arr[i-1]:
        answer += 1

answer = answer + 1 if answer else 0
print(answer)