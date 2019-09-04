import sys
sys.stdin = open('5356_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    words = []
    max_len = 0
    for j in range(5):
        temp = list(input())
        if len(temp) > max_len:
            max_len = len(temp)
        words.append(temp)
    new_word = ''

    count = 1
    for j in range(max_len):
        for k in range(5):
            if len(words[k]) < count:
                continue
            else:
                new_word += words[k][j]
        count += 1
    print('#{} {}'.format(i, new_word))


