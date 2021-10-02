# 알파벳 찾기
from collections import OrderedDict

def solution(s):
    answer = ''
    alphabet_dict = OrderedDict()
    for a in s:
        lower_a = a.lower()
        alphabet_dict[lower_a] = alphabet_dict.get(lower_a, 0) + 1

    # print(alphabet_dict)

    max_count = max(alphabet_dict.values())
    max_dict = {k: v for k, v in alphabet_dict.items() if v == max_count}

    for except_alphabet in ['t', 'o', 's']:
        if max_dict.get(except_alphabet):
            upper_except_alphabet = except_alphabet.upper()
            if upper_except_alphabet == 'S':
                answer += (upper_except_alphabet * 2)
            else:
                answer += upper_except_alphabet

            del max_dict[except_alphabet]

    answer += ''.join(sorted(max_dict.keys())) if max_dict else ''
    return answer







solution('aaBBTtooSS')