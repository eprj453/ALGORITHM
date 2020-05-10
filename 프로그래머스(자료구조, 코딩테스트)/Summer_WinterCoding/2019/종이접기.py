# 0
# 0
# 0 0 1
# left = 0 0 1 0 0 1 1 0 0 0 1 1 0 1 1



def solution(n):
    center = [0]
    paper = []
    for i in range(n):
        paper = paper + center + list(reversed([n^1 for n in paper]))
    return paper

#
# print(left(0, 2, []))
print(solution(20))