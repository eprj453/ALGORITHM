def solution(gems):
    n = len(gems)
    all_gems = list(set(gems))

    gem_dict = {

    }

    left, right = 0, 0
    min_distance = 100_001
    memo_coop = [0, 0]
    while left <= right < n:
        print(left, right)
        if len(gem_dict) < len(all_gems):
            g = gems[right]
            gem_dict[g] = gem_dict.get(g, 0) + 1

        elif len(gem_dict) == len(all_gems):
            distance = right - left

            if distance < min_distance:
                min_distance = distance
                memo_coop = [left+1, right+1]

            g = gems[left]
            gem_dict[g] = gem_dict.get(g, 0) - 1

            if not gem_dict[g]:
                del gem_dict[g]

            left += 1

        if len(gem_dict) < len(all_gems):
            right += 1
    print(min_distance)
    return memo_coop

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY", "DIA", "SAPPHIRE", "EMERALD"]))

# "DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY", "DIA", "SAPPHIRE", "EMERALD"


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))