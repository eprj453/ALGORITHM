import sys
sys.stdin = open('3752_input.txt', 'r')


#
# def check(s, e, score_sum):
#     if s == e:
#         ans_list.add(score_sum)
#     else:
#         check(s+1, e, score_sum + scores[s])
#         check(s+1, e, score_sum)

for i in range(1, int(input())+1):
    n = int(input())
    scores = list(map(int, input().split()))
    score_sum = 0
    ans_list = set()
    ans_list.add(0)
    for score in scores:
        for j in list(ans_list):
            ans_list.add(score+j)
    # for score in scores:
    #     score_sum += score
    # print(score_sum)
    # for i in range(len(scores)):
    #     for j in range(n):
    #         if i == j : continue
    #         ans_list.add(scores[i] + scores[j])

    print('#{} {}'.format(i, len(ans_list)))
    # ans_list = set()
    # check(0, n, 0)
    # print('#{} {}'.format(i, len(ans_list)))