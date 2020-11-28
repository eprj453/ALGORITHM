import sys

sys.stdin = open('5110_input.txt', 'r')


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def merge(self, array):
        start = self.head
        # print('start : ', start)
        if not start:  # 빈 linkedlist
            self.head = array.head
            # print('array.head : ', array.head.data)
            self.tail = array.tail
            return

        flag = array.head.data
        while start:
            if start.data > flag:
                break
            start = start.next

        if not start:  # 맨 뒤로 merge
            array.head.prev = self.tail
            self.tail.next = array.head
            self.tail = array.tail

        elif start.data == self.head.data:  # 맨 앞으로 merge
            self.head.prev = array.tail
            array.tail.next = self.head
            self.head = array.head

        else:  # 사이에 merge

            start_prev = start.prev

            start_prev.next = array.head
            array.head.prev = start_prev

            array.tail.next = start
            start.prev = array.tail


    def add(self, data):
        new_node = Node(data)
        if not self.head:  # 빈 linkedlist일 경우
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next

    def traverse(self):
        result = []
        start = self.head
        while start:
            result.append(start.data)
            start = start.next
        return result

    def back_traverse(self):
        result = []
        start = self.tail
        i = 0
        while start and i < 10:
            result.append(start.data)
            start = start.prev
            i += 1
        return result

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    linked_list = LinkedList()
    for _ in range(m):
        array = list(map(int, input().split()))
        merge_linked_list = LinkedList()
        for num in array:
            merge_linked_list.add(num)
        linked_list.merge(merge_linked_list)
    print('#{}'.format(i), end=' ')
    print(' '.join(map(str, linked_list.back_traverse())))
    # print('answer : ',linked_list.back_traverse())

# linked_list = LinkedList()
# linked_list.add(1)
# linked_list.add(2)
# linked_list.add(3)
# print(linked_list.traverse())
