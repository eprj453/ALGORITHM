
ans = 0
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    checked = [False] * 26
    word = input()
    isGroup = True
    # print(i,"번째")
    for l in range(len(word)-1):
        checked[alphabets.index(word[l])] = True
        # print('{} , {}'.format(word[l], word[l+1]))
        if word[l] != word[l+1]:
            # print(checked)
            if checked[alphabets.index(word[l+1])] == True:
                # print('걸림 : {}번째 {}'.format(l+1, word[l+1]))
                isGroup = False
                break
            else:
                checked[alphabets.index(word[l+1])] = True

    if isGroup == True:
        ans += 1

print(ans)

