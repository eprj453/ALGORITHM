# Node
# - data (어떤 데이터를 가지고 있는가)
# - link (다음 데이터와 이어지는 link가 무엇인가)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.tail = None

        # Dummy node 전
        # self.head = None

        # Dummy node 후
        self.head = Node(None)
        self.head.next = self.tail

    def getValue(self, value):
        nc = self.nodeCount
        print('nc :', nc)
        i = 0
        curr = self.head
        while i <= nc:
            if curr.data == value:
                return i
            else:
                curr = curr.next
            i += 1

    def getInputIdx(self, value):
        nc = self.nodeCount
        i = 0
        curr = self.head
        while i <= nc:
            if curr.data and curr.data > value:
                return i
            else:
                curr = curr.next
            i += 1
        return i

    def getAt(self, pos):

        # Dummy node 전
        # if pos < 1 and pos > self.nodeCount:
        #     return None
        # i = 1
        # curr = self.head
        # while i < pos:
        #     curr = curr.next
        #     i += 1
        # return curr

        # Dummy node 후

        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        answer = []
        curr = self.head
        # while curr != None:

        # Dummy node 전
        # while curr != None:
        #     answer.append(curr.data)
        #     curr = curr.next

        # Dummy node 후
        while curr and curr.next:
            curr = curr.next
            answer.append(curr.data)
            # curr = curr.next
        return answer

    def insertAt(self, pos, newNode):
        # Dummy node 삽입 전
        # if pos <= 0 or pos > self.nodeCount+1:
        #     return False
        # if pos == 1: # 맨 처음 노드에 삽입하려고 할때
        #     newNode.next = self.head #
        #     self.head = newNode
        #
        # else:
        #     if pos == self.nodeCount+1:
        #         prev = self.tail
        #     else:
        #         prev = self.getAt(pos-1) # 현재 삽입하고자 하는 원소의 앞 원소
        #     newNode.next = prev.next # 새로운 원소의 다음 원소를 앞 원소의 다음 원소로 끼워넣기
        #     prev.next = newNode # 기존 앞 원소의 다음 원소는 새로운 원소로
        #
        # if pos == self.nodeCount+1:
        #     self.tail = newNode
        # self.nodeCount += 1
        # return True

        # Dummy node 삽입 후
        if pos < 1 or pos > self.nodeCount+1:
            return False
        if pos != 1 and pos == self.nodeCount+1: # 맨 마지막 노드를 골랐을때
            prev = self.tail
        else:
            prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next == None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def popAt(self, pos):
        # popNode = self.getAt(pos)
        if pos < 1 or pos > self.nodeCount: # 0 미만 원소 길이 이상
            raise IndexError
            return False

        if self.nodeCount == 1: # node 길이가 1일때
            popNode = self.head
            self.head = None
            self.tail = None
        else:
            if pos == 1: # 맨 앞 node의 삭제
                popNode = self.head
                self.head = self.head.next
            elif pos == self.nodeCount: # 맨 끝 node의 삭제
                popNode = self.tail
                prev = self.getAt(pos-1)
                prev.next = None
                self.tail = prev
            else: # 그렇지 않은 경우
                popNode = self.getAt(pos)
                prev = self.getAt(pos-1)
                # popAfterNode = self.getAt(pos+1)
                prev.next = popNode.next

        self.nodeCount -= 1
        return popNode.data

    def concat(self, L): # 연결 리스트 합치는 연산
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
        return True



def solution(n, k, cmd):

    L = LinkedList()
    for i in range(n):
        node = Node(i)
        L.insertAt(i, node)

    print(L.traverse())


# solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])

L = LinkedList()
a = Node(12)
b = Node(30)
c = Node(47)
d = Node(68)

L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)
L.insertAt(4, d)

L.popAt(3)
print(L.traverse())
# L.popAt(1)
# print(L.getValue(12))
idx = L.getInputIdx(50)

L.insertAt(idx, Node(50))
print(L.traverse())
# print(L.traverse())
