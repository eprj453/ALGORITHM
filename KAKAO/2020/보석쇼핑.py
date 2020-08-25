def solution(gems):
    answer = []
    start, end = 0, 0
    gems_set = set(gems)
    gems_len = len(gems_set)
    while gems_len < len(gems) + 1:
        if start or end:
            break
        i = 0
        while i < len(gems) - gems_len + 1:
            print(gems[i:i+gems_len])
            if gems_set == set(gems[i:i+gems_len]):
                start, end = i+1, i+gems_len
                break
            i += 1
        gems_len += 1
    answer = [start, end]
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))