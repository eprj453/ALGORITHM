def solution(ip_addrs, langs, scores):
    answer = len(ip_addrs)
    cheated_students = [False] * len(ip_addrs)
    cheated_ip = {}
    ip_dict = {}
    for idx, ip in enumerate(ip_addrs):
        if cheated_ip.get(ip): # 부정 i로 판별될 경우 무조건 부정참가자
            answer -= 1
            cheated_ip[ip].append(idx)
            continue
        if not ip_dict.get(ip): # 처음 등장하는 IP인 경우
            ip_dict[ip] = {
                'total' : [],
                'C_FAMILY' : [],
                'C' : [],
                'C++': [],
                'C#' : [],
                'Java' : [],
                'JavaScript': [],
                'Python3': []
            }
            ip_dict[langs[idx]].append(idx)
            l = langs[idx]
            if l == 'C' or l == 'C++' or l == 'C#':
                ip_dict['C_FAMILY'].append(idx)
        else: # 이미 한번 나온 ip인 경우
            ip_dict[ip]['total'].append(idx)
            ip_dict[ip][langs[idx]].append(idx)
            total = ip_dict[ip]['total']
            c = ip_dict[ip]['C_FAMILY']
            if len(total) == 4:
                cheated_ip[ip] = total
                for i in total:
                    if cheated_students[i] == False:
                        cheated_students[i] = True
                        answer -= 1
            elif len(c) == 3:
                my_lan = ip_dict[ip][langs[idx]]
                if len(ip_dict[ip][my_lan]) == 3:
                    for i in ip_dict[ip][my_lan]:
                        if cheated_students[i] == False:
                            cheated_students[i] = True
                            answer -= 1
                elif len(ip_dict[ip]['C_FAMILY']) == 3 and (langs[idx] =='C' or langs[idx] == 'C++' or langs[idx] == 'C#'): # 내 언어가 c 계열이고 c계열 언어 사용자가 3명 이상일 경우
                    for i in c:
                        if cheated_students[i] == False:
                            cheated_students[i] = True
                            answer -= 1
            else:
                if len(my_lan) == 2:
                   f,s = my_lan[0], my_lan[1]
                    if scores[f] == scores[s]:
                        for i in my_lan:
                            if not cheated_students[i]:
                                cheated_students[i] = True
                                answer -= 1
    return answer