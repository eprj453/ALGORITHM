def get_available_keys(info):
    n = len(info)

    available_keys = []

    for i in range(1 << n):
        temp = []
        for j in range(i):
            if i & (1 << j):
                temp.append(j)
        info_copy = info.copy()
        for t in temp:
            info_copy[t] = '-'
        available_key = ' '.join(info_copy)
        available_keys.append(available_key)

    return available_keys


def find_score(score, arr):
    start, end = 0, len(arr)
    mid = (start + end) // 2

    while start < end:
        mid = (start + end) // 2
        value = arr[mid]
        if value >= score:
            end = mid
        else:
            start = mid+1

    return len(arr) - end


def solution(info, query):
    query_dict = {}
    answer = []

    for i in info:
        i = i.split(' ')
        score = i[-1]
        other_info = i[:-1]
        all_available_keys = get_available_keys(other_info)

        for key in all_available_keys:
            query_dict[key] = query_dict.get(key, [])
            query_dict[key].append(int(score))

    for v in query_dict.values():
        v.sort()

    for q in query:
        l, p, y, f_s = q.split(' and ')
        f, s = f_s.split(' ')

        query_dict_key = ' '.join([l, p, y, f])
        if query_dict.get(query_dict_key):
            answer.append(find_score(int(s), query_dict[query_dict_key]))
        else:
            answer.append(0)

    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] ))