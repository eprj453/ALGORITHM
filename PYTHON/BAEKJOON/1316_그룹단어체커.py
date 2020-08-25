
ans = 0
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    checked = [False] * 26
    word = input()
    # isGroup = True
    # print(i,"번째")
    for l in range(len(word)-1):
        checked[alphabets.index(word[l])] = True
        # print('{} , {}'.format(word[l], word[l+1]))
        if word[l] != word[l+1]:
            # print(checked)
            if checked[alphabets.index(word[l+1])]:
                break
            else:
                checked[alphabets.index(word[l+1])] = True

    else:
        ans += 1

print(ans)

