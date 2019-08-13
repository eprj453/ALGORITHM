import sys
sys.stdin = open('2_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    word = input()
    word_len = len(word)
    result = 'Exist'
    for j in range(0, word_len//2):
        if word[j] == '*' or word[word_len-j-1] == '*':
            result = "Exist"
            break
        if word[j] == word[word_len-j-1]:
            continue
        else:
            result = 'Not exist'
            break


    print('#{} {}'.format(i, result))