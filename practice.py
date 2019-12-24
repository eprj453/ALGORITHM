class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount+1:
            return False
        else:
            i = 1
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
            return curr

    def insertAt(self, pos, new):
        if pos < 0 or pos > self.nodeCount+1:
            return False
        if pos == 1: # 첫 위치에 삽입
            new.next = self.head # 새로운 노드의 다음은 기존의 첫 원소로
            self.head = new # # 첫 원소는 새로운 노드로
        else:
            if pos == self.nodeCount+1: # 만약 맨 끝에 원소를 넣으려고 한다면
                prev = self.tail # 직전 원소는 기존의 맨 마지막 원소로
            else:
                prev = self.getAt(pos-1) # 직전 원소는 구하고자 하는 원소의 -1번째 원소로
            new.next = prev.next # new의 next는 직전 원소의 head로
            prev.next = new # 직전 원소는 새로운 원소를 가리킨다.

        if pos == self.nodeCount + 1:
            self.tail = new

        self.nodeCount += 1
        return True






a = Node(67)
b = Node(31)
c = Node(22)

list1 = LinkedList()

list1.insertAt(1, a)
list1.insertAt(2, b)
list1.insertAt(3, c)
d = Node(11)
list1.insertAt(2, d)
print(list1)
