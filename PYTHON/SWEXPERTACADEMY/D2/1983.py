t = int(input())
for i in range(1, t+1):
    nk = list(map(int, input().split())) # 학생이 30명이라면 3명이 동일한 학점 # ex.30명 중 12번째의 학점은?
    score_list = []
    rank_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score_sum_list = []
    sorted_sum_list = []
    for j in range(0, nk[0]):
        score_list += [list(map(int, input().split()))]

    count = 0
    for k in range(0, len(score_list)):
        count = (score_list[k][0] * (35/100)) + (score_list[k][1] * (45/100) + score_list[k][2] * (20/100))
        score_sum_list.append(count)

    student_score = score_sum_list[nk[1]-1]
    student_idx = 0
    # 학생 위치와 합계 위치 동일
    # 합계를 정렬해 학점을 비교한다.
    sorted_sum_list = sorted(score_sum_list, reverse=True)

    for idx, value in enumerate(sorted_sum_list):
        if student_score == value:
            student_idx = idx

    m = nk[0] / 10
    q = student_idx // m

    print('#{} {}'.format(i, rank_list[int(q)]))







