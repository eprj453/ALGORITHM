def solution(arrangement):
    answer = 0
    stk = []
    for i in range(len(arrangement)):
        print(stk)
        if arrangement[i] == '(':
            stk.append(arrangement[i])
        else:
            if arrangement[i-1] == ")":
                answer += 1
            else:
                answer += (len(stk)-1)
            stk.pop()
    return answer

print(solution('()(((()())(())()))(())'))