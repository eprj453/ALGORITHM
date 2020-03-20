def solution(n, lost, reserve):
    answer = 0

    students = [1 for i in range(n+2)]
    for r in reserve:
        students[r] += 1
    for l in lost:
        students[l] -= 1

    for r in reserve:
        if students[r-1] == 0:
            students[r-1] += 1
            students[r] -= 1
            continue
        elif students[r+1] == 0:
            students[r+1] += 1
            students[r] -= 1
            continue

    for s in students:
        if s > 0:
            answer += 1
    return answer