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
        # else:
        #     if pos == self.nodeCount: # 맨 끝 node의 삭제
        #         self.tail = self.getAt(pos-1) # node의 맨 끝을 그 앞 원소로
        #     elif pos == 1: # 맨 앞 node의 삭제
        #


    def popAfter(self, prev):



    def concat(self, L): # 연결 리스트 합치는 연산
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
        return True
L = LinkedList()

a = Node(67)
b = Node(30)
c = Node(12)
d = Node(27)
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)
# L.insertAt(4, d)
# L.insertAfter(1, a)
# print(L.getAt(3).data)
print(L.traverse())
# L.insertAt(2, c)
L.popAt(1)

# L.insertAt(1, b)
# L.insertAt()1
# print(L.nodeCount)
print(L.traverse())
# print(L.getAt(1).item)