def solution(p,s):
    answer = 0
    p, s = str(p), str(s)
    print(p)
    print(s)
    for i in range(len(p)):
        if p[i] == s[i]:
            print('same')
            continue
        else:
            print('num1 : {}, num2 : {}'.format(p[i], s[i]))
            num1, num2 = int(p[i]), int(s[i])
            solution1 = abs(num1 - num2)
            solution2 = (num1 + 9 - num2 + 1) if num1 < num2 else (9 - num1 + num2 +1)
            print(min(solution1, solution2))
            answer += min(solution1, solution2)
    return answer


# print(solution(82195, 64723))
print(solution(00000000000000000000, 91919191919191919191))