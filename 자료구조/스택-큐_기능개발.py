from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    past_days = 0
    while progresses or speeds:
        print(answer)
        print(progresses)
        print(speeds)
        complete = 0
        prog, speed = progresses[0], speeds[0]
        if prog + (past_days * speed) >= 100:
            while progresses and progresses[0] + (past_days * speeds[0]) >= 100:
                progresses.popleft()
                speeds.popleft()
                complete += 1
            answer.append(complete)
            complete = 0
            past_days = 0
        else:
            remain_time = 100 - prog
            remain_days = remain_time // speed if remain_time % speed == 0 else (remain_time//speed)+1
            past_days += remain_days

    return answer

print(solution([93,30,55], [1,30,5]))