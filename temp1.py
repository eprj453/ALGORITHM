#
# import itertools
#
# number_set = set()
#
#
# def add_number(dice, sequence, idx, number):
#     if idx == len(sequence):
#         number_set.add(number)
#         return
#
#     for n in dice[sequence[idx]]:
#         add_number(dice, sequence, idx+1, number+str(n))
#
#
#
#
#
# # print([1] + [2])
#
#
# def solution(dice):
#     answer = 0
#
#     n = len(dice)
#
#     for i in range(1, len(dice)+1):
#         perm = list(itertools.permutations([x for x in range(n)], i))
#         for p in perm:
#             add_number(dice, p, 0, '')
#
#     print(list(number_set))
#     number_arr = list(set([int(x) for x in list(number_set)]))
#
#     i = 0
#     for idx, number in enumerate(number_arr):
#         if idx > 0 and idx != number:
#             return idx
#
#
# # print(list(itertools.permutations([0,1,2,3], 3)))
# c = solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]	)
# b = solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]])
# print(c)


# res = False
# def check_rule(string: str):
#     global res
#     if string == 'a':
#         res = True
#         return
#
#     elif string.startswith('a'):
#         # if string.endswith('b'):
#         check_rule(string[1:])
#
#     elif string.endswith('a'):
#         # if string.startswith('b'):
#         check_rule(string[:-1])
#
#     elif string.startswith('b') and string.endswith('b'):
#         check_rule(string[1:-1])
#     else:
#         return
# #
# #


def check_rule(string: str):
    print(string)

    # print()
    a_idx = -1
    for i in range(len(string)):
        if string[i] == 'a':
            a_idx = i
            break
    else:
        return False

    a_cnt = string.count('a')
    print(a_cnt)
    b_cnt = string.count('b')

    string_arr = list(string)

    while string_arr and a_cnt:
        print(string_arr)
        while string_arr[0] == 'a':
            string_arr.pop(0)
            print('asd')
            a_cnt -= 1

        while string_arr[-1] == 'a':
            string_arr.pop()
            a_cnt -= 1

        i = 0
        while i < a_cnt:
            s, e = string_arr[0], string_arr[-1]
            if s == 'b' and e == 'b':
                string_arr.pop(0)
                string_arr.pop()
            else:
                break
    print()
    if string_arr == ['arr']:
        return True
    else:
        return False




    #
    #
    # l_cnt, r_cnt = string[:a_idx+1].count('b'), string[a_idx+1:].count('b')
    # print(a_idx)
    # print(l_cnt, r_cnt)
    # print(a_idx, len(string))
    # for i in range(a_idx, len(string)):
    #     if string[i] == 'a' and l_cnt == r_cnt:
    #         return True
    #
    #     if string[i] == 'b':
    #         l_cnt += 1
    #         r_cnt -= 1
    #
    # return False



def solution(a: list):
    answer = []
    for s in a:
        answer.append(check_rule(s))

    return answer




a = solution(["abab","bbaa","bababa","bbbabababbbaa", "baabaabab", "abbaa"])
print(a)
# arr = [1,2 , 3]
# print(arr[:-1])