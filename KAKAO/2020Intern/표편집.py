# Node
# - data (어떤 데이터를 가지고 있는가)
# - link (다음 데이터와 이어지는 link가 무엇인가)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.nodeCount = 0
#         self.tail = None
#         self.head = None
#
#     def get_value(self, value):
#         nc = self.nodeCount
#         # print('nc :', nc)
#         i = 0
#         curr = self.head
#         while i <= nc:
#             if curr.data == value:
#                 return i
#             else:
#                 curr = curr.next
#             i += 1
#
#     def get_at(self, pos):
#         if pos < 0 or pos > self.nodeCount+1:
#             return None
#
#         i = 0
#         curr = self.head
#         while i < pos:
#             curr = curr.next
#             i += 1
#         return curr
#
#     def traverse(self):
#         answer = []
#         curr = self.head
#
#         while curr is not None:
#             answer.append(curr.data)
#             curr = curr.next
#
#         return answer
#
#     def insert_at(self, pos, newNode):
#         if pos < 0 or pos > self.nodeCount + 1:
#             return False
#
#         # print(pos)
#         if pos == 0:
#             newNode.next = self.head
#             self.head = newNode
#
#         else:
#             if pos == self.nodeCount + 1:
#                 prev = self.tail
#             else:
#                 prev = self.get_at(pos-1)  # 현재 삽입하고자 하는 원소의 앞 원소
#
#             newNode.next = prev.next  # 새로운 원소의 다음 원소를 앞 원소의 다음 원소로 끼워넣기
#             prev.next = newNode  # 기존 앞 원소의 다음 원소는 새로운 원소로
#
#         if pos == self.nodeCount + 1:
#             self.tail = newNode
#         self.nodeCount += 1
#         return True
#
#     def pop_at(self, pos):
#         # pop_node = self.get_at(pos)
#         if pos < 0 or pos > self.nodeCount:  # 0 미만 원소 길이 이상
#             raise IndexError
#
#         if self.nodeCount == 1:  # node 길이가 1일때
#             pop_node = self.head
#             self.head = None
#             self.tail = None
#         else:
#             if pos == 0:  # 맨 앞 node의 삭제
#                 pop_node = self.head
#                 self.head = self.head.next
#             elif pos == self.nodeCount:  # 맨 끝 node의 삭제
#                 pop_node = self.tail
#                 prev = self.get_at(pos-1)
#                 prev.next = None
#                 self.tail = prev
#             else:  # 그렇지 않은 경우
#                 pop_node = self.get_at(pos)
#                 prev = self.get_at(pos-1)
#                 # popAfterNode = self.get_at(pos+1)
#                 prev.next = pop_node.next
#
#         self.nodeCount -= 1
#         return pop_node.data
#         # return f{pop_node.data}
#
#     def get_input_idx(self, value):
#         # print("VALue!!!! ", value)
#         nc = self.nodeCount
#         i = 0
#         curr = self.head
#         # print(f"self.head!! : {curr.data}")
#         while i < nc:
#             if curr.data and curr.data > value:
#                 return i
#             else:
#                 curr = curr.next
#             i += 1
#         return i
#
#
# def solution(n, k, cmd):
#     L = LinkedList()
#
#     for i in range(n):
#         node = Node(i)
#         L.insert_at(i, node)
#
#     print(L.traverse())
#     print()
#     pop_node_queue = []
#
#     first_pos = k
#     curr_pos = first_pos
#     for c in cmd:
#         print("COMMAND!!! : ",c)
#         print('curr_pos : ',curr_pos)
#         if len(c) == 1:  # 삭제하거나 복구하거나
#             if c == 'C':
#                 pop_node = L.pop_at(curr_pos)
#                 pop_node_queue.append(pop_node)
#
#                 if curr_pos == L.nodeCount:
#                     curr_pos -= 1
#
#             else:
#                 recovery_value = pop_node_queue.pop()
#                 recovery_value = int(recovery_value)
#                 recovery_idx = L.get_input_idx(recovery_value)
#
#                 recovery_node = Node(recovery_value)
#                 L.insert_at(recovery_idx, recovery_node)
#
#                 if curr_pos <= recovery_idx:
#                     curr_pos += 1
#         else:
#             ud, cnt = c.split(' ')
#             cnt = int(cnt)
#             if ud == 'U':
#                 curr_pos -= cnt
#             else:
#                 curr_pos += cnt
#         print(L.traverse())
#         print()
#
#     # print(L.traverse())
#     ox = ['X'] * n
#     for i in L.traverse():
#         # print(str(i))
#         idx = int(i)
#         ox[idx] = 'O'
#     return ''.join(ox)
#     # print(L.nodeCount)

import heapq


def solution(n, k, cmd):

    left_queue, right_queue = [], []
    delete_queue = []

    mask = ['X'] * n

    for i in range(n):
        heapq.heappush(right_queue, i)

    for i in range(k):
        heapq.heappush(left_queue, -(heapq.heappop(right_queue)))

    for c in cmd:
        if len(c) == 1:
            if c == 'C':
                delete_queue.append(heapq.heappop(right_queue))
                if not right_queue:
                    heapq.heappush(right_queue, -(heapq.heappop(left_queue)))
            else:
                recover = delete_queue.pop()
                idx = heapq.heappop(right_queue)

                if idx < recover:
                    heapq.heappush(right_queue, recover)
                else:
                    heapq.heappush(left_queue, -recover)

                heapq.heappush(right_queue, idx)

        else:
            ud, interval = c.split(' ')
            interval = int(interval)
            if ud == 'U':
                for _ in range(interval):

                    heapq.heappush(right_queue, -(heapq.heappop(left_queue)))
            else:
                for _ in range(interval): # down
                    heapq.heappush(left_queue, -(heapq.heappop(right_queue)))

    while left_queue:
        idx = -(heapq.heappop(left_queue))
        mask[idx] = 'O'

    while right_queue:
        idx = heapq.heappop(right_queue)
        mask[idx] = 'O'


    return ''.join(mask)

    print(''.join(mask))



solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
