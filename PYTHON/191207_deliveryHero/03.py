def cut(cut_count, s, e, word, temp_word):
    global min_count
    if cut_count >= min_count:
        return
    if s == e:
        min_count = min(min_count, cut_count+1)
        return

    before = len(temp_word)
    temp_word.add(word[s])
    after = len(temp_word)
    if before == after:
        cut(cut_count+1, s+1, e, word, {word[s]})
    else:
        cut(cut_count, s+1, e, word, temp_word)




def solution(S):
    global min_count
    cut(0, 0, len(S), S, set())
    # min_count = 0 if min_count == 0 else min_count+1
    return min_count

min_count = 0xffffff
print(solution('abba'))


