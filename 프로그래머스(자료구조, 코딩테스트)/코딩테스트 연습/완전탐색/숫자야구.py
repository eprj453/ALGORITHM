import copy
def game(compare, ans):
    ball, strike = 0, 0
    numCountDict = {}
    for i in range(3):
        if ans[i] == compare[i]:
            strike += 1
        else:
            numCountDict[ans[i]] = numCountDict.get(ans[i], 0) + 1
            numCountDict[compare[i]] = numCountDict.get(compare[i], 0) + 1

    for key, value in numCountDict.items():
        if value > 1:
            ball += 1

    return [strike, ball]

def solution(baseball):
    answer = set(str(x) for x in range(100, 1000) if '0' not in str(x)
                 and str[x][0] != str[x][1] and str[x][1] != str[x][2] and str[x][0] != str[x][2])
    for base in baseball:
        num, strike, ball = base[0], base[1], base[2]
        notAnswer = set()
        for ans in list(answer):
            strikeBall = game(str(num), str(ans))
            if strikeBall[0] != strike or strikeBall[1] != ball:
                notAnswer.add(ans)
        answer = answer - notAnswer
    print(answer)
    return len(answer)
#
print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
# print(solution([[333, 1, 0], [241, 0, 2], [917, 0, 1]]))

    # return answer