def solution(gems):

    n = len(gems)
    gem_dict = dict()
    gem_cnt = len(set(gems))
    answer_start, answer_end = 0, n

    start, end = 0, 0
    while end < n:
        if len(gem_dict) != gem_cnt:
            g = gems[end]
            gem_dict[g] = gem_dict.get(g, 0) + 1
            end += 1

        if len(gem_dict) == gem_cnt:
            while start < end:
                g = gems[start]
                gem_dict[g] -= 1
                if gem_dict[g] == 0:
                    if answer_end - answer_start > end - start:
                        answer_start, answer_end = start, end
                    start = end
                    gem_dict = dict()
                    break
                else:
                    start += 1

    return [answer_start+1, answer_end]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY", "DIA", "SAPPHIRE", "EMERALD"]))