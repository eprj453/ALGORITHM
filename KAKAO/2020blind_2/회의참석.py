def solution(sales, links):
    answer = 0
    n = len(sales)
    # parents = [[] for _ in range(n+1)]
    parents = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    min_children = [10000] * (n+1)
    # for idx, sale in enumerate(sales):

    infos = sorted([[idx+1, sale] for idx, sale in enumerate(sales)], key=lambda x:x[1])
    teams = [0] * (n+1)
    for link in links:
        p, c = link
        parents[c] = p
        min_children[c] = min()
        children[p].append(c)
    #
    # for info in infos:
    #     print('answer : ',answer)
    #     print(info)
    #
    #     num, sale = info
    #     if parents[num] and children[num]: # 팀장
    #         print('팀장, 팀 : ', parents[num])
    #         pt, mt = teams[parents[num]], teams[num]
    #         print('pt, mt : ',pt, mt)
    #         if teams[num]:
    #             if pt + mt > sale:
    #                 teams[parents[num]] = sale
    #                 teams[num] = sale
    #                 answer -= (pt+mt)
    #                 answer += sale
    #             else:
    #                 print('변경하지 않음')
    #         else:
    #             print('초기값 추가')
    #             teams[num] = sale
    #             answer += sale
    #
    #     elif parents[num]: # 팀원
    #         team = parents[num]
    #         print('팀원, 팀 : ', parents[num])
    #         if teams[team]: # 이미 값이 있을 경우\
    #             print('이미 값 있음,', teams[team])
    #             if sale < teams[team]:
    #                 # answer -= teams[num]
    #                 print('변경')
    #                 answer -= teams[team]
    #                 answer += sale
    #                 teams[team] = sale
    #             else:
    #                 print('변경하지 않음')
    #         else: # 값이 없을 경우
    #             print('초기값 추가')
    #             teams[team] = sale
    #             answer += sale
    #     else: # CEO
    #         print('ceo, 팀 : ', 1)
    #         if teams[num]:
    #             print('이미 값 있음,', teams[num])
    #             if sale < teams[num]:
    #                 print('변경')
    #                 answer -= teams[num]
    #                 answer += sale
    #                 teams[num] = sale
    #             else:
    #                 print('변경하지않음')
    #         else:
    #             print('초기값 추가')
    #             teams[num] = sale
    #             answer += sale
    #     print()
    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))