def find_children(node, children):
    count = 0
    if not children[node]:
        return 1
    for x in children[node]:
        count += find_children(x, children)
    return count
def solution(total_sp, skills):
    answer = []
    children_count = [0] * (len(skills) + 1)
    children = [[] for x in range(len(skills)+2)]
    for skill in skills:
        parent, child = skill
        children[parent].append(child)
    for x in range(1, len(skills)+2):
        print(find_children(x, children))

print(solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))