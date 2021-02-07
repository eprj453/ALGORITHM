def is_duplicated(time1, time2):
    start, end = time1, time1 + 999

    t2_start, t2_end = get_start_end(time2)

    if start <= t2_start <= end or \
    start <= t2_end <= end or \
    t2_start <= start <= t2_end or \
    t2_start <= end <= t2_end:
        return True
    else:
        return False

def get_start_end(time):
    year_day, hour_second, process = time.split(' ')
    h, m, s = hour_second.split(':')
    s = s.replace('.', '')
    process = int(float(process[:-1]) * 1000)
    end = (int(h) * 3600000) + (int(m) * 60000) + int(s)
    start = end - (process+1)
    return (start, end)

def get_duplicate_count(end, time_list):
    dup_count = 0
    for time in time_list:
        if is_duplicated(end, time):
            dup_count += 1
    return dup_count

def solution(lines):
    answer = 0
    for idx, line in enumerate(lines):
        start, end = get_start_end(line)
        answer = max(answer, get_duplicate_count(end, lines))

    return answer

print(solution(
	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
))

