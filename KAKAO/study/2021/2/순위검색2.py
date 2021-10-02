def get_subset(arr):
    n = len(arr)
    result = []
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(j)
        temp_arr = arr[:]
        for idx in temp:
            temp_arr[idx] = '-'
        result.append(' '.join(temp_arr))
    return result

def get_answer_by_binary_search(score, arr):
    if not arr: return 0
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
    answer = []
    answer_dict = {}
    for i in info:
        i = i.split(' ')
        for res in get_subset(i[:-1]):
            answer_dict[res] = answer_dict.get(res, [])
            answer_dict[res].append(int(i[-1]))

    for value in answer_dict.values():
        if value:
            value.sort()

    for q in query:
        q_list = q.split(' ')
        score = int(q_list.pop())
        q_list = [word for idx, word in enumerate(q_list) if idx%2 == 0]
        condition = ' '.join(q_list)
        answer.append(get_answer_by_binary_search(score, answer_dict.get(condition)))

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] ))