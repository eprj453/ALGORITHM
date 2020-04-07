cnt = 0

def ope(numbers, start, end, s, target):
    global cnt
    if start == end:
        if s == target:
            cnt += 1
        return

    # for i in range(start, end):
    ope(numbers, start+1, end, s + numbers[start], target)
    ope(numbers, start+1, end, s - numbers[start], target)

def solution(numbers, target):
    # global cnt
    answer = 0
    ope(numbers, 0, len(numbers), 0, target)
    answer = cnt
    return answer

print(solution([1,1,1,1,1], 3))