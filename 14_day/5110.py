import sys
sys.stdin = open('5110_input.txt', 'r')


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





t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    l_list = LinkedList()
    # temp1 = list(map(int, input().split()))
    # num = 1
    # for j in range(len(temp1)):
    #     temp = Node(temp1[j])
    #     l_list.insertAt(num, temp)
    #     num += 1
    for j in range(m):
        temp2 = list(map(int, input().split()))
        # print('nodecount : ',l_list.nodeCount)
        num = 1
        num2 = 0
        result = False
        while num < l_list.nodeCount+1:
            if l_list.getAt(num).data > temp2[0]:
                result = True
                num2 = num
                for k in range(len(temp2)):
                    temp = Node(temp2[k])
                    l_list.insertAt(num2, temp)
                    num2 += 1
                break
            num += 1
        if result == False:
            num2 = l_list.nodeCount+1
            for k in range(len(temp2)):
                temp = Node(temp2[k])
                l_list.insertAt(num2, temp)
                num2 += 1
    # print(l_list)
    num = 1
    curr = l_list.head
    ans = []
    while num < l_list.nodeCount+1:
        if num > l_list.nodeCount - 10:
            # print(curr.data, end = ' ')
            ans.insert(0, str(curr.data))
        curr = curr.next
        num += 1
    print('#{} {}'.format(i, ' '.join(ans)))
    # print('#{} '.format(i), end = '')
    # num = 0
    # while l_list.next != None:
    #     l_list = l_list.next
    #     num += 1
    # num2 = 10
    # while num2 > 0:
    #     print(l_list.data, end = ' ')
    #
    #     num2 -= 1
    # print()
# a = Node(21)
# b = Node(32)
# c = Node(64)
# d = Node(80)
# e = [Node(62), Node(22)]
# list1 = LinkedList()
# list1.insertAt(1, a)
# list1.insertAt(2, b)
# list1.insertAt(3, c)
# list1.insertAt(2, d)
# n = 2
# for i in range(len(e)):
#     list1.insertAt(n, e[i])
# print(list1)
# print(list1.getAt(2).data)


# # def add(pre, data):
# #     if pre == None:
# #         print('error')
# #     else:
# #         pre.link = Node(data, pre.link)
#
# def add(data, idx):
#     global Head
#     p = Head
#     n = 0
#     while n < idx-1:
#         p = p.link
#         n += 1
#     p.link = Node(data, p.link)
#
#
# def addtoLast(data): # 마지막에 데이터 삽입
#     global Head
#
#     if Head == None: # 빈 리스트라면
#         Head = Node(data, None) # Head 하나 생성
#
#     else:
#         p = Head
#         while p.link != None:
#             p = p.link
#         p.link = Node(data, None)


# t = int(input())
# for i in range(1, t+1):
#     n, m = map(int, input().split())
#     Head = None
#     list1 = list(map(int, input().split()))
