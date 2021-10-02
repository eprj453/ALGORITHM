def time_to_second(t):
    hour, minute, second = list(map(int, t.split(':')))
    return (hour * 3600) + (minute * 60) + second


def second_to_time(t):
    hour = t // 3600
    t -= (3600 * hour)
    minute = t // 60
    t -= (60 * minute)

    return f'{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(t).zfill(2)}'


def solution(play_time, adv_time, logs):
    answer = 0

    adv_start_time = 0
    end_time = time_to_second(play_time)
    adv_time = time_to_second(adv_time)

    time_arr = [0] * (end_time + 1)
    memo = [0] * (end_time + 1)

    for log in logs:
        log_start = time_to_second(log.split('-')[0])
        log_end = time_to_second(log.split('-')[1])

        memo[log_start] += 1
        memo[log_end] -= 1

    watching_user = 0

    for i in range(0, len(memo)):
        watching_user += memo[i]
        time_arr[i] = watching_user

    adv_start_limit = end_time - adv_time

    init_start_value = sum(time_arr[0:adv_time])
    if answer < init_start_value:
        answer = init_start_value

    answer_start = adv_start_time

    while adv_start_time <= adv_start_limit:
        adv_end_time = adv_start_time + adv_time

        if answer < init_start_value:
            answer = init_start_value
            answer_start = adv_start_time

        init_start_value -= time_arr[adv_start_time]
        init_start_value += time_arr[adv_end_time]
        adv_start_time += 1

    return second_to_time(answer_start)


a = solution(
    "99:59:59"	,
    "25:00:00"	,
    ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
)

print(a)

a = solution(
"02:03:55"	,"00:14:15",	 ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
)

print(a)

a = solution(
"50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
)

print(a)

arr = [1,2,3,4,5]

print(arr[0:3])