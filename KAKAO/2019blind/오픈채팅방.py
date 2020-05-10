def solution(record):
    answer = []
    nickname_dict = {}
    for rec in record:
        rec = rec.split(" ")
        if len(rec) == 2: # 떠난다
            user_id = rec[1]
            answer.append(user_id+'님이 나갔습니다.')
        else:
            cmd, user_id, nickname = rec[0], rec[1], rec[2]
            if cmd == 'Change':
                nickname_dict[user_id] = nickname
            else:
                #if nickname_dict.get(user_id) == None:
                nickname_dict[user_id] = nickname
                answer.append(user_id+'님이 들어왔습니다.')
    for i in range(len(answer)):
        n = answer[i].find('님')
        user_id = answer[i][0:n]
        answer[i] = answer[i].replace(user_id, nickname_dict[user_id])

    return answer