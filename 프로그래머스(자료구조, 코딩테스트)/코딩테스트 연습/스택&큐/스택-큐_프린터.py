from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque()
    prioritiesList = [0] * 10
    printCount = 1
    for i in range(len(priorities)):
        deq.append([i, priorities[i]])
        prioritiesList[priorities[i]] += 1
    while deq:
        prioritie = deq.popleft()
        idx, rank = prioritie[0], prioritie[1]
        canPrint = True
        for j in range(rank+1, len(prioritiesList)):
            if prioritiesList[j] > 0:
                deq.append([idx, rank])
                canPrint = False
                break
        if canPrint: # 인쇄한다.
            if idx == location:
                return printCount
            else:
                prioritiesList[rank] -= 1
                printCount+=1




    return printCount

print(solution([1, 1, 9, 1, 1, 1], 0))