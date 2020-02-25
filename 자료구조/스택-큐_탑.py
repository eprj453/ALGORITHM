def solution(heights):
    answer = [0] * len(heights)
    stk = [ [heights[-1], len(heights)-1] ] # 높이값, 인덱스값
    for h in range(len(heights)-1, -1, -1):
        while stk:
            x, y = stk[-1][0], stk[-1][1]  # 스택 최상단의 높이값, 인덱스값
            if x < heights[h]:
                answer[y] = h+1
                stk.pop()
            else:
                break
        stk.append([heights[h], h])
    return answer

print(solution([1,5,3,6,7,6,5]))