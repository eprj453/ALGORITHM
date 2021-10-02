def solution(id_list, report, k):
    answer = []

    report_dict = dict()  # key: 신고 당한사람(string) / value: 신고한 사람(set)
    reported_dict = dict() # key: 신고한 사람 (str) / value : 신고한 ID (set)
    for r in report:
        i, j = r.split(' ')  # i: 신고한 사람 / j: 신고한 ID
        reported_dict[j] = reported_dict.get(j, set())
        reported_dict[j].add(i)

        report_dict[i] = report_dict.get(i, set())
        report_dict[i].add(j)

    # k번 이상 신고당한 ID만 집합으로 list up
    reported = set([key for key, value in reported_dict.items() if len(value) >= k])

    print(report_dict)

    for user_id in id_list:
        print(user_id)
        report_count = report_dict.get(user_id, set())
        mail_count = len(report_count & reported) if report_count else 0
        answer.append(mail_count)


    return answer

a = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(a)