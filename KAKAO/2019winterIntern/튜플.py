def solution(s):
    answer = []
    number_dict = {}
    i = 2
    temp = ''
    while i < len(s)-1:
        if s[i].isdigit():
            temp += s[i]
        else:
            if temp:
                number_dict[temp] = number_dict.get(temp, 0) + 1
            temp = ''
        i += 1
    reverse_dict = {v : k for k, v in number_dict.items()}
    for i in sorted(reverse_dict.keys(), reverse=True):
        answer.append(int(reverse_dict[i]))
    return answer

di = {1: 1, 2:2, 3: 3}
print(len(di))