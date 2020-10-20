from datetime import datetime as dt, timedelta as td, time as t

def make_time(time):
    hour, minute, second = '', '', ''
    remain_hour = time // 3600
    hour = '0'+str(remain_hour) if len(str(remain_hour)) == 1 else str(remain_hour)

    remain_min = remain_hour % 60
    minute = '0'+str(remain_min) if len(str(remain_min)) == 1 else str(remain_min)

    remain_sec = remain_min % 60
    second = '0' + str(remain_sec) if len(str(remain_sec)) == 1 else str(remain_sec)

    return hour+":"+minute+":"+second


def solution(p,n):
    flag, time = p.split('')
    hour, minute, second = time.split(':')
    time = t.strftime('%I:%M:%S',)
    # print(time + td(minutes=200000))
    return answer

print(make_time(1))
# print()
# print(3800 % 3600)
# print(solution(0, 0))