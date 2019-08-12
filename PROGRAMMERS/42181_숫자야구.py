def solution(baseball):
    answer = 0
    ball_count = 0
    strike_count = 0
    num_list = []
    count_list = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                num_list.append(str(i)+str(j)+str(k))

    for i in range(len(baseball)): # 매개변수 탐색
        ball_count = 0
        strike_count = 0
        for j in range(len(str(baseball[i][0]))): # 매개변수의 i번째의 0번째, 숫자 탐색
            compare_num = str(baseball[i][0]) # 탐색할 숫자 변수 할당
            for num in num_list: # num_list의 원소와 하나씩 비교 시작
                for num_idx in range(3): # num_list의 원소 길이 3, 0번째부터 2번째까지 탐색
                    if num[num_idx] in compare_num:
                        ball_count += 1
                    if num[num_idx] == compare_num[num_idx]:
                        ball_count -= 1
                        strike_count += 1



    return answer



