def solution(registered_list, new_id):
    print(registered_list)
    print(new_id)
    answer = ''
    regist_set = set(registered_list)
    r_len = len(regist_set)
    regist_set.add(new_id)
    if len(regist_set) != r_len:
        print('exist')
        return new_id
    else:
        i = 0
        while i < len(new_id):
            if new_id[i].isdigit():
                break
            i += 1
        print(i)
        S, N = new_id[:i], new_id[i:]
        n = 1
        if N:
            n = int(N)
        while len(str(n)) <= 6:
            recommend = S + str(n)
            regist_set.add(recommend)
            if len(regist_set) != r_len:
                answer = recommend
                break
            n += 1

    return answer

print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], 'ace15'))
# print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], 'cow'))
# print(int('b'))
# print(solution(["apple1", "orange", "banana3"], 'apple'))
# print(solution(["bird99", "bird98", "bird101", "gotoxy"], 'bird98'))