# 효율성 있음.
# 그러나 테스트 케이스가 많긴 하지만 재귀적으로 접근해도 깊이는 최대 5단계이고, 넓이도 그렇게 넓지 않음.

'''
[조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
언어는 cpp, java, python, - 중 하나입니다.
직군은 backend, frontend, - 중 하나입니다.
경력은 junior, senior, - 중 하나입니다.
소울푸드는 chicken, pizza, - 중 하나입니다.
'-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
'''

# info 배열에 -가 있는 것도 아니기 때문에, 메모리 공간을 크게 먹더라도
# 재귀적으로 파고들면 그렇게 어려운 문제는 아닌듯.

# 재귀로 하면 시간초과남 ㅋㅋㅋㅋㅋ

def get_answer_by_binary_search(score, arr):
    if not arr:
        return 0
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


def search_query(query, idx, search_value):
    key = query[idx]

    if idx == 4:
        target_score = int(query[idx])
        # print(search_value)
        score_list = search_value
        return get_answer_by_binary_search(target_score, sorted(score_list))
        # return len([x for x in score_list if x >= target_score])

    if key == '-':
        next_keys = search_value.keys()
        return_value = 0
        for key in next_keys:
            return_value += search_query(query, idx+1, search_value[key])
        return return_value

    else:
        return search_query(query, idx+1, search_value[key])


def solution(info, query):
    answer = []
    info_dict = {
        'java': {
            'backend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }
            }
        },
        'python': {
            'backend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }

            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }

            }
        },
        'cpp': {
            'backend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }

            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': []
                }

            }
        }
    }
    # 먼저 info를 등록
    for i in info:
        lan, pos, year, food, score = i.split(' ')
        info_dict[lan][pos][year][food].append(int(score))

    for q in query:
        l, p, y, f_s = q.split(' and ')
        f, s = f_s.split(' ')
        # print([l, p, y, f, s])
        answer.append(search_query([l, p, y, f, s], 0, info_dict))
        # print(answer)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] ))