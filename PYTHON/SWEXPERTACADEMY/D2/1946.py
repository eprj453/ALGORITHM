t = int(input())

for i in range(1, t+1):
    answer = ''
    char_list = []
    n = int(input())
    sum = 0

    for j in range(0, n):
        char_list += [list(map(str, input().split()))]
        char_list[j][1] = int(char_list[j][1])
        sum += char_list[j][1]
    #print(char_list)
    row_count = 0
    count = 0
    num = 0
    for j in range(0, sum):
        answer += char_list[num][0]
        #print(answer)
        count += 1
        row_count += 1
        if count == char_list[num][1]:
            num += 1
            count = 0
        if row_count == 10:
            row_count = 0
            answer += '\n'

    print('#{} {}'.format(i, answer))
