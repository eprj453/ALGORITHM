import sys
sys.stdin = open('1_input.txt', 'r')

t = int(input())

for i in range(1, t+1):
    word = input()
    word_len = len(word)
    # print(word_len)
    result = 'Exist'
    for j in range(0, word_len//2):
        # print(word[j], word[word_len-j-1])
        if word[j] == '?' or word[word_len-j-1] == '?' or word[j] == word[word_len-j-1]:
            continue
        elif word[j] != word[word_len-j-1]:
            result = 'Not exist'
            break
        print('-------------')
    print('#{} {}'.format(i, result))
