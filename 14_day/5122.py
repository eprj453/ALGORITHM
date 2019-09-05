import sys
sys.stdin = open('5122_input.txt', 'r')

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
            new.next = self.head
            self.head = new
        else:
            if pos == self.nodeCount+1:
                prev = self.tail
            else:
                prev = self.getAt(pos-1)
            new.next = prev.next
            prev.next = new

        if pos == self.nodeCount + 1:
            self.tail = new
        self.nodeCount += 1
        return True

    def deleteAt(self, pos):
        if pos < 0 or pos > self.nodeCount+1:
            return False
        if pos == 1:
            self.head = self.getAt(2)
        else:



t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    for j in range(m):
        ope = list(input().split())
        if ope[0] == 'D':
            nums.pop(int(ope[1]))
        elif ope[0] == 'I':
            nums.insert(int(ope[1]), int(ope[2]))
        else:
            nums[int(ope[1])] = int(ope[2])
    print('#{} '.format(i))
    if l < len(nums):
        print(nums[l])
    else:
        print(-1)
