from itertools import combinations
def solution(orders, course):
    answer = []
    menu_dict = {}
    for order in orders:
        for i in range(2, len(order)+1):
            if i in course:
                comb = combinations(order, i)
                for c in comb:

                    c = tuple(sorted(list(c)))
                    print(c)
                    menu_dict[c] = menu_dict.get(c, 0) + 1

    print(menu_dict)
    answer_dict = {}

    for key, value in [(key, value) for key, value in menu_dict.items() if value >= 2]:
        k, v = len(key), value

        if answer_dict.get(k): # 이미 존자
            present_max = answer_dict.get(k).get('max')
            if present_max == v:
                answer_dict.get(k).get('list').append(key)
            elif present_max < v:
                answer_dict.get(k)['max'] = v
                answer_dict.get(k)['list'] = [key]
        else:
            answer_dict[k] = {
                'max': v,
                'list': [key]
            }
    for value in answer_dict.values():
        for v in value.get('list'):
            answer.append(''.join(list(v)))

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))