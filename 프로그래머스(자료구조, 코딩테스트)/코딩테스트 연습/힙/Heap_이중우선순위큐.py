import heapq


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#         self.parent = None
#
#
# class Tree:
#     def __init__(self):
#         self.center = None
#
#     def insert_node(self, node):
#         if not self.center:
#             self.center = node
#
#
#
#         else:
#             center = self.center
#             if node.value >= center.value: # node의 값이 center보다 크거나 같을 경우
#
#
#
#     def pop_max(self, node: Node):
#         if node.right_child is None:
#             max_value = node.value
#             if node.left_child:
#                 node.left_child.parent = node.parent
#                 node.parent.right_child = node.left_child
#             return max_value
#
#         else:
#             self.pop_max(node.right_child)
#
#     def pop_min(self, node: Node):
#         if node.left_child is None:
#             min_value = node.value
#             if node.right_child:
#                 node.right_child.parent = node.parent
#                 node.parent.left_child = node.right_child
#
#             return min_value
#
#         else:
#             self.pop_min(node.left_child)
#
#
#
# def solution(operations):
#     answer = []
#     tree = Tree()
#
#     return answer


def solution(operations):
    min_heap, max_heap = [], []
    for operation in operations:
        ope, num = operation.split(' ')
        if ope == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        else:
            if num == '-1' and min_heap:
                heapq.heappop(min_heap)
            elif num == '1' and max_heap:
                heapq.heappop(max_heap)

    print(min_heap)
    print(max_heap)
    min_answer = heapq.heappop(min_heap) if min_heap else 0
    max_answer = heapq.heappop(max_heap) if max_heap else 0

    return [-max_answer, min_answer]

a = solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
print(a)

b = solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
print(b)