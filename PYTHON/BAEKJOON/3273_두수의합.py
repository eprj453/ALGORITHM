n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()

start, end = 0, n-1
answer = 0

while start < end:
    print(numbers[start], numbers[end])
    s = numbers[start] + numbers[end]
    if s == x:
        answer += 1
        end -= 1
        start += 1
    elif s > x:
        end -= 1
    else:
        start += 1
print(answer)