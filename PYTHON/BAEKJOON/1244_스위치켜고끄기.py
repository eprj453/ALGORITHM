def switch(arg):
    if arg == 1:
        return 0
    elif arg == 0:
        return 1
    else:
        return

switch_len = int(input())
switch_list = list(map(int, input().split()))
student_num = int(input())
# 1 2 3 4 5 6 7 8
# 0 1 0 1 0 0 0 1
# 남학생 : 스위치 번호가 내가 받은 번호의 배수라면 스위치 변경
# 여학생 : 내가 받은 번호를 중심으로 양 옆이 대칭이 되는 경우를 조사해 대칭이 되는 범위만큼 스위치 변경
for i in range(student_num):
    gender_num = list(map(int, input().split()))
    gender, num = gender_num[0], gender_num[1] # 1 3

    if gender == 1:
        # print('gender: 1')
        for j in range(len(switch_list)):
            if (j+1) % num == 0:
                switch_list[j] = switch(switch_list[j])

    elif gender == 2:
        compare = 1
        switch_list[num-1] = switch(switch_list[num-1])
        while num-1-compare >= 0 and num-1+compare < switch_len:
            # print(num-1+compare, num-1-compare)
            if switch_list[num-1+compare] == switch_list[num-1-compare]:
                switch_list[num-1+compare] = switch(switch_list[num-1+compare])
                switch_list[num-1-compare] = switch(switch_list[num-1-compare])
                compare += 1
            else:
                break

count = 0
for j in range(switch_len):
    if count == 20:
        print()
        count = 0
    print(switch_list[j], end=' ')
    count += 1

# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1


