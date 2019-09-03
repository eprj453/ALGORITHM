
# 첫번째 노드로 삽입
#class Node:
#     def __init__(self, data, link):
#         self.data = data
#         self.link = link
#
# def addtoFirst(data):
#     global Head
#     Head = Node(data, Head)
#
#
# def add(pre, data):
#     if pre == Node:
#         print('error')
#     else:
#         pre.link = Node(data, pre.link)
#
# data = [1,2,3,4]
# Head = None
#
# for i in range(len(data)):
#     addtoFirst(data[i])
#
# add(Head, 8)
#
# while Head.link != None:
#     print(Head.data, end=' ')
#     Head = Head.link
# print(Head.link)



class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def add(pre, data):
    if pre == Node:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data): # 마지막에 데이터 삽입
    global Head
    if Head == None: # 빈 리스트라면
        Head = Node(data, None) # Head 하나 생성

    else:
        p = Head
        while p.link != None:
            p = p.link

        p.link = Node(data, None)



Head = None

list1 = [1, 2, 3, 4]
for i in range(len(list1)):
    addtoLast(list1[i])

#
while Head.link != None:
    print(Head.data, end=' ')
    Head = Head.link
    # Head = Head.link



# print(list1)
# def add(pre, data):
#     if pre == Node:
#         print('error')
#     else:
#         pre.link = Node(data, pre.link)

# data = [1,2,3,4]
# Head = None
#
# for i in range(len(data)):
#     addtoLast(data[i])
#
# # add(Head, 8)
#
# while Head.link != None:
#     print(Head.data, end=' ')
#     Head = Head.link
# print(Head.link)