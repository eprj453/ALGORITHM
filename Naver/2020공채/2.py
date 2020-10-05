# class Pyramid:
#     def __init__(self, head):
#         self.head = Node(0, 0, None)
#
#     def traverse(self):
#         answer = []
#         n = self.head
#         pos = n.pos
#         floor = 0
#         while self.get_first_node(floor):
#             for k in sorted(n.children.keys()):
#                 answer.append(n.children.get(k))
#             floor += 1
#             n = self.get_first_node(floor)
#     def get_first_node(self, floor):
#         n = self.head
#         i = 0
#         while i < floor:
#             n = n.left
#         return n
#
# class Node:
#     def __init__(self, floor, pos, value):
#         self.floor = floor
#         self.pos = pos
#         self.value = value
#         self.left = Node(self, floor+1, pos, None)
#         self.right = Node(self, floor+1, pos+1, None)
#         self.parent = None
def is_all_filled(dictionary):
    for k in sorted(dictionary.keys()):
        for v in dictionary.get(k):
            if v is None:
                return False
    return True


def solution(blocks):
    answer = []
    pyramid = {}
    n = len(blocks)
    for i in range(n):
        pyramid[str(i)] = [None] * (i+1)
    for floor, block in enumerate(blocks):
        idx, value = block
        pyramid.get(str(floor))[idx] = value

    limit = 1
    for i in range(2, n+1):
        limit *= i
    i = 0
    while i < limit:
        for k in sorted(pyramid.keys()):
            floor = int(k)
            for idx, v in enumerate(pyramid.get(k)):
                if floor < n-1:
                    sel, left, right = v, pyramid.get(str(floor+1))[idx], pyramid.get(str(floor+1))[idx+1]
                    print(sel, left, right)
                    if sel is None:
                        if left != None and right != None:
                            pyramid[k][idx] = left+right
                    else:
                        if left is None:
                            if right is not None:
                                pyramid[str(floor+1)][idx] = sel-right
                        if right is None:
                            if left is not None:
                                pyramid[str(floor+1)][idx+1] = sel-left

        if is_all_filled(pyramid): break
        i += 1
    print(pyramid)

    for k in pyramid.keys():
        answer += pyramid.get(k)
    return answer

print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))