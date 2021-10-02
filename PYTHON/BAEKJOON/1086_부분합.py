n, s = list(map(int, input().split()))
numbers = list(map(int, input().split()))

# numbers.sort()

start, end = 0, 1
answer = 100_000


start_sum = numbers[start] + numbers[end]
print(numbers)
while start < end < n:
    print(numbers[start], numbers[end])
    print(start_sum)
    print()
    if start_sum >= s:
        answer = min(end - start + 1, answer)
        # print(start, end)
        start_sum -= numbers[start]
        start += 1

    else:
        start_sum += numbers[end+1]
        end += 1


answer = answer if answer != 100_000 else 0
print(answer)