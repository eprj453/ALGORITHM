def dup_del(word_list):
    for idx in range(0, len(word_list)-1):
        if word_list[idx] == word_list[idx+1]:
            word_list.pop(idx)
            word_list.pop(idx+1)
            break
        dup_del(word_list)
    return word_list

t = int(input())
for i in range(1, t+1):
    # word_list = list(input())
    print('#{} {}'.format(i, dup_del(list(input()))))
