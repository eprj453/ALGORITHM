def solution(m, k):
    answer = ''
    i = 0
    for idx, ch in enumerate(m):
        if i == len(k) or m[idx] != k[i]:
            answer += ch
        else:
            i += 1
    return answer
# print(solution('kkaxbycyz', 'abc'))
print(solution("acbbcdc", "abc"))