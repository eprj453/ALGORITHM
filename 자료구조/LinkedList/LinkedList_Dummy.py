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
        self.head = Node(None)
        self.head.next = self.tail



    def getAt(self, pos):

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

        while curr and curr.next:
            curr = curr.next
            answer.append(curr.data)
        return answer

    def insertAt(self, pos, newNode):
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
                prev.next = popNode.next

        self.nodeCount -= 1
        return popNode.data

    # def popAfter(self, prev):



    def concat(self, L): # 연결 리스트 합치는 연산
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
        return True