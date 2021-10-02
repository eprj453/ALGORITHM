n, s = map(int, input().split(' '))
numbers = list(map(int, input().split()))
left, right = 0, 0

temp_sum = numbers[0]
shortest_len = 100000

while left <= right < n:
    print(left, right, temp_sum)
    if temp_sum < s:
        if right + 1 < n:
            right += 1
            temp_sum += numbers[right]
        else:
            break


    else:

        shortest_len = min(shortest_len, right - left + 1)
        temp_sum -= numbers[left]
        left += 1

answer = shortest_len if shortest_len != 100000 else 0
print(answer)
'''
6 20
5 5 5 10 10 7

2
'''