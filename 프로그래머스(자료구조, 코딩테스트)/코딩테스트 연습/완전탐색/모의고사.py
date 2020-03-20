#  1, 2, 3, 4, 5, 1, 2, 3, 4, 5
#  2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5,
#  3, 3, 1, 1, 2, 2, 4, 4, 5, 5

def solution(answers):
    answer = []
    LenAns = len(answers)
    patterns = {
        1: '12345' * (LenAns // 5 + 1) if LenAns > 5 else '12345'[0:LenAns],
        2: '21232425' * (LenAns // 8 + 1) if LenAns > 8 else '21232425'[0:LenAns],
        3: '3311224455' * (LenAns // 10 + 1) if LenAns > 10 else '3311224455'[0:LenAns],
    }
    #
    scores = {
        1: 0,
        2: 0,
        3: 0,
    }

    print(patterns)
    print(type(patterns))
    for key, value in patterns.items():
        score = 0
        for i in range(len(answers)):
            if value[i] == str(answers[i]):
                score += 1
        scores[key] = score
        if answer:
            print(scores[answer[-1]])
            if scores[answer[-1]] < score:
                # answer.pop()
                # answer.append(key)
                answer = [key]
            elif scores[answer[-1]] == score:
                answer.append(key)
        else:
            answer.append(key)

    return answer

print(solution([1,2,3,4,5]))