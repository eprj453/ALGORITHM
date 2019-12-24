# 1204. 최빈수 구하기

t = int(input())
n = 0
while n < t:
    testcase_num = int(input())
    testcase = list(map(int, input().split()))
    compare_list = [0] * 101
    for i in testcase:
        compare_list[i] += 1
    max = compare_list[0]
    max_idx = 0
    for j in range(0, len(compare_list)):
        if compare_list[j] > max:
            max = compare_list[j]
            max_idx = j
    duplicate_list = []
    for idx, value in enumerate(compare_list):
        if value == max:
            duplicate_list.append(idx)
    answer = duplicate_list[-1]
    print('#{} {}'.format(testcase_num, answer))
    n += 1