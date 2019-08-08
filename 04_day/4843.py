import sys
sys.stdin = open('4843_input.txt', 'r')

t = int(input())

for i in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    convert_list = []

    for j in range(len(num_list)-1, 0, -1):
        for k in range(0 ,j):
            if num_list[k] > num_list[k+1]:
                num_list[k], num_list[k+1] = num_list[k+1], num_list[k]

    for j in range(0, 5): # 10
        convert_list.append(str(num_list[len(num_list) - j - 1]))
        convert_list.append(str(num_list[j]))

    print('#{} {}'.format(i, ' '.join(convert_list)))
