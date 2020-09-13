from copy import deepcopy
def solution(new_id):

    new_id = list(new_id.lower().replace(' ', ''))
    temp_list = []
    print('sd')
    for i in range(len(new_id)):
        ch = new_id[i]
        if ch.isalpha() or ch.isdigit() or ch in '-_.':
            temp_list.append(ch)

    new_id = temp_list
    temp_list = []

    is_dot = False
    for ch in new_id:
        if ch == '.':
            is_dot = True
        else: # 문자일 경우
            if is_dot:
                temp_list.append('.')
                is_dot = False
            temp_list.append(ch)

    new_id = deepcopy(temp_list)
    temp_list = []

    if new_id[0] == '.':
        new_id.pop(0)
    if new_id[-1] == '.':
        new_id.pop()

    if len(new_id) > 15:
        new_id = new_id[:15]

    while len(new_id) < 3:
        new_id.append(new_id[-1])

    print(''.join(new_id))

    return ''.join(new_id)

print(solution("...!@BaT#*..y.abcdefghijkl m"))
# print(solution("...!@BaT#*..y.abcdefghijklm"))