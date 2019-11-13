import sys
sys.stdin = open('4008_input.txt', 'r')



def calculate(s, count, add, sub, mul, div):
    global max_num
    global min_num
    # if s >= n+1:
    #     max_num = max(count, max_num)
    #     min_num = min(count, min_num)
    #     return

    if add + sub + mul + div == 0:
        max_num = max(count, max_num)
        min_num = min(count, min_num)
        return

    if add:
        calculate(s+1, count + nums[s], add-1, sub, mul, div)
    if sub:
        calculate(s+1, count - nums[s], add, sub-1, mul, div)
    if mul:
        calculate(s+1, count * nums[s], add, sub, mul-1, div)
    if div:
        calculate(s+1, int(count / nums[s]), add, sub, mul, div-1)

for i in range(1, int(input())+1):
    n = int(input())
    add, sub, mul, div = map(int, input().split())
    min_num = 100000000
    max_num = -100000000
    nums = list(map(int, input().split()))
    calculate(1, nums[0], add, sub, mul, div)
    # print(max_num)
    # print(min_num)
    print('#{} {}'.format(i, max_num - min_num))
    # print()
    # temp = [''] * (n-1)
    # print(temp)
    # visited = [False] * (n-1)
    # print('visited ' ,visited)
    # perm(0, my_opes)
    # for l in range(s+1, len(my_opes)):
    #     my_opes[s], my_opes[l] = my_opes[l], my_opes[s]

        # start = l
        # my_opes[s], my_opes[start] = my_opes[start], my_opes[s]
        # for k in range(start, len(my_opes)):
        #     # if my_opes[start] == my_opes[k]: continue
        #     my_opes[start], my_opes[k] = my_opes[k], my_opes[start]
        #     print(my_opes)
        #     my_opes[k], my_opes[start] = my_opes[start], my_opes[k]
        # # my_opes[start], my_opes[s] = my_opes[s], my_opes[start]
        # s += 1
    # print()