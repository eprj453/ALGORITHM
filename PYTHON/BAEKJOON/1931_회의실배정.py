n = int(input())
meetings = [list(map(int, input().split(' '))) for _ in range(n)]
meetings.sort(key=lambda x: (x[0], x[1]))

meeting_schedule = []
current_meeting = None

for meeting in meetings:
    
    if not current_meeting:
        current_meeting = meeting
        continue
    
    current_meeting_start, current_meeting_end = current_meeting
    next_meeting_start, next_meeting_end = meeting
    
    if current_meeting_start <= next_meeting_start <= next_meeting_end <= current_meeting_end:
        current_meeting = meeting
    
    if next_meeting_start >= current_meeting_end:
        meeting_schedule.append(current_meeting)
        current_meeting = meeting
    

if not meeting_schedule:
    meeting_schedule.append(current_meeting)
else:
    last_meeting_end = meeting_schedule[-1][1]
    current_meeting_start = current_meeting[0]
    if last_meeting_end <= current_meeting_start:
        meeting_schedule.append(current_meeting)

answer = len(meeting_schedule)
print(answer)

    
    

