# CTR

import math

n = int(input())
A, B = set(), set()

user_logs = dict()

for _ in range(n):
    a, b = input().split(',')
    A.add(a)
    B.add(b)

m = int(input())

a_visit_users = set()
b_visit_users = set()

a_change_users = set()
b_change_users = set()

for _ in range(m):
    log_time, log_id, log_type, log_name, svc_id, user_no, network, os, app_ver = input().split(',')
    # print(user_no)
    if log_name in ['home', 'banner_click']:

        user_logs[user_no] = user_logs.get(user_no, [])
        user_logs[user_no].append(
            (log_time, log_name)
        )

for user_n, logs in user_logs.items():

    if len(logs) == 1:
        event = logs[0][1]
        if event == 'home':
            if user_n in A:
                a_visit_users.add(user_n)
            elif user_n in B:
                b_visit_users.add(user_n)

    else:
        for i in range(len(logs)-1):
            curr_event, next_event = logs[i][1], logs[i+1][1]
            if curr_event == 'home':
                if user_n in A:
                    a_visit_users.add(user_n)
                elif user_n in B:
                    b_visit_users.add(user_n)

                if next_event == 'banner_click':
                    if user_n in A:
                        a_change_users.add(user_n)
                    elif user_n in B:
                        b_change_users.add(user_n)



print(f'A,{ math.trunc( (len(a_change_users) / len(a_visit_users) * 100))}%')
print(f'B,{ math.trunc( (len(b_change_users) / len(b_visit_users) * 100))}%')


