t = int(input())

for i in range(1, t+1):
    time_list = list(map(int, input().split()))
    print(time_list)
    hour = 0
    minute = 0

    for k in range(0, len(time_list)):
        if k % 2:
            minute += time_list[k]
        else:
            hour += time_list[k]
    print(hour)
    print(minute)

    if minute >= 60:
        minute -= 60
        hour += 1

    if hour > 12:
        hour -= 12

    print('#{} {} {}'.format(i, hour, minute))
