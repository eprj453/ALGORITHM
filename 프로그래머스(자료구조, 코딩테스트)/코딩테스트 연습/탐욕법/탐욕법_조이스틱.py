def solution(name):
    answer = 0
    notAcount = 0
    name = list(name)
    for n in name:
        if n != 'A':
            notAcount += 1
    s = 0
    while notAcount:
        left, lcnt = s, 0
        while name[left] == 'A' and lcnt < len(name):
            left -= 1
            lcnt += 1
        right, rcnt = s, 0
        while name[right] == 'A' and rcnt < len(name):
            right += 1
            rcnt += 1

        answer += min(lcnt, rcnt)

        if lcnt < rcnt:
            s = left
        else:
            s = right

        tgt = name[s]

        answer += min(ord(tgt) - ord('A'), ord('Z') - ord(tgt) + 1)
        name[s] = 'A'
        notAcount -= 1
    print(name)
    return answer

# def solution(name):
#     answer = 0
#     name = list(name)
#     compare = ['A' for _ in range(len(name))]
#     notAcount = 0
#
#     pos = 0
#     while name != compare:
#         print(name)
#         print(compare)
#         # print(notAcount)
#         left, lc = pos, 0
#         right, rc = pos, 0
#         while compare[left] == name[left]:
#             left -= 1
#             lc += 1
#         while compare[right] == name[right]:
#             right += 1
#             rc += 1
#         # print(lc, rc)
#         # print(left, right)
#         print(min(lc, rc))
#         answer += min(lc, rc)
#         if lc <= rc:
#             pos = left
#         else:
#             pos = right
#         print('pos : ', pos)
#         tgt = name[pos]
#         # cpr = compare[pos]
#
#         left = ord('Z') - ord(tgt) + 1
#         right = ord(tgt) - ord('A')
#
#         print(min(left, right))
#         answer += min(left, right)
#         compare[pos] = name[pos]
#         print('answer : ', answer)
#     print()
#     print(name)
#     print(compare)
#     return answer
# # print(list('hello'))
print(solution('JAAYAZAAZ'))
# print(solution('JAZ'))
# print(ord('I') - ord('A'))

