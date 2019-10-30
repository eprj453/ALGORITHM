musicinfos = ['12:00','12:14','HELLO','C#DEFGAB', '13:00','13:05','WORLD','ABCDEF']


m = 'ABC'
# 12:55 13:18
# info_list = []
# for i in range(0, len(musicinfos), 4):
#     start, end = musicinfos[i], musicinfos[i+1]
#     # print(start[3:], end[3:])
#     if int(start[0:2])  == int(end[0:2]):
#         play_time = int(end[3:]) - int(start[3:])
#     else:
#         play_time = (60 - int(start[3:])) + end[3:]
#
#     codes = musicinfos[i+3]
#     t_codes = ''
#     if len(codes) >= play_time:
#         t_codes = codes[0:play_time]
#     else:
#         while True:
#             if len(t_codes) == play_time:
#                 break
#             for j in range(len(codes)):
#                 if len(t_codes) == play_time:
#                     break
#                 t_codes += codes[j]
#
#
#     info_list.append([musicinfos[i+2], t_codes])
#
# ans = ''
# ans_music_len = 0
# for i in range(0, len(info_list)):
#     if m in info_list[i][1]:
#         if len(info_list[i][1]) > ans_music_len:
#             ans_music_len = len(info_list[i][1])
#             ans = info_list[i][0]
#
# if not ans:
#     print(None)
# else:
#     print(ans)
            # ans =
# print(','.join(musicinfos))

info_list = []
play_time = 0
for i in range(0, len(musicinfos), 4):
    start, end = musicinfos[i], musicinfos[i+1]
    if int(start[0:2])  == int(end[0:2]):
        play_time = int(end[3:]) - int(start[3:])
    else:
        play_time = (60 - int(start[3:])) + int(end[3:])

    codes = musicinfos[i+3]
    t_codes = ''
    if len(codes) >= play_time:
        t_codes = codes[0:play_time]
    else:
        while True:
            if len(t_codes) == play_time:
                break
            for j in range(len(codes)):
                if len(t_codes) == play_time:
                    break
                t_codes += codes[j]


    info_list.append([musicinfos[i+2], t_codes])
print(info_list)
ans = ''
ans_music_len = 0
for i in range(0, len(info_list)):
    if m in info_list[i][1] and :
        if len(info_list[i][1]) > ans_music_len:
            ans_music_len = len(info_list[i][1])
            ans = info_list[i][0]

if not ans:
    answer = None
else:
    answer = ans

print(answer)

'''

['12:00','12:14','HELLO','CDEFGAB', '13:00','13:05','WORLD','ABCDEF']
['03:00','03:30','FOO','CC#B', '04:00','04:08','BAR','CC#BCC#BCC#B']
['12:00','12:14','HELLO','C#DEFGAB', '13:00','13:05','WORLD','ABCDEF']


'''