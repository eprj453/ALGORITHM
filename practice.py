def summary(word):
    count = 0
    count_char = ''

    for idx in range(0, len(word)):
        if idx == len(word) - 1:
            if word[idx] == word[idx - 1]:
                count += 1
                count_char += (word[idx - 1] + str(count))
            elif word[idx] != word[idx - 1]:
                count_char += (word[idx - 1] + str(count))
                count_char += word[idx]
                count_char += '1'
            break
        elif idx > 0 and word[idx] != word[idx - 1]:
            count_char += word[idx - 1]
            count_char += str(count)
            count = 1
        else:
            count += 1

    return count_char


# def summary(word):
#     result = []
#     tmp_list = []
#
#     for char in word:
#         if tmp_list and tmp_list[-1] != char:
#             result.append(tmp_list[-1])
#             result.append('{}'.format(len(tmp_list)))
#             tmp_list.clear()
#
#         tmp_list.append(char)
#     result.append(tmp_list[-1])
#     result.append('{}'.format(len(tmp_list)))

print(summary('aabbaacc'))
print(summary('ffgggeeeef'))
print(summary('abcdefg'))