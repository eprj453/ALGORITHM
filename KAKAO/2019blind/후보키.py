# temp = []
#
# def canCandidate(relation, col):
#     row = set()
#     for rel in relation:
#         tmp = []
#         for c in col:
#             tmp.append(rel[c])
#         if tuple(tmp) in row:
#             return 0
#         row.add(tuple(tmp))
#     return 1
# def comb(k, start, arr, l, relation, answer):
#     ans = []
#     if k == l:
#         if canCandidate(relation, temp):
#             ans.append(tuple(temp))
#         return
#
#     for i in range(start, len(arr)):
#         temp.append(arr[i])
#         for t in answer:
#             if set(t).issubset(set(temp)):
#                 break
#         else:
#             comb(k+1, i+1, arr, l, relation,answer)
#         temp.pop()
#
#     return ans
# def solution(relation):
#     answer = set()
#     arr = [x for x in range(0, len(relation[0]))]
#     print(arr)
#     for i in range(len(relation)+1):
#         addCandidate = comb(0, 0, arr, i ,relation, answer)
#         if addCandidate:
#             for a in addCandidate:
#                 answer.add(a)
#
#     print(answer)
#     return len(answer)
import itertools

def canCandidate(col, answer, relation):
    temp = set()

    for i in range(1, len(col)+1):
        c = tuple(col[0:i])
        for t in answer:
            if set(c).issubset(set(t)):
                return 0

    for rel in relation:
        c = tuple([rel[x] for x in col])
        if c in temp:
            return 0
        temp.add(c)
    return 1


def solution(relation):
    cols = [x for x in range(len(relation[0]))]
    answer = set()
    for i in range(1, len(relation[0])+1):
        arr = list(itertools.combinations(cols, i))
        for col in arr:
            if canCandidate(list(col), answer, relation):
                answer.add(tuple(col))
    return len(answer)
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))