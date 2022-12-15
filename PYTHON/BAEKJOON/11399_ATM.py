n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = []

for i in arr:
    withdrawal_time = i + answer[-1] if answer else i
    answer.append(withdrawal_time)

print(sum(answer))