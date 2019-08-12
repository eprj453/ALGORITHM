import sys
sys.stdin = open('GNS_test_input.txt', 'r')

alian_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
t = int(input())
for i in range(1, t+1):
    str_list = list(map(str, input().split()))
    count_list = [0] * len(alian_list)
    num_list = list(input().split())
    for num in num_list:
        for a_num in range(len(alian_list)):
            if num == alian_list[a_num]:
                count_list[a_num] += 1

    print('#{}'.format(i))
    for j in range(len(count_list)):
        for k in range(count_list[j]):
            print(alian_list[j], end=' ')
    print()


