def solution(cookie):
    answer = 0

    for i in range(1, len(cookie)-1):
        left, right = i, i+1
        left_sum, right_sum = cookie[left], cookie[right]
        while True:
            if 0 < left and left_sum < right_sum:
                left -=1
                left_sum += cookie[left]
            elif right < len(cookie)-1 and left_sum > right_sum:
                right += 1
                right_sum += cookie[right]
            else:
                break
            if left_sum == right_sum:
                answer = max(answer, left_sum)

    return answer
print(solution([1,1,2,3]))

# print(solution([1,2,4,5]))
