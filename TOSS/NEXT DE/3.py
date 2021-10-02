# 토스 유저의 송금 퍼널을 분석해보자

from itertools import permutations
import math

# class LogInfo:
#     def __init__(self, log_time, log_id, log_type, log_name, svc_id, user_no, network, os, app_ver):
#         self.log_time = log_time
#         self.log_id = log_id
#         self.log_type = log_type
#         self.log_name = log_name
#         self.svc_id = svc_id
#         self.user_no = user_no
#         self.network = network
#         self.os = os
#         self.app_ver = app_ver
#
#     def __str__(self):
#         return ()


def generate_page_change_dict(pages):
    page_change_dict = dict()
    for i in range(0, len(pages) - 1):
        curr_page, next_page = pages[i], pages[i + 1]
        page_change_dict[f'{curr_page}{next_page}'] = set()
    return page_change_dict


def sort_dict_values(d: dict):
    for k, v in d.items():
        d[k] = sorted(v, key=lambda x:x[0])

    return d

def get_min_rate(d: dict):
    min_rate = min([v for v in d.values()])

    for k, v in d.items():
        if v == min_rate:
            return min_rate, k

# class Android:
#     def __init__(self):
#         self.pages = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#         self.page_count = {v: 0 for v in self.pages}
#         self.page_change_count = generate_page_change_dict(self.pages)
#
#
# class IOS:
#     def __init__(self):
#         self.pages = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#         self.page_count = {v: 0 for v in self.pages}
#         self.page_change_count = generate_page_change_dict(self.pages)


log_name_dict = {
    'home': 'A',
    'transfer': 'B',
    'account_tab': 'C',
    'enter_account_no': 'D',
    'enter_transfer_amount': 'E',
    'transfer_decision': 'F',
    'enter_password': 'G',
    'transfer_complete': 'H'
}

log_name_reverse = {v: k for k, v in log_name_dict.items()}

page_rate_dict = {
    'A': 'AB',
    'B': 'BC',
    'C': 'CD',
    'D': 'DE',
    'E': 'EF',
    'F': 'FG',
    'G': 'GH'
}

page_rate_reverse = {v: k for k, v in page_rate_dict.items()}


android_user_dict, ios_user_dict = dict(), dict()


pages = [v for v in log_name_dict.values()]
android_page_dict, ios_page_dict = {v: set() for v in pages}, {v: set() for v in pages}
android_page_change_dict, ios_page_change_dict = generate_page_change_dict(pages), generate_page_change_dict(pages)

android_page_change_rate, ios_page_change_rate = dict(), dict()

n = int(input())

for _ in range(n-1):
    log_time, log_id, log_type, log_name, svc_id, user_no, network, os, app_ver = input().split(',')
    if not log_name_dict.get(log_name): continue

    user_os_dict = android_user_dict if os == 'android' else ios_user_dict
    user_os_dict[user_no] = user_os_dict.get(user_no, [])

    user_os_dict[user_no].append(
        (log_time, log_name_dict[log_name])
    )




    # print(log_time)

android_user_dict = sort_dict_values(android_user_dict)
ios_user_dict = sort_dict_values(ios_user_dict)



for user_no, logs in android_user_dict.items():
    for idx in range(len(logs)):

        if idx == len(logs)-1:
            t, curr_page = logs[idx]
            android_page_dict[curr_page].add(user_no)
        else:
            t, curr_page = logs[idx]
            next_page = logs[idx+1][1]

            android_page_dict[curr_page].add(user_no)
            android_page_change_dict[f'{curr_page}{next_page}'].add(user_no)


for user_no, logs in ios_user_dict.items():
    for idx in range(len(logs)):
        if idx == len(logs)-1:
            t, curr_page = logs[idx]
            ios_page_dict[curr_page].add(user_no)
        else:
            t, curr_page = logs[idx]
            next_page = logs[idx+1][1]

            ios_page_dict[curr_page].add(user_no)
            ios_page_change_dict[f'{curr_page}{next_page}'].add(user_no)


for page in pages:
    if page == 'H': break
    page_change = page_rate_dict[page]

    android_page_change, android_page = len(android_page_change_dict[page_change]), len(android_page_dict[page])
    ios_page_change, ios_page = len(ios_page_change_dict[page_change]), len(ios_page_dict[page])
    print(android_page_change, android_page)
    android_page_change_rate[page_change] = math.trunc((android_page_change / android_page) * 100)
    ios_page_change_rate[page_change] = math.trunc((ios_page_change / ios_page) * 100)

# print(android_page_change_rate)

android_min_rate, android_p = get_min_rate(android_page_change_rate)
ios_min_rate, ios_p = get_min_rate(ios_page_change_rate)

print(f'android,{log_name_reverse[android_p[0]]},{log_name_reverse[android_p[1]]},{str(android_min_rate)}%')
print(f'ios,{log_name_reverse[ios_p[0]]},{log_name_reverse[ios_p[1]]},{str(ios_min_rate)}%')

# # android_min_
# print(ios_page_change_rate)


# print(sorted(ios_dict['0']))