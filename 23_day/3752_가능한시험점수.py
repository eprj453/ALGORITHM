import sys
sys.stdin = open('3752_input.txt', 'r')

def subset():
    ans_list = set()
    for i in range(1 << N):
        sum = 0
        for j in range(N + 1):
            if i & (1 << j):
                sum += scores[j]
        ans_list.add(sum)
    return len(ans_list)

for i in range(1, int(input())+1):
    n = int(input())
    scores = list(map(int, input().split()))
    N = len(scores)
    print('#{} {}'.format(i, subset()))


# for i in range(1, int(input())+1):
#     n = int(input())
#     scores = list(map(int, input().split()))
#     score_sum = 0
#     ans_list = set()
#     ans_list.add(0)
#     for score in scores:
#         for j in list(ans_list):
#             ans_list.add(score+j)
#
#     print('#{} {}'.format(i, len(ans_list)))